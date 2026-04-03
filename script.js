// GSAP and ScrollTrigger initialization
gsap.registerPlugin(ScrollTrigger);

document.addEventListener('DOMContentLoaded', () => {
    // 1. Navbar Scroll & Dark Theme Toggle
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 2. Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const icon = hamburger?.querySelector('i');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
            if (icon) {
                if (navLinks.classList.contains('active')) {
                    icon.classList.remove('fa-bars');
                    icon.classList.add('fa-times');
                } else {
                    icon.classList.remove('fa-times');
                    icon.classList.add('fa-bars');
                }
            }
        });
    }

    // Mobile dropdown toggle
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener('click', (e) => {
            if (window.innerWidth <= 768) {
                e.stopPropagation();
                dropdown.classList.toggle('active');
            }
        });
    });

    // 3. Magnetic Buttons (GSAP)
    const magneticBtns = document.querySelectorAll('.magnetic-btn');
    
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            gsap.to(btn, {
                x: x * 0.4,
                y: y * 0.4,
                duration: 0.4,
                ease: "power2.out"
            });
        });

        btn.addEventListener('mouseleave', () => {
            gsap.to(btn, {
                x: 0,
                y: 0,
                duration: 0.7,
                ease: "elastic.out(1, 0.3)"
            });
        });
    });

    // 4. GSAP Scroll Animations
    // Fade Up
    gsap.utils.toArray('.gsap-fade-up').forEach(elem => {
        gsap.to(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
            },
            y: 0,
            opacity: 1,
            duration: 1,
            ease: "power3.out"
        });
    });

    // Fade In
    gsap.utils.toArray('.gsap-fade-in').forEach(elem => {
        gsap.to(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
            },
            opacity: 1,
            duration: 1.5,
            ease: "power2.out"
        });
    });

    // Stagger Item (for grids)
    const staggerContainers = document.querySelectorAll('.grid-2, .grid-3, .values-grid, .gallery-grid, .projects-grid');
    staggerContainers.forEach(container => {
        const items = container.querySelectorAll('.gsap-stagger-item');
        if (items.length > 0) {
            gsap.to(items, {
                scrollTrigger: {
                    trigger: container,
                    start: "top 85%",
                },
                y: 0,
                opacity: 1,
                duration: 0.8,
                stagger: 0.15,
                ease: "power3.out"
            });
        }
    });

    // Scale Up Images
    gsap.utils.toArray('.gsap-scale-up').forEach(elem => {
        gsap.to(elem, {
            scrollTrigger: {
                trigger: elem,
                start: "top 85%",
            },
            scale: 1,
            opacity: 1,
            duration: 1.2,
            ease: "power3.out"
        });
    });

    // Hero Parallax
    const heroBg = document.querySelector('.page-hero-bg');
    if (heroBg) {
        gsap.to(heroBg, {
            scrollTrigger: {
                trigger: ".page-hero",
                start: "top top",
                end: "bottom top",
                scrub: true
            },
            y: "30%",
            ease: "none"
        });
    }

    // 5. Gallery Filter Logic (for gallery.html)
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    if (filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class
                filterBtns.forEach(b => b.classList.remove('active'));
                // Add active class to clicked
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                galleryItems.forEach(item => {
                    if (filterValue === 'all' || item.classList.contains(filterValue)) {
                        item.style.display = 'block';
                        gsap.fromTo(item, { scale: 0.8, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4 });
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    }

    // 6. Lightbox Modal Logic
    const modal = document.getElementById("lightbox-modal");
    const modalImg = document.getElementById("lightbox-img");
    const captionText = document.getElementById("caption");
    const closeBtn = document.querySelector(".close-modal");

    if (modal && modalImg) {
        const triggers = document.querySelectorAll('.lightbox-trigger');
        triggers.forEach(img => {
            img.addEventListener('click', function(e) {
                e.preventDefault();
                modal.style.display = "block";
                setTimeout(() => modal.classList.add("show"), 10);
                
                // If the trigger wrapper is an anchor, use href, else use img src
                if (this.tagName === 'A') {
                    modalImg.src = this.getAttribute('href');
                    const innerImg = this.querySelector('img');
                    captionText.innerHTML = innerImg ? innerImg.getAttribute('alt') : '';
                } else if (this.tagName === 'IMG') {
                    modalImg.src = this.src;
                    captionText.innerHTML = this.alt;
                }
                
                document.body.style.overflow = 'hidden'; // prevent background scrolling
            });
        });

        const closeModal = () => {
            modal.classList.remove("show");
            setTimeout(() => {
                modal.style.display = "none";
                document.body.style.overflow = '';
            }, 300);
        };

        if (closeBtn) closeBtn.addEventListener('click', closeModal);

        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeModal();
            }
        });
    }
    // 7. Connect Form Submission Logic
    const contactForm = document.getElementById('contact-form-element');
    const successMsg = document.getElementById('form-success-message');
    
    if (contactForm && successMsg) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Stop page reload
            
            // Hide form and show success message
            contactForm.style.display = 'none';
            successMsg.style.display = 'block';
            
            // Animate it nicely using GSAP
            gsap.fromTo(successMsg, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.5 });
        });
    }
});
