import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about.html'),
        events: resolve(__dirname, 'events.html'),
        gallery: resolve(__dirname, 'gallery.html'),
        membership: resolve(__dirname, 'membership.html'),
        'get-involved': resolve(__dirname, 'get-involved.html'),
        ambassadors: resolve(__dirname, 'ambassadors.html'),
        'partners-venues': resolve(__dirname, 'partners-venues.html'),
        'membership-tiers': resolve(__dirname, 'membership-tiers.html'),
        'event-management': resolve(__dirname, 'event-management.html'),
        mentorship: resolve(__dirname, 'mentorship.html'),
        'knowledge-hub': resolve(__dirname, 'knowledge-hub.html'),
        login: resolve(__dirname, 'login.html'),
        'education-skills': resolve(__dirname, 'education-skills.html'),
        'professional-networking': resolve(__dirname, 'professional-networking.html'),
        'social-cultural-events': resolve(__dirname, 'social-cultural-events.html'),
        admin: resolve(__dirname, 'admin.html'),
      }
    }
  }
})
