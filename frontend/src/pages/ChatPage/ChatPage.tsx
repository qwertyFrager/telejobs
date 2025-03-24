'use client';

import { Avatar } from '@/shared/Avatar';
import ChatHeader from './components/ChatHeader';
import ChatInput from './components/ChatInput';
import PartnerMessage from './components/PartnerMessage';
import UserMessage from './components/UserMessage';

const ChatPage = () => {
  //   const navigate = useRouter();

  //   const onClickBackButton = () => {
  //     navigate.push(ROUTE.CHATS);
  //   };

  return (
    <div className="overflow-hidden h-screen">
      <ChatHeader />
      <div className="bg-dark-green h-full pt-5 overflow-scroll pb-64 px-6">
        <div className="text-center text-gray text-xs">20th September</div>

        <PartnerMessage />
        <UserMessage />
        <UserMessage />
        <UserMessage />
        <PartnerMessage />
        <PartnerMessage />
        <div className="text-center text-gray text-xs">20th September</div>

        <PartnerMessage />
        <UserMessage />
        <UserMessage />
        <UserMessage />
        <PartnerMessage />
        <PartnerMessage />
        <div className="text-center text-gray text-xs">20th September</div>

        <PartnerMessage />
        <UserMessage />
        <UserMessage />
        <UserMessage />
        <PartnerMessage />
        <PartnerMessage />
      </div>
      <div className="fixed bottom-0 left-0 w-full">
        <div className="bg-dark-green border-t border-dirty-green py-3 px-5 flex items-center gap-3">
          <Avatar src="https://i.pravatar.cc/300" className="w-[18px] h-[18px] rounded" />
          <span className="text-gray text-xs">Frontend Developer</span>
        </div>
        <ChatInput />
      </div>
    </div>
  );
};

export default ChatPage;
