// HTMX event handling for dog pagination
document.addEventListener('htmx:beforeRequest', function(event) {
  if (event.detail.target.id === 'dog-results-container') {
    // Show loading indicator
  }
});

// Mobile navigation dropdown handling
document.addEventListener('DOMContentLoaded', function() {
  // Handle adopt dropdown link click in both mobile and desktop views
  const adoptDropdownLinks = document.querySelectorAll('.adopt-dropdown > a');
  adoptDropdownLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      // Find the toggle-dropdown element and trigger a click on it
      const parentDropdown = this.closest('.dropdown');
      const toggleDropdown = parentDropdown.querySelector('.toggle-dropdown');
      
      if (toggleDropdown) {
        toggleDropdown.click();
      }
    });
  });

  // Prevent mobile menu from closing when clicking our custom adopt link
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    if (navmenu.classList.contains('mobile-adopt-link')) {
      // Remove the default click handler for this specific link
      navmenu.setAttribute('data-no-close', 'true');
    }
  });
  
  // Fix any remaining indentation issues with the adopt dropdown
  const adoptDropdown = document.querySelector('.adopt-dropdown');
  if (adoptDropdown) {
    // Force override any inherited styles that might cause indentation
    adoptDropdown.style.paddingLeft = '0';
    adoptDropdown.style.marginLeft = '0';
    
    // Apply the same positioning as other top-level menu items
    const regularItems = document.querySelectorAll('.navmenu > ul > li:not(.dropdown)');
    if (regularItems.length > 0) {
      const firstItem = regularItems[0];
      const computedStyle = window.getComputedStyle(firstItem);
      
      // Apply the same padding and margin
      adoptDropdown.style.padding = computedStyle.padding;
      adoptDropdown.style.margin = computedStyle.margin;
      
      // Apply to the mobile-adopt-link as well
      const mobileAdoptLink = adoptDropdown.querySelector('.mobile-adopt-link');
      if (mobileAdoptLink) {
        const regularLinks = document.querySelectorAll('.navmenu > ul > li > a');
        if (regularLinks.length > 0) {
          const firstLink = regularLinks[0];
          const linkStyle = window.getComputedStyle(firstLink);
          
          mobileAdoptLink.style.paddingLeft = linkStyle.paddingLeft;
          mobileAdoptLink.style.marginLeft = linkStyle.marginLeft;
        }
      }
    }
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