<template>
  <div class="home-page">
    <!-- ===== HERO SECTION ===== -->
    <section class="hero">
      <video
        ref="bgVideo"
        class="hero-video"
        muted loop playsinline autoplay preload="auto"
      >
        <source src="/assets/4.mp4" type="video/mp4" />
      </video>
      <div class="hero-line"></div>

      <div class="hero-overlay">
        <div class="hero-content">
          <p class="hero-eyebrow">
            Facial Biometric Authentication Vulnerability Detection
          </p>
          <h1 class="hero-title">
            Detect Deepfake Attacks<span class="cn-green">.</span>
          </h1>
          <p class="hero-desc">
            Advanced vulnerability detection platform for facial model and ocular biometric authentication systems. Identify and mitigate deepfake threats in real-time.
          </p>
          <div class="hero-buttons">
            <a href="#features" class="btn-primary">
              Get Started
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
            </a>
            <button class="btn-outline" @click="showLearnMore = true">Learn More</button>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== TECH MARQUEE ===== -->
    <section class="marquee-section">
      <div class="marquee-track marquee-left">
        <div class="marquee-inner">
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>PyTorch</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>YOLOv8</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>ResNet50</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/></svg>FastAPI</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="7.5 4.21 12 6.81 16.5 4.21"/><polyline points="7.5 19.79 7.5 14.6 3 12"/><polyline points="21 12 16.5 14.6 16.5 19.79"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>Three.js</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>MPS</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="3"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>OpenCV</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>SQLite</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M14.31 8l5.74 9.94"/><path d="M9.69 8h11.48"/><path d="M7.38 12l5.74-9.94"/><path d="M9.69 16L3.95 6.06"/><path d="M14.31 16H2.83"/><path d="M16.62 12l-5.74 9.94"/></svg>ECharts</span>
          <!-- duplicated for seamless loop -->
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>PyTorch</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="3"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>YOLOv8</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>ResNet50</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/></svg>FastAPI</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="7.5 4.21 12 6.81 16.5 4.21"/><polyline points="7.5 19.79 7.5 14.6 3 12"/><polyline points="21 12 16.5 14.6 16.5 19.79"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>Three.js</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>MPS</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="3"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>OpenCV</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>SQLite</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M14.31 8l5.74 9.94"/><path d="M9.69 8h11.48"/><path d="M7.38 12l5.74-9.94"/><path d="M9.69 16L3.95 6.06"/><path d="M14.31 16H2.83"/><path d="M16.62 12l-5.74 9.94"/></svg>ECharts</span>
        </div>
      </div>
      <div class="marquee-track marquee-right">
        <div class="marquee-inner">
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>Vue 3</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>Vite</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10"/><path d="M12 2a15.3 15.3 0 0 0-4 10 15.3 15.3 0 0 0 4 10"/></svg>Deep3DFaceRecon</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>FaceForensics++</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>DFDC</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>Apple M2 Max</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>Element Plus</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Pinia</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10"/><path d="M12 2a15.3 15.3 0 0 0-4 10 15.3 15.3 0 0 0 4 10"/></svg>GAN</span>
          <!-- duplicated for seamless loop -->
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>Vue 3</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>Vite</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10"/><path d="M12 2a15.3 15.3 0 0 0-4 10 15.3 15.3 0 0 0 4 10"/></svg>Deep3DFaceRecon</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>FaceForensics++</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>DFDC</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>Apple M2 Max</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>Element Plus</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Pinia</span>
          <span class="tech-badge"><svg viewBox="0 0 24 24" class="badge-icon" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10"/><path d="M12 2a15.3 15.3 0 0 0-4 10 15.3 15.3 0 0 0 4 10"/></svg>GAN</span>
        </div>
      </div>
    </section>

    <!-- ===== GALLERY 1: GPU ACCELERATION ===== -->
    <section class="gallery">
      <div class="gallery-wrapper">
        <!-- Left: Text content -->
        <div class="gallery-info">
          <p class="gallery-label">DEVICE &amp; INFERENCE</p>
          <h2 class="gallery-title">MPS-accelerated dual-model pipeline<span class="cn-green">.</span></h2>
          <p class="gallery-subtitle">
            The entire detection stack runs locally on Apple M2 Max via PyTorch MPS. YOLOv8‑nano handles face localization at 640×640 input, then ResNet50 classifies each detected face into real, 2D‑deepfake, or 3D‑synthetic — all within a single FastAPI backend with zero cloud dependency.
          </p>

          <div class="gallery-divider"></div>

          <div class="gallery-spec-section">
            <h4 class="gallery-spec-heading">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#5ed29c" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
              Stage 1 · YOLOv8‑nano Face Detector
            </h4>
            <p class="gallery-spec-text">
              <code>yolo_wrapper.py</code> wraps Ultralytics YOLOv8, loading <code>yolov8n.pt</code> onto MPS at startup. The <code>detect()</code> method runs inference with conf=0.35 and iou=0.45 thresholds, returning bounding boxes for every detected face. A helper <code>crop_face()</code> extracts each region for the downstream classifier. The entire module is a thin singleton wrapper — loaded once, reused across all API requests.
            </p>
            <div class="gallery-spec-meta">
              <span class="gallery-meta-item"><span class="cn-green">3.2M</span> params</span>
              <span class="gallery-meta-item"><span class="cn-green">640×640</span> input</span>
              <span class="gallery-meta-item"><span class="cn-green">conf=0.35</span> threshold</span>
              <span class="gallery-meta-item"><span class="cn-green">MPS</span> backend</span>
            </div>
          </div>

          <div class="gallery-spec-section">
            <h4 class="gallery-spec-heading">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#5ed29c" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              Stage 2 · ResNet50 Authenticity Classifier
            </h4>
            <p class="gallery-spec-text">
              <code>resnet_wrapper.py</code> defines a custom <code>ResNet50Classifier</code> with a 3‑class head: real / 2d_deepfake / 3d_synthetic. Weights from <code>best_model.pth</code> are loaded via <code>load_state_dict()</code> with DataParallel prefix stripping. The <code>classify()</code> method preprocesses face crops with ImageNet normalization, runs a single forward pass on MPS, and returns per‑class probabilities plus a combined <code>fake_score</code>.
            </p>
            <div class="gallery-spec-meta">
              <span class="gallery-meta-item"><span class="cn-green">25.6M</span> params</span>
              <span class="gallery-meta-item"><span class="cn-green">3‑class</span> output</span>
              <span class="gallery-meta-item"><span class="cn-green">224×224</span> input</span>
              <span class="gallery-meta-item"><span class="cn-green">best_model.pth</span> weights</span>
            </div>
          </div>

          <div class="gallery-spec-section">
            <h4 class="gallery-spec-heading">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#5ed29c" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
              Orchestration · detect_service.py
            </h4>
            <p class="gallery-spec-text">
              <code>DetectService</code> ties both stages together. It loads the image via <code>image_proc.py</code>, runs YOLO detection, then iterates over each face crop through ResNet classification. Results are drawn onto the original image by <code>draw_label.py</code> and saved to <code>static/output_img/</code>. The service also handles video frame‑by‑frame processing with configurable sampling intervals.
            </p>
            <div class="gallery-spec-meta">
              <span class="gallery-meta-item"><span class="cn-green">FastAPI</span> router</span>
              <span class="gallery-meta-item"><span class="cn-green">SQLite</span> storage</span>
              <span class="gallery-meta-item"><span class="cn-green">CSV</span> report export</span>
              <span class="gallery-meta-item"><span class="cn-green">3D recon</span> optional</span>
            </div>
          </div>

          <div class="gallery-footer-note">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#5ed29c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            <span>Models preloaded at FastAPI startup via <code>@app.on_event("startup")</code>. All inference runs on <code>torch.device("mps")</code> with <code>torch.no_grad()</code>.</span>
          </div>
        </div>

        <!-- Right: Two videos stacked, aligned to top -->
        <div class="gallery-videos">
          <div class="gallery-card">
            <video class="gallery-video" muted loop playsinline autoplay preload="auto">
              <source src="/assets/1.mp4" type="video/mp4" />
            </video>
          </div>
          <div class="gallery-card">
            <video class="gallery-video" muted loop playsinline autoplay preload="auto">
              <source src="/assets/2.mp4" type="video/mp4" />
            </video>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== GALLERY 2: MODEL SHOWCASE ===== -->
    <section class="model-showcase">
      <div class="ms-header">
        <p class="ms-label">MODEL ARCHITECTURE</p>
        <h2 class="ms-title">Two-stage detection pipeline<span class="cn-green">.</span></h2>
        <p class="ms-subtitle">A lightweight face detector paired with a deep residual classifier — delivering real-time deepfake identification with production-grade accuracy.</p>
      </div>

      <!-- Two model cards side-by-side -->
      <div class="ms-cards-row">
        <div class="ms-spec-group">
          <div class="ms-spec-dot"></div>
          <div class="ms-spec-body">
            <h4 class="ms-spec-name">YOLOv8<span class="cn-green">‑nano</span></h4>
            <p class="ms-spec-desc">Ultralytics YOLOv8‑nano — the lightest face detector in the YOLOv8 family, optimized for real‑time video pipelines. Built on a CSPDarknet53 backbone with a decoupled detection head, it delivers exceptional speed without sacrificing localization precision.</p>
            <ul class="ms-spec-list">
              <li>Params <span class="cn-green">3.2M</span></li>
              <li>mAP@50 <span class="cn-green">37.3</span></li>
              <li>Inference <span class="cn-green">~1.2ms / frame</span></li>
              <li>Input <span class="cn-green">640×640</span></li>
              <li>FLOPs <span class="cn-green">8.7G</span></li>
              <li>Backbone <span class="cn-green">CSPDarknet53</span></li>
              <li>Framework <span class="cn-green">PyTorch + Ultralytics</span></li>
              <li>Pre‑trained <span class="cn-green">COCO + WIDER Face</span></li>
            </ul>
          </div>
        </div>

        <div class="ms-spec-group">
          <div class="ms-spec-dot"></div>
          <div class="ms-spec-body">
            <h4 class="ms-spec-name">ResNet<span class="cn-green">50</span></h4>
            <p class="ms-spec-desc">ResNet50 binary classifier trained on FaceForensics++ &amp; DFDC. Residual bottleneck blocks capture subtle deepfake artifacts invisible to the human eye — including blending boundaries, inconsistent specular highlights, and unnatural texture frequencies in GAN‑generated faces.</p>
            <ul class="ms-spec-list">
              <li>Params <span class="cn-green">25.6M</span></li>
              <li>Accuracy <span class="cn-green">94.7% (FF++)</span></li>
              <li>Layers <span class="cn-green">50 Bottleneck</span></li>
              <li>Input <span class="cn-green">224×224</span></li>
              <li>FLOPs <span class="cn-green">4.1G</span></li>
              <li>Dataset <span class="cn-green">FF++ + DFDC</span></li>
              <li>Optimizer <span class="cn-green">AdamW (lr=1e‑4)</span></li>
              <li>Augmentation <span class="cn-green">RandomErase + MixUp</span></li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Bottom: Data visualization -->
      <div class="ms-chart-row">
        <!-- Card 1: Inference Speed Bar Chart -->
        <div class="ms-chart-card">
          <div class="ms-chart-header">
            <span class="ms-chart-icon">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#5ed29c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
            </span>
            <h4 class="ms-chart-title">Inference Latency<span class="cn-green">.</span></h4>
          </div>
          <p class="ms-chart-desc">Per-frame processing time across hardware backends — lower is better.</p>
          <div class="ms-chart">
            <div class="ms-bar-wrap">
              <span class="ms-bar-label">CPU Baseline</span>
              <div class="ms-bar-track"><div class="ms-bar-fill" style="width: 18%"><span class="ms-bar-val">45.2 ms</span></div></div>
            </div>
            <div class="ms-bar-wrap">
              <span class="ms-bar-label">Apple M2 Ultra</span>
              <div class="ms-bar-track"><div class="ms-bar-fill" style="width: 35%"><span class="ms-bar-val">12.0 ms</span></div></div>
            </div>
            <div class="ms-bar-wrap">
              <span class="ms-bar-label">NVIDIA A100</span>
              <div class="ms-bar-track"><div class="ms-bar-fill" style="width: 62%"><span class="ms-bar-val">2.8 ms</span></div></div>
            </div>
            <div class="ms-bar-wrap">
              <span class="ms-bar-label">NVIDIA H100</span>
              <div class="ms-bar-track"><div class="ms-bar-fill" style="width: 88%"><span class="ms-bar-val">1.2 ms</span></div></div>
            </div>
            <div class="ms-bar-wrap">
              <span class="ms-bar-label">NVIDIA H100 · TensorRT</span>
              <div class="ms-bar-track"><div class="ms-bar-fill ms-bar-best" style="width: 100%"><span class="ms-bar-val">0.8 ms</span></div></div>
            </div>
          </div>
          <div class="ms-chart-footer">
            <span class="ms-speed-badge">Up to <span class="cn-green">56×</span> faster than CPU</span>
          </div>
        </div>


      </div>
    </section>

    <!-- ===== FEATURES (light green section) ===== -->
    <section id="features" class="features-light">
      <p class="fl-label">CAPABILITIES</p>
      <h2 class="fl-title">Explore the detection platform.</h2>

      <div class="fl-grid">
        <div v-for="f in features" :key="f.id" class="fl-item">
          <!-- Feature card slot — reuse existing square card -->
          <router-link :to="f.link" class="feature-card">
            <div class="feature-bg">
              <img :src="f.bg" :alt="f.title" class="feature-bg-img" />
            </div>
            <div class="feature-overlay">
              <div class="feature-tag">{{ f.tag }}</div>
              <h3 class="feature-card-title">{{ f.title }}</h3>
              <p class="feature-card-desc">{{ f.desc }}</p>
              <span class="feature-arrow">&rarr;</span>
            </div>
          </router-link>
          <!-- Text below the card -->
          <h3 class="fl-item-title">{{ f.subtitle }}</h3>
          <p class="fl-item-desc">{{ f.subdesc }}</p>
        </div>
      </div>
    </section>

    <!-- ===== DYNAMIC WORD CARD ===== -->
    <section class="dynamic-word-section">
      <div class="dw-card">
        <div class="dw-icon-ring">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#5ed29c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 6v6l4 2"/>
          </svg>
        </div>
        <p class="dw-label">VULNERABILITY RESEARCH</p>
        <h2 class="dw-title" :class="{ 'dw-animating': isSwapping }">
          <span class="dw-word-a dw-side-word">Building</span>
          <span class="dw-word-b dw-core-word" :style="{ minWidth: coreWidth }">
            <span class="dw-core-inner dw-core-current" :key="'c-' + currentIdx">{{ words[currentIdx] }}</span>
            <span class="dw-core-inner dw-core-next" :key="'n-' + nextIdx">{{ words[nextIdx] }}</span>
          </span>
          <span class="dw-word-c dw-side-word">Authentication</span>
        </h2>
        <p class="dw-subtitle">Biometric systems deserve proactive defense against the next generation of deepfake attacks.</p>
      </div>
    </section>

    <!-- ===== FOOTER ===== -->
    <footer class="footer">
      <div class="footer-inner">
        <p class="footer-copy">&copy; 2025 Biometric 3D Vulnerability Research. All rights reserved.</p>
        <div class="footer-links">
        </div>
      </div>
    </footer>

    <!-- ===== LEARN MORE MODAL ===== -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="showLearnMore" class="modal-backdrop" @click.self="showLearnMore = false">
          <div class="modal-panel">
            <button class="modal-close" @click="showLearnMore = false">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>

            <div class="modal-scroll">
              <p class="modal-eyebrow">ABOUT THIS PROJECT</p>
              <h2 class="modal-heading">Biometric 3D Vulnerability<span class="cn-green">.</span></h2>
              <p class="modal-subtitle">
                An advanced research platform for detecting deepfake attacks against facial and ocular biometric authentication systems — combining cutting-edge computer vision with real-time vulnerability assessment.
              </p>

              <hr class="modal-divider" />

              <h3 class="modal-section-title">🤖 Models</h3>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">YOLOv8</span> — Face Detection
                </h4>
                <p class="modal-card-body">
                  Ultralytics YOLOv8 is employed as the primary face detector. It locates facial regions in both images and video frames with high precision and real-time performance, serving as the first stage of our detection pipeline.
                </p>
              </div>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">ResNet50</span> — Deepfake Classification
                </h4>
                <p class="modal-card-body">
                  A ResNet50 binary classifier trained on FaceForensics++ and DFDC datasets distinguishes real faces from AI-generated fakes. The model outputs a confidence score and binary verdict for every detected face.
                </p>
              </div>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">Deep3DFaceRecon</span> — 3D Reconstruction
                </h4>
                <p class="modal-card-body">
                  Genuine faces are passed through Deep3DFaceRecon to generate OBJ-format 3D mesh models. Fake faces are blocked from reconstruction, providing an additional layer of biometric integrity verification.
                </p>
              </div>

              <hr class="modal-divider" />

              <h3 class="modal-section-title">⚙️ Backend Architecture</h3>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">FastAPI</span> + SQLAlchemy + SQLite
                </h4>
                <p class="modal-card-body">
                  The backend is built with <span class="cn-green">FastAPI</span> for high-performance async REST APIs, <span class="cn-green">SQLAlchemy</span> as the ORM layer, and <span class="cn-green">SQLite</span> for lightweight persistent storage. All detection tasks, file uploads, and report generation are served through clean RESTful endpoints.
                </p>
              </div>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">PyTorch</span> with MPS Acceleration
                </h4>
                <p class="modal-card-body">
                  Models run on <span class="cn-green">PyTorch</span> with automatic device selection — CUDA for NVIDIA GPUs, <span class="cn-green">MPS</span> for Apple Silicon, and CPU fallback. This ensures optimal inference speed across all hardware platforms.
                </p>
              </div>

              <hr class="modal-divider" />

              <h3 class="modal-section-title">🎨 Frontend &amp; Design</h3>

              <p class="modal-card-body">
                The frontend is a modern <span class="cn-green">Vue 3</span> SPA powered by <span class="cn-green">Vite</span>, with <span class="cn-green">Element Plus</span> UI components, <span class="cn-green">Pinia</span> state management, and <span class="cn-green">ECharts</span> for data visualization. The visual identity draws inspiration from industry-leading design platforms:
              </p>

              <div class="modal-links">
                <a href="https://motionsites.ai/" target="_blank" rel="noopener" class="modal-link-item">
                  <span class="modal-link-icon">↗</span>
                  <div>
                    <strong>MotionSites</strong>
                    <span>motionsites.ai</span>
                  </div>
                </a>
                <a href="https://modal.com/" target="_blank" rel="noopener" class="modal-link-item">
                  <span class="modal-link-icon">↗</span>
                  <div>
                    <strong>Modal</strong>
                    <span>modal.com</span>
                  </div>
                </a>
                <a href="https://neon.com/" target="_blank" rel="noopener" class="modal-link-item">
                  <span class="modal-link-icon">↗</span>
                  <div>
                    <strong>Neon</strong>
                    <span>neon.com</span>
                  </div>
                </a>
              </div>

              <hr class="modal-divider" />

              <h3 class="modal-section-title">📖 How to Use</h3>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">Step 1</span> — Single Image Detection
                </h4>
                <p class="modal-card-body">
                  Navigate to <span class="cn-green">/detect</span> and upload a single image. YOLOv8 will detect all faces, and ResNet50 will classify each as Real or Fake. Results are annotated directly on the image with bounding boxes and confidence scores.
                </p>
              </div>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">Step 2</span> — Batch Video Analysis
                </h4>
                <p class="modal-card-body">
                  Go to <span class="cn-green">/batch</span> and upload one or more video files. The system processes every frame, calculates per-frame risk scores, generates annotated output videos, and exports detailed CSV reports with frame-level statistics.
                </p>
              </div>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">Step 3</span> — 3D Face Reconstruction
                </h4>
                <p class="modal-card-body">
                  Visit <span class="cn-green">/verify</span> to generate 3D face models. Only images classified as Real are eligible for 3D reconstruction. Download the resulting OBJ model for further analysis or integration.
                </p>
              </div>

              <div class="modal-card">
                <h4 class="modal-card-head">
                  <span class="cn-green">Step 4</span> — Vulnerability Reports
                </h4>
                <p class="modal-card-body">
                  After completing any detection task, comprehensive reports are automatically generated. View fake ratios, average risk scores, and interactive ECharts risk distribution charts. All reports are exportable in CSV format for offline analysis.
                </p>
              </div>

              <hr class="modal-divider" />

              <div class="modal-footer-note">
                <p>Built with ❤️ by the Biometric 3D Vulnerability Research team.</p>
                <p class="modal-footer-sub">Powered by PyTorch · FastAPI · Vue 3 · Vite</p>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'


