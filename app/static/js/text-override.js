// Override script to fix heading
document.addEventListener('DOMContentLoaded', function() {
  console.log('Text override script running');
  
  // Find all h1 elements in the hero section
  const heroH1Elements = document.querySelectorAll('h1');
  console.log('Found h1 elements:', heroH1Elements.length);
  
  // Check all h1 elements anywhere on the page
  heroH1Elements.forEach(function(h1) {
    console.log('H1 text:', h1.textContent);
    if (h1.textContent.includes('Impact')) {
      console.log('Replacing Impact text');
      h1.textContent = 'Welcome to Barb\'s Dog Rescue';
    }
  });
});
