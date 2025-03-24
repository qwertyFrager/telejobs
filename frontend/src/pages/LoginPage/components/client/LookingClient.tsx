import { Dispatch, SetStateAction, useState } from 'react';

import { ITab, Tabs } from '@/shared/Tabs';
import { CooperationFormType } from '@/types/Login';

interface CooperatingFormData {
  id: CooperationFormType;
  data: string;
}

const mockData: CooperatingFormData[] = [
  {
    id: CooperationFormType.LongTerm,
    data: 'A lasting collaboration — from ongoing freelance projects to full-time employment. Perfect for those seeking stable relationships and consistent work.',
  },
  {
    id: CooperationFormType.OneTime,
    data: 'A single task or project. Great for quick solutions to specific needs, with no future commitments.',
  },
];

interface CooperatingFormTab extends ITab {
  id: CooperationFormType;
}

const LookingClient = ({
  nextStep,
}: // setUserType,
{
  nextStep: () => void;
  // setUserType: Dispatch<SetStateAction<UserType | undefined>>;
}) => {
  const [tabs, setTabs] = useState<CooperatingFormTab[]>([
    {
      id: CooperationFormType.LongTerm,
      title: 'Long-term',
      active: true,
    },
    {
      id: CooperationFormType.OneTime,
      title: 'One-time',
    },
  ]);

  return (
    <div className="flex flex-col">
      <div className="text-[32px] font-bold mb-5">What cooperation are you looking for?</div>
      <Tabs
        tabs={tabs}
        setTabs={setTabs as Dispatch<SetStateAction<ITab[]>>}
        activeTabClassName="bg-dirty-green text-white"
        tabClassName="bg-dark-green text-gray"
        className="mb-5"
      />
      <p className="text-base mb-5 text-gray">
        {mockData.find((item) => item.id === tabs.find((item) => item.active)?.id)?.data}
      </p>

      <button
        className="ml-auto bg-dark-green text-gray text-sm rounded-xl py-2 px-3 shadow-greenBorder flex items-center gap-2"
        onClick={nextStep}
      >
        Proceed
      </button>
      <div className="flex justify-center">
        <button onClick={nextStep} className="text-gray">
          Skip
        </button>
      </div>
    </div>
  );
};

export default LookingClient;