const bgVideo = ref(null)
const showLearnMore = ref(false)

// ── Dynamic word animation ──
const words = ['Fast', 'Safe', 'Smart']
const currentIdx = ref(0)
const nextIdx = ref(1)
const isSwapping = ref(false)
const coreWidth = ref('0px')
let wordTimer = null

function measureWidth() {
  // 用离屏 canvas 测量最宽单词的实际宽度
  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')
  const el = document.querySelector('.dw-title')
  if (!el || !ctx) return
  const style = window.getComputedStyle(el)
  ctx.font = `${style.fontWeight} ${style.fontSize} ${style.fontFamily}`
  let maxW = 0
  words.forEach(w => {
    const m = ctx.measureText(w)
    if (m.width > maxW) maxW = m.width
  })
  coreWidth.value = Math.ceil(maxW + 4) + 'px'
}

function cycleWord() {
  isSwapping.value = true
  setTimeout(() => {
    const next = (nextIdx.value + 1) % words.length
    currentIdx.value = nextIdx.value
    nextIdx.value = next
    isSwapping.value = false
  }, 850)
}

onMounted(() => {
  if (bgVideo.value) bgVideo.value.play().catch(() => {})
  measureWidth()
  wordTimer = setInterval(cycleWord, 3500)
})

onUnmounted(() => {
  if (wordTimer) clearInterval(wordTimer)
})

