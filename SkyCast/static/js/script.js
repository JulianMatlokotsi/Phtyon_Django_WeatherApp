document.addEventListener('DOMContentLoaded', function() {
    // Theme Toggle
    const themeToggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';

    if (currentTheme === 'dark') {
        document.body.setAttribute('data-theme', 'dark');
        themeToggleBtn.textContent = 'Switch to Light Mode';
    }

    themeToggleBtn.addEventListener('click', function () {
        if (document.body.getAttribute('data-theme') === 'dark') {
            document.body.setAttribute('data-theme', 'light');
            themeToggleBtn.textContent = 'Switch to Dark Mode';
            localStorage.setItem('theme', 'light');
        } else {
            document.body.setAttribute('data-theme', 'dark');
            themeToggleBtn.textContent = 'Switch to Light Mode';
            localStorage.setItem('theme', 'dark');
        }
    });

    // Loading Spinner
    const form = document.querySelector('form');
    const spinner = document.getElementById('loading-spinner');

    form.addEventListener('submit', function () {
        spinner.style.display = 'block';
    });
});