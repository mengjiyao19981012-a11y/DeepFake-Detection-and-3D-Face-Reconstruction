#!/usr/bin/env python3
"""
一键启动脚本 — 同时启动后端（FastAPI）和前端（Vite dev server）。
用法：python3 start.py
Ctrl+C 优雅关闭两个服务。
"""
from __future__ import annotations

import os
import sys
import time
import signal
import subprocess
import threading
import platform
from pathlib import Path

# ──────────────────────────────────────────────
#  项目根目录（脚本所在目录）
# ──────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent
BACKEND_DIR = PROJECT_ROOT / "backend"
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# ──────────────────────────────────────────────
#  颜色输出
# ──────────────────────────────────────────────
class Color:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

def log_info(msg: str) -> None:
    print(f"{Color.CYAN}[INFO]{Color.RESET} {msg}")

def log_ok(msg: str) -> None:
    print(f"{Color.GREEN}[ OK ]{Color.RESET} {msg}")

def log_warn(msg: str) -> None:
    print(f"{Color.YELLOW}[WARN]{Color.RESET} {msg}")

def log_err(msg: str) -> None:
    print(f"{Color.RED}[ERR ]{Color.RESET} {msg}")

# ──────────────────────────────────────────────
#  子进程管理
# ──────────────────────────────────────────────
_processes: list[subprocess.Popen] = []

def run_in_thread(cmd: list[str], cwd: Path, name: str) -> None:
    """在子线程中启动一个子进程并实时打印输出。"""
    try:
        env = os.environ.copy()
        # Force unbuffered output
        env["PYTHONUNBUFFERED"] = "1"
        proc = subprocess.Popen(
            cmd,
            cwd=str(cwd),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        _processes.append(proc)
        for line in iter(proc.stdout.readline, ""):
            if line:
                print(f"{Color.BOLD}[{name}]{Color.RESET} {line}", end="")
        proc.wait()
        if proc.returncode != 0 and proc.returncode != -15:  # -15 = SIGTERM
            log_err(f"{name} 异常退出 (code={proc.returncode})")
    except Exception as e:
        log_err(f"{name} 启动失败: {e}")

def cleanup(signum=None, frame=None) -> None:
    """SIGINT / SIGTERM 处理，关闭所有子进程。"""
    print()
    log_warn("正在关闭所有服务...")
    for proc in _processes:
        if proc.poll() is None:
            proc.terminate()
    # 等 2 秒再强制 kill
    time.sleep(2)
    for proc in _processes:
        if proc.poll() is None:
            proc.kill()
    log_ok("所有服务已关闭。")
    sys.exit(0)

# ──────────────────────────────────────────────
#  环境检查
# ──────────────────────────────────────────────
def check_prerequisites() -> bool:
    """检查 Python / Node / npm 是否可用。"""
    ok = True

    # Python
    try:
        ver = sys.version_info
        log_ok(f"Python {ver.major}.{ver.minor}.{ver.micro}")
    except Exception:
        log_err("Python 未安装或不可用")
        ok = False

    # Node
    try:
        r = subprocess.run(["node", "--version"], capture_output=True, text=True, timeout=5)
        log_ok(f"Node {r.stdout.strip()}")
    except FileNotFoundError:
        log_err("Node.js 未安装，请先安装 https://nodejs.org")
        ok = False

    # npm
    try:
        r = subprocess.run(["npm", "--version"], capture_output=True, text=True, timeout=5)
        log_ok(f"npm {r.stdout.strip()}")
    except FileNotFoundError:
        log_err("npm 未安装")
        ok = False

    return ok

# ──────────────────────────────────────────────
#  Python 依赖安装
# ──────────────────────────────────────────────
def install_python_deps() -> bool:
    """安装 requirements.txt 中的依赖。"""
    req_file = BACKEND_DIR / "requirements.txt"
    if not req_file.exists():
        log_err(f"未找到 {req_file}")
        return False

    log_info("检查 Python 依赖...")
    try:
        # 快速检查 torch 是否已安装
        import torch  # noqa: F401
        import fastapi  # noqa: F401
        log_ok("Python 核心依赖已安装")
        return True
    except ImportError:
        log_info("安装 Python 依赖 (pip install -r requirements.txt)...")
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "-r", str(req_file)],
                cwd=str(PROJECT_ROOT),
                check=True,
            )
            log_ok("Python 依赖安装完成")
            return True
        except subprocess.CalledProcessError:
            log_err("Python 依赖安装失败，请手动执行:")
            log_err(f"  pip install -r {req_file}")
            return False

