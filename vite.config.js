//vite.config.js
import { defineConfig } from 'vite';
import { djangoVitePlugin } from 'django-vite-plugin';

export default defineConfig({
  plugins: [
    djangoVitePlugin([
      'assets/js/index.js',
      'assets/css/main.css',
    ])
  ],
});
