import { Dispatch, SetStateAction, useState } from 'react';

import { ITab, Tabs } from '@/shared/Tabs';
import { CoordinatorLookingType } from '@/types/Login';

interface LookingContractorData {
  id: CoordinatorLookingType;
  data: string;
}

const mockData: LookingContractorData[] = [
  {
    id: CoordinatorLookingType.Employment,
    data: 'A full-time or part-time job with a steady paycheck and long-term commitment. Ideal for those seeking stability, benefits, and career growth.',
  },
  {
    id: CoordinatorLookingType.Freelance,
    data: 'Flexible, project-based work on your terms. Perfect for those who value independence, diverse projects, and the freedom to choose when and where to work.',
  },
];

interface LookingContractorTab extends ITab {
  id: CoordinatorLookingType;
}

const LookingContractor = ({
  nextStep,
}: // setUserType,
{
  nextStep: () => void;
  // setUserType: Dispatch<SetStateAction<UserType | undefined>>;
}) => {
  const [tabs, setTabs] = useState<LookingContractorTab[]>([
    {
      id: CoordinatorLookingType.Employment,
      title: 'Employment',
      active: true,
    },
    {
      id: CoordinatorLookingType.Freelance,
      title: 'Freelance',
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

export default LookingContractor;
