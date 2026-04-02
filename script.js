document.addEventListener('DOMContentLoaded', () => {
    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const icon = hamburger.querySelector('i');

    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        if (navLinks.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });

    // Close mobile menu when a link is clicked
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        });
    });

    // Scroll Animation (Intersection Observer)
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');

    const revealSettings = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealSettings);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // Dynamic Image Loading script to pick different hero backgrounds from available files if needed
    // Assuming 'a.jpg' through 't.jpg' exist, let's just make the hero background rotate slightly
    // or just rely on CSS for now.

    // Lightbox Modal Logic
    const modal = document.getElementById("lightbox-modal");
    const modalImg = document.getElementById("lightbox-img");
    const captionText = document.getElementById("caption");
    const closeBtn = document.querySelector(".close-modal");

    // Add click event to all gallery images
    const triggers = document.querySelectorAll('.lightbox-trigger');
    triggers.forEach(img => {
        img.addEventListener('click', function() {
            modal.style.display = "block";
            // slight delay to allow display flex/block to apply before opacity transition
            setTimeout(() => {
                modal.classList.add("show");
            }, 10);
            modalImg.src = this.src;
            captionText.innerHTML = this.alt;
        });
    });

    // Close Modal Event
    const closeModal = () => {
        modal.classList.remove("show");
        setTimeout(() => {
            modal.style.display = "none";
        }, 300); // match transition time
    };

    closeBtn.addEventListener('click', closeModal);

    // Close when clicking outside the image
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

});
