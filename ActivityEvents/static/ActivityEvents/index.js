document.addEventListener('DOMContentLoaded', function() {
// Active Link Indicator
const links = document.querySelectorAll('nav a');
links.forEach(link => {
  if (link.href === window.location.href) {
    link.classList.add('active');
  }
})
})