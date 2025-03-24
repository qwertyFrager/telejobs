'use client';

import Image from 'next/image';
import { useState } from 'react';
import Marquee from 'react-fast-marquee';

import logo from '@/public/images/logo.svg';
import PolygonImage from '@/public/images/main-running/polygon.png';
import TonImage from '@/public/images/main-running/ton.png';
import MainSphere from '@/public/images/main-sphere.png';
import { CheckWithBorderIcon } from '@/shared/icons/CheckWithBorderIcon';
import { PlusIcon } from '@/shared/icons/primary/PlusIcon';
import { SearchIcon } from '@/shared/icons/primary/SearchIcon';
import { PageWrapper } from '@/shared/PageWrapper';
import { ITab, Tabs } from '@/shared/Tabs';

const WorkPage = () => {
  const [topTabs, setTopTabs] = useState<ITab[]>([
    { id: 'freelance', title: 'Freelance', active: true },
    { id: 'hiring', title: 'Hiring' },
  ]);

  const [jobTabs, setJobTabs] = useState<ITab[]>([
    { id: 'active', title: 'Active', active: true },
    { id: 'draft', title: 'Draft' },
    { id: 'acrhive', title: 'Archive' },
  ]);
  return (
    <PageWrapper>
      <Tabs tabs={topTabs} setTabs={setTopTabs} />
      <div className="flex justify-center relative mt-5 mb-4">
        <span className="text-white font-bold text-lg">My jobs</span>
        <div className="ml-auto flex gap-4 absolute right-0 top-1/2 -translate-y-1/2">
          <button>
            <SearchIcon />
          </button>
          <button>
            <PlusIcon />
          </button>
        </div>
      </div>
      <Tabs
        {...{ tabs: jobTabs, setTabs: setJobTabs }}
        className="flex-nowrap"
        activeTabClassName="bg-dirty-green text-white"
      />

      <div className="mt-14">
        <Marquee className="mb-4">
          <div className="flex gap-10 mr-10">
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
            <Image src={TonImage} alt="ton" width={95} height={36} />
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
            <Image src={TonImage} alt="ton" width={95} height={36} />
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
            <Image src={TonImage} alt="ton" width={95} height={36} />
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
            <Image src={TonImage} alt="ton" width={95} height={36} />
          </div>
        </Marquee>

        <Marquee direction="right">
          <div className="flex gap-10 mr-10">
            <Image src={TonImage} alt="ton" width={95} height={36} />
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
            <Image src={TonImage} alt="ton" width={95} height={36} />
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
            <Image src={TonImage} alt="ton" width={95} height={36} />
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
            <Image src={TonImage} alt="ton" width={95} height={36} />
            <Image src={PolygonImage} alt="polygon" width={172} height={36} />
          </div>
        </Marquee>
      </div>
      <div className="absolute bottom-0 left-1/2 -translate-x-1/2 w-full flex justify-center">
        <Image src={MainSphere} alt="sphere" width={393} height={324} />
      </div>
      <div className="absolute z-10 bottom-28 left-0 w-full px-5">
        <div className="bg-dark-green rounded-2xl shadow-border p-1 pt-3.5">
          <ul className="pl-3 flex flex-col gap-3">
            <li className="flex gap-3 items-center">
              <CheckWithBorderIcon />
              <div className="flex flex-col gap-1">
                <span className="text-white text-base">{'>10,000 Web3 Professionals'}</span>
                <span className="text-gray text-xs">will see your vacancy within 30 days</span>
              </div>
            </li>
            <li className="flex gap-3 items-center">
              <Image src={logo} alt="logo" width={18} height={18} />
              <div className="flex flex-col gap-1">
                <span className="text-white text-base">{'>10 matching CV’s'}</span>
                <span className="text-gray text-xs">as soon as it’s posted</span>
              </div>
            </li>
          </ul>
          <button className="text-dark-green bg-main w-full py-3 rounded-xl mt-5">Create Job</button>
        </div>
      </div>
    </PageWrapper>
  );
};

export default WorkPage;
