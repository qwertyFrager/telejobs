import { Metadata } from 'next';
// import { Space_Mono } from 'next/font/google';

import './globals.css';
import { Providers } from './providers';

// const spaceMono = Space_Mono({ weight: ['400', '700'], subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'TeleJobs',
  description: 'Jobs and Freelance in one Telegram mini-app!',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      {/* <body className={`${spaceMono.className}`}> */}
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