const features = [
  {
    id: 1,
    tag: 'Image Detection',
    bg: '/assets/feature-01.png',
    title: 'Single Image Detection',
    desc: 'Upload a single image for real-time YOLOv8 face detection + ResNet50 authenticity classification with annotated results.',
    subtitle: 'Real-time inference',
    subdesc: 'YOLOv8-nano locates faces at 640×640, ResNet50 classifies real vs. fake in a single forward pass on MPS.',
    link: '/detect',
  },
  {
    id: 2,
    tag: 'Video Analysis',
    bg: '/assets/feature-02.png',
    title: 'Batch Video Analysis',
    desc: 'Upload videos for frame-by-frame deepfake detection. Get per-frame risk scores, annotated output video, and CSV reports.',
    subtitle: 'Frame-by-frame pipeline',
    subdesc: 'Configurable sampling interval, per-frame bbox annotation, and statistical aggregation across the full clip.',
    link: '/batch',
  },
  {
    id: 3,
    tag: '3D Reconstruction',
    bg: '/assets/feature-03.png',
    title: '3D Face Reconstruction',
    desc: 'Generate OBJ 3D face models from real faces using Deep3DFaceRecon. Fake faces are blocked from reconstruction.',
    subtitle: 'Geometry verification',
    subdesc: 'Only genuine faces pass through Deep3DFaceRecon — synthetic inputs are rejected to preserve output fidelity.',
    link: '/verify',
  },
  {
    id: 4,
    tag: 'Sample Library',
    bg: '/assets/feature-04.png',
    title: 'Sample Library',
    desc: 'Browse and manage the deepfake sample database. Explore real vs. synthetic face datasets used for model training and validation.',
    subtitle: 'Dataset management',
    subdesc: 'Centralized sample repository with metadata tagging, authenticity labels, and quick access to training data subsets.',
    link: '/samples',
  },

]
</script>

