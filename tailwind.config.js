/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./**/*.html', './**/*.js'],
  content: ["./src/**/*.{html,js}", "./templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}