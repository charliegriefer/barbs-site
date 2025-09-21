// HTMX event handling for dog pagination
document.addEventListener('htmx:beforeRequest', function(event) {
  if (event.detail.target.id === 'dog-results-container') {
    // Show loading indicator
  }
});

document.addEventListener('htmx:afterSwap', function(event) {
  if (event.detail.target.id === 'dog-results-container') {
    // Scroll to the available-dogs section heading for better orientation
    const availableDogsSection = document.getElementById('available-dogs');
    if (availableDogsSection) {
      const headerHeight = 100; // Adjust based on your site's header height
      const topPosition = availableDogsSection.getBoundingClientRect().top + window.pageYOffset - headerHeight;
      
      window.scrollTo({
        top: topPosition,
        behavior: 'smooth'
      });
    }
  }
});