<style scoped>
/* ── Hero ── */
.hero {
  position: relative;
  width: 100%;
  border: 1px solid rgba(255,255,255,0.12);
  border-top: none;
}
.hero-video {
  width: 100%;
  max-height: 70vh;
  object-fit: cover;
  display: block;
}
.hero-line {
  width: 100%;
  border-top: 1px solid rgba(255,255,255,0.12);
}
.hero-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  padding: 0 48px 24px 48px;
}
.hero-content {
  max-width: 720px;
}
.hero-eyebrow {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #5ed29c;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.eyebrow-icon { flex-shrink: 0; }
.hero-title {
  font-weight: 800;
  text-transform: uppercase;
  line-height: 0.95;
  font-size: clamp(36px, 6vw, 72px);
  margin-bottom: 12px;
  max-width: 800px;
}
.hero-desc {
  font-size: 14px;
  color: rgba(255,255,255,0.65);
  max-width: 480px;
  line-height: 1.6;
  margin-bottom: 20px;
}
.hero-buttons {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
}
.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 28px;
  border-radius: 999px;
  background: #5ed29c;
  color: #070b0a;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  transition: all 0.3s;
}
.btn-primary:hover {
  gap: 16px;
  padding-right: 36px;
  background: #4cc08a;
}
.btn-primary:hover svg {
  transform: translateX(6px);
}
.btn-primary svg {
  transition: transform 0.3s;
}
.btn-outline {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 28px;
  border-radius: 999px;
  border: 2px solid rgba(94, 210, 156, 0.5);
  color: #5ed29c;
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  transition: all 0.3s;
  background: transparent;
  cursor: pointer;
}
.btn-outline:hover {
  border-color: #5ed29c;
  background: rgba(94, 210, 156, 0.1);
}

