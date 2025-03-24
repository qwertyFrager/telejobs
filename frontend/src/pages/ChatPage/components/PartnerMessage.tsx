import { Avatar } from '@/shared/Avatar';

const PartnerMessage = () => {
  return (
    <div className="flex items-end gap-2 my-1 text-xs">
      <Avatar src="https://i.pravatar.cc/300" className="w-[18px] h-[18px] rounded" />
      <div className="flex flex-col">
        <span>Alex</span>
        <div className="shadow-border py-1 px-2.5 bg-dark-green rounded-xl flex flex-col">
          <p className="text-white">Hello, I’m developer! Wassup??</p>
          <span className="ml-auto">00:39</span>
        </div>
      </div>
    </div>
  );
};

export default PartnerMessage;
