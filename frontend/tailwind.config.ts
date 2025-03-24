import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/shared/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "main",
        foreground: "var(--foreground)",
      },
      
    },
    colors:{
        'main':'#5EB5F7',
        'gray':'#768C9E',
        'black':"#000000",
        "dark":"#0E1621",
        "dark-green": "#17212B",
        "white":"#FFFFFF",
        'dirty-green':'#25303E'
    },
    boxShadow: {
        border: "0px 0px 2px 0px #FFFFFF99 inset",
        greenBorder: "0px 0px 2px 0px #5EB5F7 inset"
    },
    backgroundImage:{
        'gradient-blue-pink': "linear-gradient(91.76deg, #27A9E1 0.09%, #C727E1 100.09%)",
        'gradient-green-yellow': 'linear-gradient(91.54deg, #57E127 0%, #E1DA27 100%)'
    }
  },
  plugins: [],
};
export default config;