/* ── Marquee ── */
.marquee-section {
  padding: 24px 0;
  overflow: hidden;
  border-bottom: 1px solid rgba(255,255,255,0.06);
  background: linear-gradient(180deg, rgba(94,210,156,0.015) 0%, transparent 100%);
}
.marquee-track { overflow: hidden; white-space: nowrap; }
.marquee-left .marquee-inner {
  display: flex;
  animation: marqueeLeft 32s linear infinite;
}
.marquee-right .marquee-inner {
  display: flex;
  animation: marqueeRight 32s linear infinite;
  margin-top: 12px;
}
@keyframes marqueeLeft {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
@keyframes marqueeRight {
  0%   { transform: translateX(-50%); }
  100% { transform: translateX(0); }
}
.tech-badge {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.28);
  white-space: nowrap;
  padding: 7px 18px;
  margin: 0 7px;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 999px;
  background: rgba(255,255,255,0.015);
  transition: color 0.35s, border-color 0.35s, background 0.35s, box-shadow 0.35s;
  user-select: none;
  cursor: default;
}
.tech-badge:hover {
  color: #fff;
  border-color: rgba(94,210,156,0.3);
  background: rgba(94,210,156,0.06);
  box-shadow: 0 0 12px rgba(94,210,156,0.08);
}
.badge-icon {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
  opacity: 0.45;
  transition: opacity 0.35s;
}
.tech-badge:hover .badge-icon {
  opacity: 0.85;
}
.marquee-track:hover .marquee-inner { animation-play-state: paused; }

/* ── Gallery ── */
.gallery {
  padding: 60px 64px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}
.gallery-wrapper {
  display: grid;
  grid-template-columns: 1fr 0.5fr;
  gap: 48px;
  align-items: stretch;
}

/* Left info column */
.gallery-info {
  display: flex;
  flex-direction: column;
}
.gallery-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #5ed29c;
  margin: 0 0 12px 0;
}
.gallery-title {
  font-size: 30px;
  font-weight: 800;
  text-transform: uppercase;
  color: #fff;
  margin: 0 0 14px 0;
  line-height: 1.1;
}
.gallery-subtitle {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.45);
  line-height: 1.65;
  margin: 0;
}

.gallery-divider {
  border: none;
  border-top: 1px solid rgba(94, 210, 156, 0.1);
  margin: 22px 0;
}

.gallery-spec-section {
  margin-bottom: 16px;
}
.gallery-spec-heading {
  font-size: 13px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 8px 0;
  display: flex;
  align-items: center;
  gap: 8px;
}
.gallery-spec-heading svg {
  flex-shrink: 0;
}
.gallery-spec-text {
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.4);
  line-height: 1.6;
  margin: 0 0 10px 0;
}
.gallery-spec-text code {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 11px;
  color: #5ed29c;
  background: rgba(94, 210, 156, 0.08);
  padding: 1px 5px;
  border-radius: 3px;
}
.gallery-spec-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 10px;
}
.gallery-meta-item {
  font-size: 10.5px;
  color: rgba(255, 255, 255, 0.38);
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 600;
  letter-spacing: 0.04em;
  padding: 4px 10px;
  border: 1px solid rgba(94, 210, 156, 0.1);
  border-radius: 5px;
  background: rgba(94, 210, 156, 0.025);
  transition: border-color 0.3s, background 0.3s;
}
.gallery-meta-item:hover {
  border-color: rgba(94, 210, 156, 0.22);
  background: rgba(94, 210, 156, 0.05);
}
.gallery-meta-item .cn-green {
  color: #5ed29c;
  font-weight: 700;
}

