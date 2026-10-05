# README.md DeepFake 检测 + 人脸3D重建项目
# DeepFake Detection and 3D Face Reconstruction
## 项目简介
本项目实现 **DeepFake伪造人脸检测** 以及 **人脸三维模型重建**。
利用图像输入，完成伪造人脸判别；同时对二维人脸图像进行3D人脸模型重建，得到人脸三维几何与纹理信息。

> 应用场景：数字图像真伪鉴别、多媒体取证、人脸三维建模。

### 主要功能
1. **DeepFake 伪造人脸检测**
- 对输入图片/人脸截图进行检测，判断图像是否为DeepFake生成伪造人脸；
- 输出伪造置信分数，区分真实人脸与AI换脸、AI生成虚假人脸；
- 支持批量图片推理。

2. **2D图像转3D人脸重建**
- 从单张二维人脸图像重建三维人脸模型；
- 输出人脸三维网格(vertices顶点、faces面片)；
- 可导出3D模型文件（obj格式），支持可视化渲染查看人脸三维形态；
- 获取人脸姿态、纹理、面部关键点信息。

3. **可视化模块**
- 检测结果可视化，标记伪造概率；
- 3D人脸网格可视化展示；
- 结果保存至本地。

## 技术栈
- Python
- PyTorch：深度学习模型推理
- OpenCV：人脸检测、图像预处理
- NumPy：矩阵运算
- Matplotlib / Mayavi：3D可视化
- MediaPipe：人脸关键点定位

## 环境依赖
```bash
pip install -r requirements.txt
```

主要依赖库：
```
torch
opencv-python
numpy
matplotlib
mediapipe
mayavi
scipy
```


> 说明：
> - `weights/` 预训练模型权重文件体积较大，不上传Git仓库，使用者自行下载放置到此文件夹；
> - `output/` 文件夹程序运行自动生成，保存检测结果与重建得到的3D人脸obj模型。

## 运行方式
### 1. 执行完整流程（DeepFake检测 + 3D人脸重建）
```bash
python main.py --image ./input_images/test_face.jpg
```

### 参数说明
`--image`：输入人脸图片路径

程序输出：
1. DeepFake伪造置信得分（score，越接近1代表伪造可能性越高）
2. 绘制检测结果图片保存至`output/`
3. 重建人脸3D模型，导出 `face_model.obj` 三维模型文件

## 实验说明
1. DeepFake检测模型：输入裁剪后的人脸区域，提取伪造特征，输出二分类置信度；
2. 单图像3D人脸重建：由2D人脸图像回归人脸三维顶点坐标，生成三角面片网格；
3. 输出obj文件可以使用MeshLab等三维软件打开查看人脸模型。

## 注意事项
1. 预训练权重需要自行下载，不存放在本仓库；
2. 输入图像建议包含清晰正脸，侧脸过大将降低3D重建和检测精度；
3. output文件夹运行时自动创建，不需要手动新建。
```

## 配套 requirements.txt
```txt
torch
opencv-python
numpy
matplotlib
mediapipe
mayavi
scipy
pillow
```
