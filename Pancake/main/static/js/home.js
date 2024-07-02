document.addEventListener('DOMContentLoaded', function() {
  const hero = document.querySelector('.hero');
  const form = document.querySelector('#tech-stack-form');

  window.addEventListener('scroll', () => {
    let scrollPosition = window.scrollY;
    let windowHeight = window.innerHeight;

    // Adjusted calculations for opacity and scale
    let heroOpacity = Math.min(1, scrollPosition / (windowHeight / 2));
    // Start changing the form's opacity and scale sooner
    let formStart = windowHeight / 3; // Adjust this value as needed
    let formOpacity = Math.max(0, Math.min(1, (scrollPosition - formStart) / (windowHeight / 2)));

    // Apply styles based on scroll position
    hero.style.opacity = 1 - heroOpacity;
    hero.style.transform = `scale(${1 - heroOpacity * 0.05})`;

    // Adjusted form opacity and scale application
    form.style.opacity = formOpacity;
    form.style.transform = `scale(${0.95 + formOpacity * 0.05})`;
  });
});