.gallery-footer-note {
  margin-top: 6px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 12px 14px;
  background: rgba(94, 210, 156, 0.025);
  border: 1px solid rgba(94, 210, 156, 0.07);
  border-radius: 8px;
}
.gallery-footer-note svg {
  flex-shrink: 0;
  margin-top: 1px;
}
.gallery-footer-note span {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.3);
  line-height: 1.5;
}
.gallery-footer-note code {
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 10px;
  color: #5ed29c;
  background: rgba(94, 210, 156, 0.08);
  padding: 1px 4px;
  border-radius: 3px;
}

/* Right videos column — fills full height, compact */
.gallery-videos {
  display: flex;
  flex-direction: column;
  gap: 14px;
  height: 100%;
  justify-content: space-between;
}
.gallery-card {
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.07);
  transition: border-color 0.35s;
  aspect-ratio: 16 / 9;
  width: 100%;
}
.gallery-card:hover {
  border-color: rgba(94, 210, 156, 0.2);
}
.gallery-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s;
}
.gallery-card:hover .gallery-video {
  transform: scale(1.02);
}

/* ── Model Showcase ── */
.model-showcase {
  position: relative;
  padding: 60px 64px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  background:
    /* 左上角光晕 */
    radial-gradient(ellipse 600px 400px at 15% 20%, rgba(94, 210, 156, 0.045), transparent 60%),
    /* 右下角光晕 */
    radial-gradient(ellipse 500px 350px at 85% 75%, rgba(59, 130, 246, 0.035), transparent 60%),
    /* 中心微光 */
    radial-gradient(ellipse 400px 300px at 50% 50%, rgba(94, 210, 156, 0.02), transparent 70%),
    #070b0a;
}

/* 网格叠加层 */
.model-showcase::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background-image:
    linear-gradient(rgba(94, 210, 156, 0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(94, 210, 156, 0.025) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse 65% 65% at 50% 50%, black 35%, transparent 75%);
}

/* 确保内容在网格之上 */
.model-showcase > * {
  position: relative;
  z-index: 1;
}

.ms-header {
  margin-bottom: 36px;
}

.ms-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #5ed29c;
  margin: 0 0 12px 0;
}

.ms-title {
  font-size: 36px;
  font-weight: 800;
  text-transform: uppercase;
  color: #fff;
  margin: 0 0 14px 0;
  line-height: 1.1;
  max-width: 640px;
}

.ms-subtitle {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.45);
  line-height: 1.7;
  margin: 0;
  max-width: 680px;
}

/* Two cards side-by-side */
.ms-cards-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-bottom: 32px;
}

.ms-spec-group {
  display: flex;
  gap: 14px;
  align-items: flex-start;
  padding: 28px;
  background: rgba(94, 210, 156, 0.03);
  border: 1px solid rgba(94, 210, 156, 0.08);
  border-radius: 16px;
  transition: border-color 0.4s, background 0.4s;
}
.ms-spec-group:hover {
  border-color: rgba(94, 210, 156, 0.22);
  background: rgba(94, 210, 156, 0.05);
}

.ms-spec-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #5ed29c;
  flex-shrink: 0;
  margin-top: 8px;
  box-shadow: 0 0 10px rgba(94, 210, 156, 0.3);
}

.ms-spec-body { flex: 1; }

.ms-spec-name {
  font-size: 19px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 8px 0;
}

.ms-spec-desc {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.5);
  line-height: 1.6;
  margin: 0 0 16px 0;
}

.ms-spec-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px 20px;
}
.ms-spec-list li {
  font-size: 12.5px;
  color: rgba(255, 255, 255, 0.55);
  line-height: 1.7;
}
.ms-spec-list li .cn-green {
  color: #5ed29c;
  font-weight: 600;
}

/* Data visualization row — bar chart + dot chart */
.ms-chart-row {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

.ms-chart-card {
  background: rgba(94, 210, 156, 0.025);
  border: 1px solid rgba(94, 210, 156, 0.08);
  border-radius: 16px;
  padding: 28px 32px 24px;
  transition: border-color 0.4s, background 0.4s;
}
.ms-chart-card:hover {
  border-color: rgba(94, 210, 156, 0.2);
  background: rgba(94, 210, 156, 0.04);
}

.ms-chart-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}
.ms-chart-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 8px;
  background: rgba(94, 210, 156, 0.1);
  flex-shrink: 0;
}

.ms-chart-title {
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  margin: 0;
}

.ms-chart-desc {
  font-size: 11.5px;
  color: rgba(255, 255, 255, 0.35);
  line-height: 1.5;
  margin: 0 0 24px 0;
  padding-left: 40px;
}

