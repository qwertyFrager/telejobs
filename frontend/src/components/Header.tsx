import Image from 'next/image';

// import logo from '@/public/images/logo.svg';

export const Header = () => {
  return (
    <div className="flex items-center pt-6 justify-center mb-3">
      {/* <Image src={logo} alt="logo" width={24} height={24} /> */}
      <span className="text-xl ml-3 text-white">
        Tele<span className="text-main font-bold ">Jobs</span>
      </span>
    </div>
  );
};
