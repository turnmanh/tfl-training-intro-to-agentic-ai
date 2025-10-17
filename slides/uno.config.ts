import { defineConfig } from 'unocss';
import { presetWebFonts } from 'unocss';

export default defineConfig({
    theme: {
        colors: {
            'aai-slide': '#f6f6f6',
            'aai-blue': '#084059',
            'aai-green': '#18a5a7',
            'aai-blue-light': '#46add5',
            'aai-green-light': '#bfffc7',
            'aai-grey': '#b7c6cf',
            'aai-orange': '#ff611a',
            'aai-box-blue': '#b7c6cfff',
            'aai-box-grey': '#d6dde0ff',
        },
    },
    presets: [
        presetWebFonts({
            provider: 'google',
            fonts: {
                sans: {
                    name: 'Work Sans',
                    weights: [100, 200, 300, 400, 500, 600, 700, 800],
                },
            },
        }),
    ],
    safelist: [],
});
