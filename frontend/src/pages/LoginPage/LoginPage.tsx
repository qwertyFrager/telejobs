'use client';

import { useState } from 'react';

import { UserType } from '@/types/Login';

import LookingClient from './components/client/LookingClient';
import LookingContractor from './components/contractor/LookingContractor';
import Email from './components/Email';
import Welcome from './components/Welcome';
import WhoAreYou from './components/WhoAreYou';

const LoginPage = () => {
  const totalSteps = 5;

  const [userType, setUserType] = useState<UserType>();

  const [currentStep, setCurrentStep] = useState(0);

  function nextStep() {
    if (currentStep < totalSteps) {
      setCurrentStep(currentStep + 1);
    }
  }

  return (
    <div className="px-5 min-h-screen flex flex-col relative ">
      <div className="flex gap-2.5 w-48 mt-14 mx-auto absolute left-1/2 -translate-x-1/2">
        {new Array(totalSteps).fill(0).map((_, i) => (
          <div className={`h-1.5 w-full rounded-3xl ${currentStep >= i ? 'bg-main' : 'bg-[#5EB5F733]'}`} key={i}></div>
        ))}
      </div>
      <div className="my-auto text-white">
        {currentStep === 0 && <Welcome nextStep={nextStep} />}
        {currentStep === 1 && <Email nextStep={nextStep} />}
        {currentStep === 2 && <WhoAreYou nextStep={nextStep} setUserType={setUserType} />}
        {currentStep === 3 && userType === UserType.Client && (
          <LookingClient
            nextStep={nextStep}
            //  setUserType={setUserType}
          />
        )}
        {currentStep === 3 && userType === UserType.Contrator && (
          <LookingContractor
            nextStep={nextStep}
            //  nextStep={nextStep} setUserType={setUserType}
          />
        )}
        {/* {currentStep === 4 && userType === UserType.Client && (
          <LookingClient
          //  nextStep={nextStep} setUserType={setUserType}
          />
        )}
        {currentStep === 4 && userType === UserType.Contrator && (
          <LookingContractor
          //  nextStep={nextStep} setUserType={setUserType}
          />
        )}
        {/* {currentStep === 5 && userType === UserType.Client && (
          <LookingClient
          //  nextStep={nextStep} setUserType={setUserType}
          />
        )}
        {currentStep === 5 && userType === UserType.Contrator && (
          <LookingContractor
          //  nextStep={nextStep} setUserType={setUserType}
          />
        )}
        {currentStep === 6 && userType === UserType.Client && (
          <LookingClient
          //  nextStep={nextStep} setUserType={setUserType}
          />
        )} */}
        {/* {currentStep === 6 && userType === UserType.Contrator && (
          <LookingContractor
          //  nextStep={nextStep} setUserType={setUserType}
          />
        )} */}
      </div>
    </div>
  );
};
export default LoginPage;
