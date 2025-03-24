import { InputButton } from '@/shared/InputButton';

const Email = ({ nextStep }: { nextStep: () => void }) => {
  return (
    <>
      <div className="text-[32px] font-bold mb-5">
        Lets get
        <br />
        started
      </div>
      <p className="text-base mb-5">Confirm your Email</p>
      <div className="mb-2.5">
        <InputButton placeholder="Email" type="email" buttonText="Send Code" />
      </div>
      <InputButton placeholder="Code" className="mb-2.5" buttonText="Proceed" handleClick={nextStep} />
    </>
  );
};

export default Email;
