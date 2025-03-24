'use client';
import { useState } from 'react';

import { SearchIcon } from '@/shared/icons/primary/SearchIcon';
import { PageWrapper } from '@/shared/PageWrapper';
import { ITab, Tabs } from '@/shared/Tabs';
import ChatItem from './components/ChatItem';

const ChatsPage = () => {
  const [tabs, setTabs] = useState<ITab[]>([
    { id: 'freelance', title: 'Freelance', active: true },
    { id: 'hiring', title: 'Hiring' },
  ]);
  return (
    <PageWrapper>
      <div className="h-screen overflow-hidden">
        <Tabs tabs={tabs} setTabs={setTabs} className="mb-5" />
        <div className="flex justify-center items-center relative mb-5">
          <span className="text-white font-bold text-lg">Chats</span>
          <button className="absolute right-0">
            <SearchIcon />
          </button>
        </div>
        <div className="flex flex-col gap-5 overflow-scroll h-full">
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
          <ChatItem />
        </div>
      </div>
    </PageWrapper>
  );
};

export default ChatsPage;
