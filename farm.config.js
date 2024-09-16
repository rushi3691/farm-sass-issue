import { defineConfig } from '@farmfe/core';

export default defineConfig({
  compilation: {
    input: {
      index: './public/index.html',
      app: './src/index.jsx'
    },
    output: {
      path: 'build',
      publicPath: '/',
      targetEnv: 'browser'
    },
  },
  plugins: [
    '@farmfe/plugin-react',
    '@farmfe/plugin-sass'
  ]
});