'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { twMerge } from 'tailwind-merge';

import { bottomMenu } from '@/constants/menu';

export const BottomMenu = () => {
  const pathname = usePathname();

  return (
    <div className="bg-dark-green border-t border-dirty-green fixed bottom-0 left-0 w-full pt-3 pb-6 flex justify-center gap-4">
      {bottomMenu.map((item) => {
        const isActive = pathname === item.href;
        const Icon = item.icon;

        return (
          <Link
            href={item.href}
            className={twMerge('flex flex-col items-center text-white', isActive && 'text-main')}
            key={item.label}
          >
            <span className="h-5">
              <Icon fill={isActive ? '#5EB5F7' : 'white'} />
            </span>
            {item.label}
          </Link>
        );
      })}
    </div>
  );
};
