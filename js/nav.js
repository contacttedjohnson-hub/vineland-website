/* Vineland Development — minimal nav toggle for the mobile hamburger.
   No framework. On desktop the CSS handles the How-to-Pay hover dropdown;
   this only opens/closes the collapsed nav panel on small screens. */
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!toggle || !nav) return;

  toggle.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Close the panel after tapping a real navigation link (not the
  // How-to-Pay parent, which should still navigate on tap per spec).
  nav.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (a) nav.classList.remove('open');
  });
})();
