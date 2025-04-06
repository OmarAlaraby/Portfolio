document.addEventListener('DOMContentLoaded', function() {
    // Auto dismiss alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            // Create the bootstrap alert instance and call hide method
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // Get all navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Add click event listener to each link
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            this.classList.add('active');
        });
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add animation class to elements when they come into view
    function fadeInOnScroll() {
        const sections = document.querySelectorAll('section');
        
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (sectionTop < windowHeight - 100) {
                section.classList.add('visible');
            }
        });
    }
    
    // Initialize particles.js for background effect
    if (typeof particlesJS !== 'undefined') {
        particlesJS('particles-js', {
            particles: {
                number: { value: 120, density: { enable: true, value_area: 800 } },
                color: { value: '#ffffff' },
                shape: {
                    type: 'circle',
                    stroke: { width: 0, color: '#000000' },
                    polygon: { nb_sides: 5 }
                },
                opacity: {
                    value: 0.7,
                    random: true,
                    anim: { 
                        enable: true,
                        speed: 0.8,
                        opacity_min: 0.3,
                        sync: false
                    }
                },
                size: {
                    value: 3,
                    random: true,
                    anim: { 
                        enable: true,
                        speed: 2,
                        size_min: 0.5,
                        sync: false
                    }
                },
                line_linked: {
                    enable: false,
                    distance: 150,
                    color: '#ffffff',
                    opacity: 0.3,
                    width: 1
                },
                move: {
                    enable: true,
                    speed: 0.8,
                    direction: 'none',
                    random: true,
                    straight: false,
                    out_mode: 'out',
                    bounce: false
                }
            },
            interactivity: {
                detect_on: 'canvas',
                events: {
                    onhover: { enable: true, mode: 'bubble' },
                    onclick: { enable: true, mode: 'push' },
                    resize: true
                },
                modes: {
                    bubble: { 
                        distance: 200, 
                        size: 5, 
                        duration: 2, 
                        opacity: 0.8, 
                        speed: 3 
                    },
                    push: { particles_nb: 5 }
                }
            },
            retina_detect: true
        });
    }
    
    // Initial check
    fadeInOnScroll();
    
    // Check on scroll
    window.addEventListener('scroll', fadeInOnScroll);
    
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Skills tracks infinite scroll setup
    function setupSkillsTracks() {
        const tracks = document.querySelectorAll('.skills-track');
        
        tracks.forEach(track => {
            // Clone the cards for infinite scrolling
            const cards = track.querySelectorAll('.skill-card');
            const cardsToClone = [...cards].map(card => card.cloneNode(true));
            
            // Append clones to the track
            cardsToClone.forEach(card => {
                track.appendChild(card);
            });
        });
    }
    
    setupSkillsTracks();

    // Project Carousel Setup
    function initProjectCarousel() {
        const carousel = document.querySelector('.projects-carousel');
        const cards = Array.from(carousel.querySelectorAll('.project-card'));
        const prevBtn = document.querySelector('.carousel-prev');
        const nextBtn = document.querySelector('.carousel-next');
        const indicators = document.querySelector('.carousel-indicators');
        const isMobile = window.innerWidth <= 768;
        
        let currentIndex = 0;
        const cardCount = cards.length;
        
        // Skip if no carousel is found
        if (!carousel || cards.length === 0) return;
        
        // Create indicator dots
        cards.forEach((_, index) => {
            const dot = document.createElement('div');
            dot.classList.add('carousel-indicator');
            if (index === 0) dot.classList.add('active');
            dot.addEventListener('click', () => goToCard(index));
            indicators.appendChild(dot);
        });
        
        // Initial positioning
        updateCarousel();
        
        // Navigation buttons
        if (prevBtn) prevBtn.addEventListener('click', previousCard);
        if (nextBtn) nextBtn.addEventListener('click', nextCard);
        
        // Enhanced Touch/swipe support with better thresholds for mobile
        let touchStartX = 0;
        let touchEndX = 0;
        let touchStartY = 0;
        let touchEndY = 0;
        let isScrolling = false;
        
        carousel.addEventListener('touchstart', e => {
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
            isScrolling = false;
        }, { passive: true });
        
        carousel.addEventListener('touchmove', e => {
            // Detect vertical scrolling to prevent carousel from changing during page scroll
            if (!isScrolling) {
                touchEndY = e.changedTouches[0].screenY;
                isScrolling = Math.abs(touchEndY - touchStartY) > 30;
            }
        }, { passive: true });
        
        carousel.addEventListener('touchend', e => {
            if (isScrolling) return; // Skip if user was trying to scroll the page
            
            touchEndX = e.changedTouches[0].screenX;
            const swipeDistance = touchStartX - touchEndX;
            const swipeThreshold = isMobile ? 30 : 50; // More sensitive on mobile
            
            if (Math.abs(swipeDistance) > swipeThreshold) {
                if (swipeDistance > 0) {
                    nextCard();
                } else {
                    previousCard();
                }
            }
        }, { passive: true });
        
        // Add resize event listener to adjust carousel for different screen sizes
        window.addEventListener('resize', () => {
            updateCarousel();
        });
        
        // Keyboard navigation
        document.addEventListener('keydown', e => {
            if (isElementInViewport(carousel)) {
                if (e.key === 'ArrowLeft') {
                    previousCard();
                } else if (e.key === 'ArrowRight') {
                    nextCard();
                }
            }
        });
        
        // Navigation functions
        function previousCard() {
            currentIndex = (currentIndex - 1 + cardCount) % cardCount;
            updateCarousel();
        }
        
        function nextCard() {
            currentIndex = (currentIndex + 1) % cardCount;
            updateCarousel();
        }
        
        function goToCard(index) {
            currentIndex = index;
            updateCarousel();
        }
        
        function updateCarousel() {
            // Check if mobile view
            const isMobile = window.innerWidth <= 768;
            
            // First, pause all videos and remove video-playing class
            cards.forEach(card => {
                const video = card.querySelector('video');
                if (video) {
                    video.pause();
                }
            });
            
            // Update cards
            cards.forEach((card, index) => {
                // Calculate position (-2, -1, 0, 1, 2)
                const position = (((index - currentIndex) % cardCount) + cardCount) % cardCount;
                
                // Assign position -2 to 2, with 0 being the center card
                const cardPosition = position <= Math.floor(cardCount / 2) 
                    ? position 
                    : position - cardCount;
                
                // Apply position attribute for styling
                card.setAttribute('data-position', cardPosition);
                
                // Remove all old positions
                card.classList.remove('center', 'left', 'right');
                
                // Add appropriate position class
                if (cardPosition === 0) card.classList.add('center');
                else if (cardPosition < 0) card.classList.add('left');
                else card.classList.add('right');
                
                // Handle videos - only play video in center card
                const video = card.querySelector('video');
                if (video) {
                    if (cardPosition === 0) {
                        // Reset video to start and play
                        video.currentTime = 0;
                        video.play().catch(err => console.log('Video play failed:', err));
                        
                        // Make sure overlay hover effect still works for center card
                        const projectImage = video.closest('.project-image');
                        if (projectImage) {
                            const overlay = projectImage.querySelector('.project-overlay');
                            if (overlay) {
                                // Add hover event listeners for overlay
                                overlay.addEventListener('mouseenter', function() {
                                    video.pause();
                                });
                                
                                overlay.addEventListener('mouseleave', function() {
                                    video.play().catch(err => {});
                                });
                            }
                        }
                    }
                }
            });
            
            // Update indicators
            const indicatorDots = indicators.querySelectorAll('.carousel-indicator');
            indicatorDots.forEach((dot, index) => {
                if (index === currentIndex) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        }
    }
    
    // Helper function to check if element is in viewport
    function isElementInViewport(el) {
        const rect = el.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }
    
    // Initialize project carousel
    initProjectCarousel();

    // Enhanced hover tilt effect for project cards
    function setupTiltEffect() {
        const centerCard = document.querySelector('.project-card[data-position="0"]');
        if (!centerCard) return;
        
        const tiltEffect = function(e) {
            const card = this;
            const cardRect = card.getBoundingClientRect();
            const cardWidth = cardRect.width;
            const cardHeight = cardRect.height;
            
            // Calculate mouse position relative to card
            const mouseX = e.clientX - cardRect.left;
            const mouseY = e.clientY - cardRect.top;
            
            // Calculate rotation values (max 5 degrees)
            const rotateY = ((mouseX / cardWidth) - 0.5) * 5;
            const rotateX = ((0.5 - (mouseY / cardHeight)) * 5);
            
            // Apply the rotation and slight scale
            card.style.transform = `translateX(-50%) translateZ(10px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        };
        
        const resetTilt = function() {
            this.style.transform = `translateX(-50%) translateZ(0) rotateY(0deg) rotateX(0deg)`;
            setTimeout(() => {
                this.style.transform = '';
            }, 100);
        };
        
        // Watch for the active card and add tilt effect
        const observer = new MutationObserver(mutations => {
            mutations.forEach(mutation => {
                if (mutation.attributeName === 'data-position') {
                    const card = mutation.target;
                    
                    // Remove event listeners from all cards
                    document.querySelectorAll('.project-card').forEach(card => {
                        card.removeEventListener('mousemove', tiltEffect);
                        card.removeEventListener('mouseleave', resetTilt);
                    });
                    
                    // Add event listeners only to center card
                    if (card.getAttribute('data-position') === '0') {
                        card.addEventListener('mousemove', tiltEffect);
                        card.addEventListener('mouseleave', resetTilt);
                    }
                }
            });
        });
        
        // Observe all project cards
        document.querySelectorAll('.project-card').forEach(card => {
            observer.observe(card, { attributes: true });
            
            // Initialize for the center card
            if (card.getAttribute('data-position') === '0') {
                card.addEventListener('mousemove', tiltEffect);
                card.addEventListener('mouseleave', resetTilt);
            }
        });
    }
    
    // Add particle star effect behind project cards
    function setupStarParticles() {
        const carouselContainer = document.querySelector('.projects-carousel-container');
        if (!carouselContainer) return;
        
        // Create canvas for star particles
        const canvas = document.createElement('canvas');
        canvas.classList.add('project-stars-canvas');
        carouselContainer.appendChild(canvas);
        
        // Style the canvas
        canvas.style.position = 'absolute';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100%';
        canvas.style.height = '100%';
        canvas.style.pointerEvents = 'none';
        canvas.style.zIndex = '0';
        
        const ctx = canvas.getContext('2d');
        let particles = [];
        
        function resizeCanvas() {
            canvas.width = carouselContainer.offsetWidth;
            canvas.height = carouselContainer.offsetHeight;
            createParticles();
        }
        
        function createParticles() {
            particles = [];
            const particleCount = Math.min(50, Math.floor(canvas.width * canvas.height / 10000));
            
            for (let i = 0; i < particleCount; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    size: Math.random() * 2 + 0.5,
                    speed: Math.random() * 0.2 + 0.1,
                    opacity: Math.random() * 0.5 + 0.2,
                    color: i % 5 === 0 ? '#00ff9d' : '#ffffff'
                });
            }
        }
        
        function animateParticles() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            particles.forEach(p => {
                p.y -= p.speed;
                if (p.y < -10) p.y = canvas.height + 10;
                
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                ctx.fillStyle = p.color;
                ctx.globalAlpha = p.opacity;
                ctx.fill();
            });
            
            requestAnimationFrame(animateParticles);
        }
        
        // Initialize and start animation
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
        animateParticles();
    }
    
    // Enhance section title reveal animations - simplified and fixed
    function enhanceSectionTitles() {
        // Instead of manipulating the DOM structure which caused issues,
        // simply add a class to section titles for styling
        const titles = document.querySelectorAll('.section-title');
        
        titles.forEach(title => {
            title.classList.add('visible');
        });
    }
    
    // Function to toggle fullscreen for videos
    function toggleFullscreen(videoId) {
        const video = document.getElementById(videoId);
        if (!video) return;
        
        if (video.requestFullscreen) {
            video.requestFullscreen();
        } else if (video.webkitRequestFullscreen) { /* Safari */
            video.webkitRequestFullscreen();
        } else if (video.msRequestFullscreen) { /* IE11 */
            video.msRequestFullscreen();
        }
        
        // Add class to parent card to prevent animations
        const card = video.closest('.project-card');
        if (card) {
            card.classList.add('video-playing');
        }
    }

    // Handle video interactions for project cards
    function setupVideoHandlers() {
        // Find all project cards with videos
        const videoContainers = document.querySelectorAll('.project-card .video-container');
        
        videoContainers.forEach(container => {
            const video = container.querySelector('video');
            const card = container.closest('.project-card');
            const projectImage = container.closest('.project-image');
            const overlay = projectImage.querySelector('.project-overlay');
            
            if (!video || !card) return;
            
            // Set up autoplay and loop
            video.autoplay = false; // Don't autoplay initially
            video.muted = true; // Required for autoplay in most browsers
            video.loop = true;
            video.controls = false; // Remove video controls
            video.setAttribute('playsinline', ''); // For iOS
            
            // Only play videos in center cards initially
            if (card.getAttribute('data-position') === '0') {
                video.play().catch(err => console.log('Autoplay failed:', err));
            }
            
            // Pause video when overlay is being hovered to prevent click conflicts
            if (overlay) {
                overlay.addEventListener('mouseenter', function() {
                    video.pause();
                });
                
                overlay.addEventListener('mouseleave', function() {
                    // Only resume playing if it's the center card
                    if (card.getAttribute('data-position') === '0') {
                        video.play().catch(err => {});
                    }
                });
            }
        });
    }

    // Initialize all enhanced effects
    setupTiltEffect();
    setupStarParticles();
    enhanceSectionTitles();
    setupVideoHandlers();
}); 