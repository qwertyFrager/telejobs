import { Dispatch, SetStateAction } from 'react';
import { twMerge } from 'tailwind-merge';

export interface ITab {
  title: string;
  id: string;
  active?: boolean;
}

export const Tabs = ({
  tabs,
  className,
  activeTabClassName,
  tabClassName,
  setTabs,
}: {
  tabs: ITab[];
  setTabs: Dispatch<SetStateAction<ITab[]>>;
  className?: string;
  activeTabClassName?: string;
  tabClassName?: string;
}) => {
  // const [tabs, setTabs] = useState<ITab[]>([
  //   { id: 'freelance', title: 'Freelance', active: true },
  //   { id: 'hiring', title: 'Hiring' },
  // ]);
  const handleTabClick = (item: ITab) => {
    setTabs((prev) => prev.map((tab) => ({ ...tab, active: tab.id === item.id })));
  };

  return (
    <div
      className={twMerge(`font-bold text-sm text-gray grid p-1 rounded-2xl shadow-border bg-dark-green`, className)}
      style={{
        gridTemplateColumns: `repeat(${tabs.length}, minmax(0, 1fr))`,
      }}
    >
      {tabs.map((item) => (
        <button
          className={twMerge(
            tabClassName,
            item.active && `bg-main text-dark ${activeTabClassName}`,
            'inline-block text-center py-1 rounded-xl',
          )}
          key={item.id}
          onClick={() => handleTabClick(item)}
        >
          {item.title}
        </button>
      ))}
    </div>
  );
};
