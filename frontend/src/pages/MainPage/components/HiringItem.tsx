'use client';

import { Avatar } from '@/shared/Avatar';
import { Button } from '@/shared/Button';
import { StarIcon } from '@/shared/icons/StarIcon';

const HiringItem = ({
  person,
}: {
  person: {
    lastSeen: string;
    title: string;
    rate: string;
    age: string;
    city: string;
    experince: string;
    image: string;
    activityType: string;
  };
}) => {
  return (
    <div className="shadow-border p-2 pb-1 pt-3 rounded-2xl text-xs text-white relative">
      <div className="">
        <div className="text-gray">Last seen {person?.lastSeen}</div>
        <div className="font-bold text-base">{person?.title}</div>
        <div className="mb-2">
          {person?.rate} · {person?.age} y/o · {person?.city}
        </div>
        <span className="px-2.5 bg-[#193A1C] rounded-xl py-1">{person?.activityType}</span>

        <div className="flex flex-col mt-3">
          <span className="text-gray">Experience:</span>
          <span>{person?.experince}</span>
        </div>
      </div>
      <div className="flex flex-col gap-3 items-center absolute top-3 right-3">
        <Avatar src={person?.image} />
        <button>
          <StarIcon />
        </button>
      </div>
      <Button value="Get in touch" className="mt-3" />
    </div>
  );
};

export default HiringItem;
