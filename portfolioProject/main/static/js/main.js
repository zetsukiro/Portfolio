document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('sidebarToggle');
  const aside = document.querySelector('.sidebar');
  if (btn && aside) {
    btn.addEventListener('click', () => {
      aside.classList.toggle('open');
    });
  }
});
