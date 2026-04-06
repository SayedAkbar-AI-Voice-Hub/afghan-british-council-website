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
      }
    }
  }
})
