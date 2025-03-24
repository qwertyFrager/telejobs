import { useRouter } from 'next/navigation';

import { ROUTE } from '@/constants/route';
import { Avatar } from '@/shared/Avatar';

interface IChatPreview {
  title: string;
  lastMessage: string;
  lastMessageDate: string;
}

const ChatItem = ({ chat }: { chat?: IChatPreview }) => {
  const navigate = useRouter();
  const onClickChat = () => {
    navigate.push(`${ROUTE.CHATS}/1`);
  };
  return (
    <button className="flex items-start text-white text-sm relative text-left" onClick={onClickChat}>
      <Avatar src="https://i.pravatar.cc/300" />
      <div className="flex flex-col ml-4">
        <span className="text-base font-bold">Alex</span>
        <span>Frontend Developer</span>
        <span className="text-gray mt-2">Hey, bro!</span>
      </div>
      <div className="ml-auto flex flex-col justify-between items-end h-full">
        <span className="text-gray">21:17</span>
        <span className="bg-main rounded-full flex items-center justify-center w-5 h-5 text-black text-xs absolute bottom-0">
          1
        </span>
      </div>
    </button>
  );
};

export default ChatItem;
