import { WalletIcon } from '@/shared/icons/WalletIcon';

const Welcome = ({ nextStep }: { nextStep: () => void }) => {
  return (
    <>
      <div className="text-[32px] font-bold mb-5">
        Gm! <br />
        Welcome to <br /> Engage<span className="text-main">WORK</span>
      </div>
      <p className="text-base mb-5">This is the first mini app that combines jobs and freelance in web3!</p>
      <p className="text-base mb-5">Please, Connect your TON wallet to proceed</p>
      <button
        className="bg-dark-green text-main text-sm rounded-xl py-2 px-3 shadow-greenBorder flex items-center gap-2"
        onClick={nextStep}
      >
        <WalletIcon /> Connect Wallet
      </button>
    </>
  );
};

export default Welcome;
