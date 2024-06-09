const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: ["./templates/**/*.{html,htm}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', defaultTheme.fontFamily.sans]
      }
    },
  },
  plugins: [],
}

