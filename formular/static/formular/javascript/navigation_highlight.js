document.addEventListener('DOMContentLoaded', function() {
    // Get the current path
    var path = window.location.pathname;
    console.log("Test")
    // Define the emoji representation for each link
    var emojiMap = {
        '{% url 'home' %}': '🏠',  // Home emoji
        '{% url 'showTableDB' %}': '👀',  // See Employee emoji
        // Add more URLs and corresponding emoji representations here
    };

    // Get all navigation links
    var navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    // Loop through each navigation link
    for (var i = 0; i < navLinks.length; i++) {
        var link = navLinks[i];

        // Check if the link's href matches the current path
        if (link.getAttribute('href') === path) {
            link.classList.add('active');

            // Create the <span class="sr-only"></span> element
            var span = document.createElement('span');
            span.classList.add('sr-only');
            

            // Append the <span> element to the link
            link.appendChild(span);

            // Get the emoji representation for the link
            var emoji = emojiMap[link.getAttribute('href')];

            // Create the <span> element for the emoji
            var emojiSpan = document.createElement('span');
            emojiSpan.classList.add('emoji');
            emojiSpan.textContent = emoji;

            // Insert the emoji span before the <span class="sr-only">(current)</span>
            span.parentNode.insertBefore(emojiSpan, span);
        }
    }
});