/* Bar chart */
.ms-chart {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.ms-bar-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.ms-bar-label {
  font-size: 11px;
  color: rgba(255, 255, 255, 0.4);
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  flex: 0 0 140px;
  text-align: right;
}

.ms-bar-track {
  flex: 1;
  height: 24px;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  overflow: hidden;
}

.ms-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, rgba(94, 210, 156, 0.25), #5ed29c);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 12px;
  min-width: 52px;
  transition: width 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  position: relative;
}
.ms-bar-fill::after {
  content: '';
  position: absolute;
  right: 4px;
  top: 4px;
  bottom: 4px;
  width: 4px;
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.4);
}
.ms-bar-best {
  background: linear-gradient(90deg, rgba(94, 210, 156, 0.5), #5ed29c);
  box-shadow: 0 0 14px rgba(94, 210, 156, 0.3);
}
.ms-bar-best::after {
  background: rgba(255, 255, 255, 0.7);
}

.ms-bar-val {
  font-size: 11px;
  font-weight: 700;
  color: #070b0a;
  white-space: nowrap;
}

.ms-chart-footer {
  margin-top: 20px;
  padding-left: 40px;
}

.ms-speed-badge {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-weight: 600;
  letter-spacing: 0.04em;
}

@media (max-width: 900px) {
  .ms-cards-row {
    grid-template-columns: 1fr;
  }
  .model-showcase {
    padding: 48px 20px 40px;
  }
}

/* ── Features Light Section ── */
.features-light {
  background: #E6F2E0;
  padding: 60px 64px;
  font-family: 'Inter', system-ui, sans-serif;
  margin: 40px 32px;
  border-radius: 24px;
}

.fl-label {
  font-size: 13px;
  color: #555A55;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin: 0 0 12px 0;
  font-weight: 600;
}

.fl-title {
  font-size: 40px;
  font-weight: 600;
  color: #000000;
  margin: 0 0 40px 0;
  line-height: 1.1;
}

.fl-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.fl-item {
  text-align: left;
}

/* ── Feature Card — square (reused) ── */
.feature-card {
  position: relative;
  aspect-ratio: 1 / 1;
  border-radius: 16px;
  overflow: hidden;
  cursor: pointer;
  border: none;
  text-decoration: none;
  display: block;
}

.feature-bg {
  position: absolute;
  inset: -10%;
  z-index: 0;
  transform: scale(1.0);
  transition: transform 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
.feature-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.feature-card:hover .feature-bg {
  transform: scale(0.92);
}

.feature-overlay {
  position: absolute;
  inset: 0;
  z-index: 1;
  background: linear-gradient(
    180deg,
    rgba(7, 11, 10, 0.0) 0%,
    rgba(7, 11, 10, 0.35) 50%,
    rgba(7, 11, 10, 0.88) 100%
  );
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 20px;
  transition: background 0.5s;
}
.feature-card:hover .feature-overlay {
  background: linear-gradient(
    180deg,
    rgba(7, 11, 10, 0.05) 0%,
    rgba(7, 11, 10, 0.45) 50%,
    rgba(7, 11, 10, 0.94) 100%
  );
}

.feature-tag {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: #5ed29c;
  margin-bottom: 8px;
}

.feature-card-title {
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 6px 0;
  line-height: 1.25;
}

.feature-card-desc {
  font-size: 12px;
  color: rgba(255,255,255,0.55);
  line-height: 1.5;
  margin-bottom: 10px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.4s, transform 0.4s;
}
.feature-card:hover .feature-card-desc {
  opacity: 1;
  transform: translateY(0);
}

.feature-arrow {
  font-size: 18px;
  color: #5ed29c;
  opacity: 0;
  transform: translateX(-8px);
  transition: opacity 0.4s, transform 0.4s;
}
.feature-card:hover .feature-arrow {
  opacity: 1;
  transform: translateX(0);
}

/* ── Item text below card ── */
.fl-item-title {
  font-size: 20px;
  font-weight: 600;
  color: #333333;
  margin: 16px 0 6px 0;
}

.fl-item-desc {
  font-size: 13px;
  color: #667066;
  line-height: 1.5;
  margin: 0;
}

@media (max-width: 1000px) {
  .features-light {
    margin: 24px 16px;
    padding: 40px 32px;
  }
  .fl-title {
    font-size: 32px;
  }
  .fl-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 600px) {
  .features-light {
    margin: 16px 8px;
    padding: 32px 20px;
    border-radius: 16px;
  }
  .fl-title {
    font-size: 26px;
  }
  .fl-grid {
    grid-template-columns: 1fr;
  }
}/* ── Dynamic Word Card ── */
.dynamic-word-section {
  position: relative;
  margin: 40px 32px;
  min-height: 420px;
  border-radius: 24px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background:
    /* 左上角绿色大光晕 */
    radial-gradient(ellipse 500px 350px at 10% 15%, rgba(94, 210, 156, 0.06), transparent 55%),
    /* 右下角蓝色光晕 */
    radial-gradient(ellipse 400px 300px at 90% 85%, rgba(59, 130, 246, 0.04), transparent 55%),
    /* 中心上方微光 */
    radial-gradient(ellipse 300px 200px at 50% 30%, rgba(94, 210, 156, 0.03), transparent 70%),
    linear-gradient(180deg, #0a1410 0%, #0c1a14 40%, #0e1f17 70%, #0a1410 100%);
  border: 1px solid rgba(94, 210, 156, 0.1);
  transition: border-color 0.4s;
}
.dynamic-word-section:hover {
  border-color: rgba(94, 210, 156, 0.2);
}

/* ── Card Content ── */
.dw-card {
  position: relative;
  z-index: 1;
  text-align: center;
  padding: 60px 40px;
  max-width: 720px;
}

.dw-icon-ring {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 2px solid rgba(94, 210, 156, 0.2);
  background: rgba(94, 210, 156, 0.05);
  margin-bottom: 20px;
  animation: dwIconGlow 3s ease-in-out infinite;
}

@keyframes dwIconGlow {
  0%, 100% { box-shadow: 0 0 12px rgba(94, 210, 156, 0.1); }
  50%      { box-shadow: 0 0 24px rgba(94, 210, 156, 0.25); }
}

.dw-label {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #5ed29c;
  margin: 0 0 24px 0;
}

/* ── Title: three independent words ── */
.dw-title {
  font-size: clamp(28px, 5vw, 48px);
  font-weight: 800;
  text-transform: uppercase;
  color: #fff;
  margin: 0 0 16px 0;
  line-height: 1.15;
  display: flex;
  flex-wrap: nowrap;
  align-items: center;
  justify-content: center;
  gap: 0.45em;
  white-space: nowrap;
}

/* ── Side words (Building / Authentication) ── */
.dw-side-word {
  display: inline-block;
  color: rgba(255, 255, 255, 0.85);
  flex-shrink: 0;
  transition: transform 0.9s cubic-bezier(0.22, 1, 0.36, 1);
}

/* Push side words outward during animation */
.dw-title.dw-animating .dw-word-a {
  transform: translateX(-0.35em);
}
.dw-title.dw-animating .dw-word-c {
  transform: translateX(0.35em);
}

/* ── Core word container ── */
.dw-core-word {
  position: relative;
  display: inline-block;
  vertical-align: middle;
  flex-shrink: 0;
  line-height: 1;
}

.dw-core-inner {
  position: absolute;
  left: 50%;
  white-space: nowrap;
  color: #5ed29c;
  text-shadow: 0 0 28px rgba(94, 210, 156, 0.3);
  pointer-events: none;
  transform: translate(-50%, -50%);
  line-height: 1;
  will-change: top, opacity, filter;
}

/* Current core word — visible at center */
.dw-core-current {
  top: 50%;
  opacity: 1;
  filter: blur(0);
  transition:
    top    0.8s cubic-bezier(0.22, 1, 0.36, 1),
    opacity 0.65s ease,
    filter  0.65s ease;
}

/* Next core word — parked above, blurred */
.dw-core-next {
  top: -140%;
  opacity: 0;
  filter: blur(6px);
  transition:
    top    0.8s cubic-bezier(0.22, 1, 0.36, 1),
    opacity 0.65s ease,
    filter  0.65s ease;
}

/* ── ANIMATING STATE ── */
.dw-title.dw-animating .dw-core-current {
  top: 240%;
  opacity: 0;
  filter: blur(8px);
}
.dw-title.dw-animating .dw-core-next {
  top: 50%;
  opacity: 1;
  filter: blur(0);
}

.dw-subtitle {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.4);
  line-height: 1.6;
  margin: 0;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
}

@media (max-width: 768px) {
  .dynamic-word-section {
    margin: 24px 16px;
    min-height: 320px;
  }
  .dw-card {
    padding: 40px 24px;
  }
  .dw-title {
    flex-wrap: wrap;
    gap: 0.35em;
  }
  .dw-title.dw-animating .dw-word-a {
    transform: translateX(-0.25em);
  }
  .dw-title.dw-animating .dw-word-c {
    transform: translateX(0.25em);
  }
}


/* ── Footer ── */
.footer {
  padding: 32px 48px;
  border-top: 1px solid rgba(255,255,255,0.06);
}
.footer-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 16px;
}
.footer-copy {
  font-size: 12px;
  color: rgba(255,255,255,0.25);
  margin: 0;
}
.footer-links {
  display: flex;
  align-items: center;
  gap: 24px;
}
.footer-links a {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: rgba(255,255,255,0.35);
  text-decoration: none;
  transition: color 0.25s;
}
.footer-links a:hover {
  color: #5ed29c;
}

@media (max-width: 768px) {
  .gallery { padding: 40px 20px; }
  .gallery-wrapper { grid-template-columns: 1fr; gap: 28px; align-items: start; }
  .gallery-videos { flex-direction: row; gap: 12px; }
  .gallery-card { flex: 1; }
  .gallery-title { font-size: 24px; }
  .hero-overlay { padding: 0 24px 16px 24px; }
}

/* ── Learn More Modal ── */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
}

