// Progressive enhancement: navigation is visible when JavaScript is unavailable.
const toggle = document.querySelector('.nav-toggle');
const navigation = document.querySelector('#site-navigation');
if (toggle && navigation) {
  document.documentElement.classList.add('js');
  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
    toggle.textContent = open ? 'Close' : 'Menu';
  };
  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });
  // Match the CSS breakpoint so a mobile menu does not stay open after resizing.
  const desktopNavigation = window.matchMedia('(min-width: 701px)');
  desktopNavigation.addEventListener('change', (event) => {
    if (event.matches) setOpen(false);
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
}

// Native modal image viewer: focus stays inside until dismissal.
const imageLinks = document.querySelectorAll('.collage-photo a, .technical-figure a');
if (imageLinks.length && typeof HTMLDialogElement !== 'undefined') {
  const viewer = document.createElement('dialog');
  viewer.className = 'image-viewer';
  viewer.setAttribute('aria-label', 'Image viewer');
  viewer.innerHTML = '<div class="viewer-panel"><button class="viewer-close" type="button" autofocus aria-label="Close image viewer">Close <span aria-hidden="true">×</span></button><figure><img class="viewer-image" alt=""><figcaption class="viewer-caption"></figcaption></figure></div>';
  document.body.append(viewer);
  const image = viewer.querySelector('.viewer-image');
  const caption = viewer.querySelector('.viewer-caption');
  const closeButton = viewer.querySelector('.viewer-close');
  let trigger;

  imageLinks.forEach((link) => {
    const thumbnail = link.querySelector('img') || link.closest('figure')?.querySelector('img');
    if (!thumbnail) return;
    link.setAttribute('aria-label', `Enlarge image: ${thumbnail.alt}`);
    link.removeAttribute('target');
    if (!link.querySelector('img')) link.textContent = 'Enlarge image';
    link.addEventListener('click', (event) => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      trigger = link;
      image.src = link.href;
      image.alt = thumbnail.alt;
      caption.textContent = thumbnail.alt;
      viewer.showModal();
      document.body.classList.add('viewer-open');
    });
  });

  closeButton.addEventListener('click', () => viewer.close());
  viewer.addEventListener('keydown', (event) => {
    // Close is the viewer's only interactive control; wrap keyboard focus here.
    if (event.key === 'Tab') {
      event.preventDefault();
      closeButton.focus();
    }
  });
  viewer.addEventListener('click', (event) => {
    if (event.target === viewer) viewer.close();
  });
  viewer.addEventListener('close', () => {
    document.body.classList.remove('viewer-open');
    trigger?.focus({ preventScroll: true });
    image.removeAttribute('src');
  });
}
