'use client';
import { useRouter } from 'next/navigation';

import { ROUTE } from '@/constants/route';
import { ArrowIcon } from '@/shared/icons/primary/ArrowIcon';
import { MoreIcon } from '@/shared/icons/primary/MoreIcon';

const ChatHeader = () => {
  const navigate = useRouter();

  const onClickBackButton = () => {
    navigate.push(ROUTE.CHATS);
  };
  return (
    <>
      <div className="flex items-center justify-between border-b border-dirty-green py-3.5 px-6 text-center bg-dark-green">
        <button onClick={onClickBackButton}>
          <ArrowIcon className="rotate-180" stroke="#768C9E" />
        </button>
        <div className="flex flex-col gap-1">
          <span className="font-bold text-base">Alex</span>
          <span className="text-gray">Last seen 1 day ago</span>
        </div>
        <button>
          <MoreIcon />
        </button>
      </div>
      <div className="px-6 py-2 flex justify-between items-center border-b border-dirty-green bg-dark-green text-white">
        <div className="flex flex-col text-xs">
          <span>Response</span>
          <span className="font-bold">Frontend Developer</span>
        </div>
        <button>
          <ArrowIcon />
        </button>
      </div>
    </>
  );
};

export default ChatHeader;
