import { BottomMenu } from '@/components/BottomMenu';
import { Header } from '@/components/Header';

export const PageWrapper = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="h-screen overflow-hidden">
      <Header />
        <div className="max-w-md px-5 m-auto">{children}</div>
      <BottomMenu />
    </div>
  );
};