# ──────────────────────────────────────────────
#  前端依赖安装
# ──────────────────────────────────────────────
def install_frontend_deps() -> bool:
    """npm install。"""
    node_modules = FRONTEND_DIR / "node_modules"
    if node_modules.exists() and any(node_modules.iterdir()):
        log_ok("前端 node_modules 已存在，跳过安装")
        return True

    log_info("安装前端依赖 (npm install)...")
    try:
        subprocess.run(["npm", "install"], cwd=str(FRONTEND_DIR), check=True)
        log_ok("前端依赖安装完成")
        return True
    except subprocess.CalledProcessError:
        log_err("npm install 失败，请手动执行:")
        log_err(f"  cd {FRONTEND_DIR} && npm install")
        return False

# ──────────────────────────────────────────────
#  确保目录存在
# ──────────────────────────────────────────────
def ensure_dirs() -> None:
    """创建必要的目录。"""
    dirs = [
        BACKEND_DIR / "static" / "uploads",
        BACKEND_DIR / "static" / "output_img",
        BACKEND_DIR / "static" / "3d_model",
        PROJECT_ROOT / "data" / "samples",
        PROJECT_ROOT / "data" / "reports",
    ]
    for d in dirs:
        if d.is_file():
            d.unlink()  # 删除同名文件
        d.mkdir(parents=True, exist_ok=True)
    log_ok("目录结构已就绪")

# ──────────────────────────────────────────────
#  启动服务
# ──────────────────────────────────────────────
def start_services() -> None:
    """启动后端 + 前端。"""
    print()
    print(f"{Color.BOLD}{Color.GREEN}{'='*60}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GREEN}  Biometric 3D Vulnerability Detection System{Color.RESET}")
    print(f"{Color.BOLD}{Color.GREEN}  一键启动 — 后端 FastAPI + 前端 Vite{Color.RESET}")
    print(f"{Color.BOLD}{Color.GREEN}{'='*60}{Color.RESET}")
    print()

    # 后端命令
    backend_cmd = [
        sys.executable, "-m", "uvicorn",
        "backend.main:app",
        "--host", "127.0.0.1",
        "--port", "8000",
        "--reload",
    ]

    # 前端命令
    frontend_cmd = ["npm", "run", "dev"]

    log_info("启动后端 (FastAPI) → http://127.0.0.1:8000")
    log_info("API 文档 → http://127.0.0.1:8000/docs")
    backend_thread = threading.Thread(
        target=run_in_thread,
        args=(backend_cmd, PROJECT_ROOT, "Backend"),
        daemon=True,
    )
    backend_thread.start()

    # 等后端先启动一会儿
    time.sleep(2)

    log_info("启动前端 (Vite) → http://localhost:3000")
    frontend_thread = threading.Thread(
        target=run_in_thread,
        args=(frontend_cmd, FRONTEND_DIR, "Frontend"),
        daemon=True,
    )
    frontend_thread.start()

    print()
    log_ok("服务启动中，请稍候...")
    print(f"{Color.BOLD}  前端页面: {Color.GREEN}http://localhost:3000{Color.RESET}")
    print(f"{Color.BOLD}  API 文档: {Color.GREEN}http://127.0.0.1:8000/docs{Color.RESET}")
    print(f"{Color.BOLD}  按 Ctrl+C 关闭所有服务{Color.RESET}")
    print()

    # 主线程挂起，等待子线程
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()

# ──────────────────────────────────────────────
#  Main
# ──────────────────────────────────────────────
def main() -> None:
    # 注册信号处理
    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    print(f"{Color.BOLD}检查运行环境...{Color.RESET}")
    if not check_prerequisites():
        sys.exit(1)

    if not install_python_deps():
        sys.exit(1)

    if not install_frontend_deps():
        sys.exit(1)

    ensure_dirs()

    start_services()

if __name__ == "__main__":
    main()
