// Document ready
document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded");
    
    // Initialize mobile menu
    initMobileMenu();
    
    // Initialize direct navigation with vanilla JS
    setupNavigation();
    
    // Initialize animations
    initAnimations();
    
    // Initialize form handling
    initContactForm();
});

// Mobile menu functionality
function initMobileMenu() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            
            // Toggle menu icon
            const icon = mobileMenuBtn.querySelector('i');
            if (icon.classList.contains('fa-bars')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // Close menu when clicking on a link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            const icon = mobileMenuBtn.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        });
    });
}

// Setup navigation for all links 
function setupNavigation() {
    // Hide all sections except home initially
    const allSections = document.querySelectorAll('section');
    allSections.forEach(section => {
        if (section.id !== 'home') {
            section.style.display = 'none';
        }
    });
    
    // Get all nav links including the hero CTA
    const navLinks = document.querySelectorAll('.nav-link, .hero-cta');
    console.log(`Found ${navLinks.length} navigation links`);
    
    // Process all navigation links
    navLinks.forEach(link => {
        console.log(`Setting up click handler for ${link.textContent.trim()} link to ${link.getAttribute('href')}`);
        
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Extract the target section ID from the href attribute
            const targetId = this.getAttribute('href').substring(1); // Remove the # character
            console.log(`Clicked on ${this.textContent.trim()}, navigating to #${targetId}`);
            
            // Find the target section
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                console.log(`Found target section with id=${targetId}`);
                
                // Hide all sections first
                allSections.forEach(section => {
                    section.style.display = 'none';
                });
                
                // Show the target section
                targetSection.style.display = 'block';
                
                // Update active state in navigation
                document.querySelectorAll('.nav-link').forEach(navLink => {
                    if (navLink.getAttribute('href') === `#${targetId}`) {
                        navLink.classList.add('active');
                    } else {
                        navLink.classList.remove('active');
                    }
                });
                
                // Scroll to top
                window.scrollTo(0, 0);
            } else {
                console.error(`Target section #${targetId} not found!`);
            }
        });
    });
    
    // Handle navbar appearance on scroll
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// Animation functionality
function initAnimations() {
    // Fade-in animations on scroll
    const fadeElements = document.querySelectorAll('.fade-in');
    
    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                fadeObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    fadeElements.forEach(element => {
        fadeObserver.observe(element);
    });
    
    // Animate hero elements sequentially
    const heroElements = document.querySelectorAll('.hero .fade-in');
    heroElements.forEach((element, index) => {
        setTimeout(() => {
            element.classList.add('visible');
        }, 300 * index);
    });
}

// Contact form handling
function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = new FormData(contactForm);
            const data = {
                name: formData.get('name'),
                email: formData.get('email'),
                subject: formData.get('subject'),
                message: formData.get('message')
            };

            try {
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                
                if (response.ok) {
                    showNotification('Thank you for your message! I\'ll get back to you soon.', 'success');
                    contactForm.reset();
                } else {
                    showNotification('There was an error sending your message. Please try again.', 'error');
                }
            } catch (error) {
                console.error('Error:', error);
                showNotification('There was an error sending your message. Please try again.', 'error');
            }
        });
    }
}

// Notification function
function showNotification(message, type) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    // Add to body
    document.body.appendChild(notification);
    
    // Show notification
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
} 