.modal-panel {
  position: relative;
  width: 100%;
  max-width: 720px;
  max-height: 85vh;
  background: #0a0f0d;
  border: 1px solid rgba(94, 210, 156, 0.15);
  border-radius: 20px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.modal-close {
  position: absolute;
  top: 16px;
  right: 16px;
  z-index: 10;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  color: #fff;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.25s;
}
.modal-close:hover {
  border-color: rgba(94, 210, 156, 0.4);
  background: rgba(94, 210, 156, 0.08);
}

.modal-scroll {
  overflow-y: auto;
  padding: 48px 40px 40px;
  flex: 1;
}

.modal-eyebrow {
  font-family: 'Plus Jakarta Sans', sans-serif;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #5ed29c;
  margin: 0 0 8px 0;
}

.modal-heading {
  font-size: 36px;
  font-weight: 800;
  text-transform: uppercase;
  color: #fff;
  margin: 0 0 16px 0;
  line-height: 1.05;
}

.modal-subtitle {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.55);
  line-height: 1.7;
  margin: 0;
}

.modal-divider {
  border: none;
  border-top: 1px solid rgba(94, 210, 156, 0.1);
  margin: 32px 0;
}

.modal-section-title {
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 20px 0;
}

.modal-card {
  margin-bottom: 20px;
  padding: 20px;
  background: rgba(94, 210, 156, 0.04);
  border: 1px solid rgba(94, 210, 156, 0.08);
  border-radius: 12px;
}

.modal-card-head {
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 8px 0;
}

.modal-card-body {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.55);
  line-height: 1.7;
  margin: 0;
}

.cn-green {
  color: #5ed29c;
  font-weight: 700;
}

.modal-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 4px;
}

.modal-link-item {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 14px 18px;
  background: rgba(94, 210, 156, 0.04);
  border: 1px solid rgba(94, 210, 156, 0.1);
  border-radius: 10px;
  text-decoration: none;
  color: #fff;
  transition: all 0.25s;
}
.modal-link-item:hover {
  border-color: rgba(94, 210, 156, 0.3);
  background: rgba(94, 210, 156, 0.08);
}
.modal-link-icon {
  font-size: 18px;
  color: #5ed29c;
  flex-shrink: 0;
}
.modal-link-item strong {
  display: block;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 2px;
}
.modal-link-item span {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.4);
}

.modal-footer-note {
  text-align: center;
  padding-top: 8px;
}
.modal-footer-note p {
  font-size: 13px;
  color: rgba(255, 255, 255, 0.35);
  margin: 0;
}
.modal-footer-sub {
  margin-top: 6px !important;
  font-size: 11px !important;
  color: rgba(255, 255, 255, 0.2) !important;
}

/* ── Modal Transition ── */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.35s ease;
}
.modal-enter-active .modal-panel,
.modal-leave-active .modal-panel {
  transition: transform 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.35s ease;
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
.modal-enter-from .modal-panel {
  transform: scale(0.92) translateY(20px);
  opacity: 0;
}
.modal-leave-to .modal-panel {
  transform: scale(0.92) translateY(20px);
  opacity: 0;
}

@media (max-width: 600px) {
  .modal-backdrop {
    padding: 16px;
  }
  .modal-scroll {
    padding: 40px 24px 32px;
  }
  .modal-heading {
    font-size: 26px;
  }
}
</style>