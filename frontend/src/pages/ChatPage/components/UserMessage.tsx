import { MessageStatusIcon } from '@/shared/icons/MessageStatusIcon';

const UserMessage = () => {
  return (
    <div className="bg-[#5EB5F71A] py-1 px-2.5 rounded-xl w-fit shadow-border ml-auto my-1 text-xs">
      <p className="text-xs">Hello</p>
      <span className="flex text-gray items-center gap-1">
        00:40 <MessageStatusIcon />
      </span>
    </div>
  );
};

export default UserMessage;
