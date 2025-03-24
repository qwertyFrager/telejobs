import Image from 'next/image';
import { twMerge } from 'tailwind-merge';

export const Avatar = ({ src, className }: { src: string; className?: string }) => {
  return (
    <Image src={src} alt="avatar" width={32} height={32} className={twMerge('shadow-border rounded-xl', className)} />
  );
};
