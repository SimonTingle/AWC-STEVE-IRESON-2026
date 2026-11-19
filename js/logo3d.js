// Plays intro once, then swaps seamlessly to the idle loop.
// Static PNG stays underneath as fallback (Safari, reduced motion, errors).
(function () {
  var w = document.getElementById('logo3d');
  var a = document.getElementById('l3-intro'), b = document.getElementById('l3-loop');
  if (!w || !a || !b) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!a.canPlayType || !a.canPlayType('video/webm; codecs="vp9"')) return;
  var ready = 0;
  function start() {
    if (++ready < 2) return;
    a.play().then(function () { a.classList.add('on'); }).catch(function () {});
  }
  a.addEventListener('canplaythrough', start, { once: true });
  b.addEventListener('canplaythrough', start, { once: true });
  a.addEventListener('ended', function () {
    b.currentTime = 0;
    b.play().then(function () {
      var swap = function () { b.classList.add('on'); a.classList.remove('on'); };
      if (b.requestVideoFrameCallback) b.requestVideoFrameCallback(swap); else swap();
    }).catch(function () {});
  });
  function fail() { a.remove(); b.remove(); }
  a.addEventListener('error', fail); b.addEventListener('error', fail);
  a.load(); b.load();
})();
