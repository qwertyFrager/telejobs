import { Avatar } from '@/shared/Avatar';
import { MoreIcon } from '@/shared/icons/primary/MoreIcon';
import { SettingsIcon } from '@/shared/icons/primary/SettingsIcon';
import { PageWrapper } from '@/shared/PageWrapper';

const ProfilePage = () => {
  return (
    <PageWrapper>
      <div className="flex justify-center items-center relative mb-5">
        <span className="text-white font-bold text-lg">Alex</span>
        <button className="absolute right-0">
          <SettingsIcon />
        </button>
      </div>
      <div className="bg-dark-green shadow-border rounded-2xl px-4 py-3 mb-2.5">
        <div className="flex items-center justify-between mb-1">
          <span className="text-white text-base font-bold">MyCompany</span>
          <button className="mr-2">
            <MoreIcon />
          </button>
        </div>
        <div className="flex justify-between items-center">
          <span>Id: 113293021</span>
          <Avatar src="https://i.pravatar.cc/300" />
        </div>
        <div>
          <span>Unverified</span>
          <button className="bg-gradient-blue-pink text-white px-3 py-1 rounded-xl ml-2">Get Verified</button>
        </div>
      </div>
      <div className="bg-dark-green shadow-border rounded-2xl px-4 py-3 mb-2">
        <span>
          Subscription: <span className="text-white">None</span>
        </span>
        <ul className="mb-5 list-disc pl-4">
          <li>Benefit 1</li>
          <li>Benefit 2</li>
          <li>Benefit 3</li>
        </ul>
        <button className="bg-gradient-green-yellow text-dark-green py-3 rounded-xl w-full">Upgrade</button>
      </div>
    </PageWrapper>
  );
};

export default ProfilePage;
