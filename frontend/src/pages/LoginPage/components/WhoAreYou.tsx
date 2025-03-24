import { Dispatch, SetStateAction, useEffect, useState } from 'react';

import { Input } from '@/shared/Input';
import { ITab, Tabs } from '@/shared/Tabs';
import { UserType } from '@/types/Login';

const WhoAreYou = ({
  nextStep,
  setUserType,
}: {
  nextStep: () => void;
  setUserType: Dispatch<SetStateAction<UserType | undefined>>;
}) => {
  const [tabs, setTabs] = useState<
    {
      id: UserType;
      title: string;
      active?: boolean;
    }[]
  >([
    {
      id: UserType.Client,
      title: 'Client',
      active: true,
    },
    { id: UserType.Contrator, title: 'Contrator' },
  ]);

  useEffect(() => {
    setUserType(tabs.find((t) => t.active)?.id);
  }, [tabs, setUserType]);

  return (
    <>
      <div className="text-[32px] font-bold mb-5">Who are you?</div>
      <Tabs
        tabs={tabs}
        setTabs={setTabs as Dispatch<SetStateAction<ITab[]>>}
        className="mb-5"
        activeTabClassName="bg-dirty-green text-white"
        tabClassName="bg-dark-green text-gray"
      />
      <div className="h-32">
        {tabs.find((t) => t.active)?.id === UserType.Client && (
          <>
            <p className="text-base mb-5">
              An employer or business looking to hire talent — from full-time employees to freelancers for specific
              projects. You bring the opportunities!
            </p>

            <Input placeholder="Your Name" className="mb-5 w-full" />
            <Input placeholder="Company Name" className="mb-5 w-full" />
            <button
              className="ml-auto bg-dark-green text-gray text-sm rounded-xl py-2 px-3 shadow-greenBorder flex items-center gap-2"
              onClick={nextStep}
            >
              Proceed
            </button>
          </>
        )}
        {tabs.find((t) => t.active)?.id === UserType.Contrator && (
          <>
            <p className="text-base mb-5">
              A freelancer or job candidate ready to work — whether for a single project or a full-time role. You bring
              the skills!
            </p>

            <Input placeholder="Your Name" className="mb-5 w-full" />
            <button
              className="ml-auto bg-dark-green text-gray text-sm rounded-xl py-2 px-3 shadow-greenBorder flex items-center gap-2"
              onClick={nextStep}
            >
              Proceed
            </button>
          </>
        )}
      </div>
    </>
  );
};

export default WhoAreYou;
