'use client';

import { useState } from 'react';

import { PageWrapper } from '@/shared/PageWrapper';
import { ITab, Tabs } from '@/shared/Tabs';
import HiringItem from './components/HiringItem';
import InputModal from './components/InputModal';

const MainPage = () => {
  const [tabs, setTabs] = useState<ITab[]>([
    { id: 'freelance', title: 'Freelance', active: true },
    { id: 'hiring', title: 'Hiring' },
  ]);

  return (
    <PageWrapper>
      <Tabs tabs={tabs} setTabs={setTabs} />
      <InputModal />

      <div className="flex justify-between items-center text-xs mb-2.5 mt-5">
        <span>9,123 total</span>
        <span>
          Sort by: <span className="text-main">Wage Decay</span>
        </span>
      </div>
      <div className="flex flex-col gap-2.5">
        <HiringItem
          person={{
            lastSeen: '4 September',
            title: 'Frontend Developer',
            rate: '$1,000',
            age: '25',
            city: 'New York',
            experince: '5 years',
            image: 'https://i.pravatar.cc/300',
            activityType: 'Hiring',
          }}
        />
      </div>
    </PageWrapper>
  );
};

export default MainPage;
