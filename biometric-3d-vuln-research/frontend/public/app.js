// ============================================================
//   app.js — CodeNest Frontend Logic
// ============================================================

document.addEventListener('DOMContentLoaded', () => {

  // ===================== MOBILE MENU =====================
  const menuToggle = document.getElementById('menu-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  const menuIcon = document.getElementById('menu-icon');

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', () => {
      const isOpen = mobileMenu.classList.contains('opacity-100');
      if (isOpen) {
        mobileMenu.classList.remove('opacity-100', 'pointer-events-auto');
        mobileMenu.classList.add('opacity-0', 'pointer-events-none');
        menuIcon.innerHTML = '<line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="18" x2="20" y2="18"/>';
      } else {
        mobileMenu.classList.remove('opacity-0', 'pointer-events-none');
        mobileMenu.classList.add('opacity-100', 'pointer-events-auto');
        menuIcon.innerHTML = '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>';
      }
    });
  }

  // ===================== BACKGROUND VIDEO =====================
  const bgVideo = document.getElementById('bg-video');
  if (bgVideo) {
    bgVideo.play().catch(() => {});
  }

  // ===================== SYNC OVERLAY HEIGHT TO VIDEO =====================
  const overlay = document.querySelector('.video-overlay');
  const videoEl = document.getElementById('bg-video');

  function syncOverlayHeight() {
    if (!overlay || !videoEl) return;
    const videoHeight = videoEl.clientHeight;
    if (videoHeight > 0) {
      overlay.style.height = videoHeight + 'px';
    }
  }

  if (overlay && videoEl) {
    syncOverlayHeight();
    videoEl.addEventListener('loadedmetadata', syncOverlayHeight);
    videoEl.addEventListener('resize', syncOverlayHeight);
    window.addEventListener('resize', syncOverlayHeight);

    // observe video size changes
    if (window.ResizeObserver) {
      const ro = new ResizeObserver(() => syncOverlayHeight());
      ro.observe(videoEl);
    }
  }

  // ===================== GALLERY VIDEOS =====================
  const galleryVideos = document.querySelectorAll('.gallery-video');
  galleryVideos.forEach(v => {
    v.play().catch(() => {});
  });

});
