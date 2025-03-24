'use client';
import { useState } from 'react';

import Looking from './components/Looking';

const CreateJobPage = () => {
  const totalSteps = 5;

  const [currentStep, setCurrentStep] = useState(0);

  function nextStep() {
    if (currentStep < totalSteps) {
      setCurrentStep(currentStep + 1);
    }
  }

  return (
    <div className="px-5 min-h-screen flex flex-col relative ">
      <div className="flex gap-2.5 w-48 mt-14 mx-auto relative">
        {new Array(totalSteps).fill(0).map((_, i) => (
          <div className={`h-1.5 w-full rounded-3xl ${currentStep >= i ? 'bg-main' : 'bg-[#5EB5F733]'}`} key={i}></div>
        ))}
      </div>
      <div className="text-white mt-5">
        <Looking />
      </div>
    </div>
  );
};

export default CreateJobPage;
