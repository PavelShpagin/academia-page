/**
 * Академія - Optical Positioning Systems
 * Premium Interactions
 */

(function() {
    'use strict';

    const nav = document.getElementById('nav');
    const navToggle = document.getElementById('navToggle');
    const mobileMenu = document.getElementById('mobileMenu');

    document.addEventListener('DOMContentLoaded', init);

    function init() {
        initNavigation();
        initMobileMenu();
        initSmoothScroll();
    }

    /**
     * Premium navigation with smooth transitions
     */
    function initNavigation() {
        let ticking = false;
        let lastScrollY = 0;
        
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    const scrollY = window.scrollY;
                    
                    // Add scrolled class
                    nav.classList.toggle('scrolled', scrollY > 80);
                    
                    lastScrollY = scrollY;
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    /**
     * Mobile menu with smooth open/close
     */
    function initMobileMenu() {
        navToggle.addEventListener('click', () => {
            const isActive = mobileMenu.classList.toggle('active');
            navToggle.classList.toggle('active');
            document.body.classList.toggle('no-scroll', isActive);
        });

        document.querySelectorAll('.mobile-link').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') closeMobileMenu();
        });
    }

    function closeMobileMenu() {
        mobileMenu.classList.remove('active');
        navToggle.classList.remove('active');
        document.body.classList.remove('no-scroll');
    }

    /**
     * Smooth scroll with easing
     */
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;

                e.preventDefault();
                const target = document.querySelector(href);
                
                if (target) {
                    const offset = nav.offsetHeight + 20;
                    const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
                    
                    window.scrollTo({ 
                        top, 
                        behavior: 'smooth' 
                    });
                    closeMobileMenu();
                }
            });
        });
    }

})();
