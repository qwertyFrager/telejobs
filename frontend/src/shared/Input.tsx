import { twJoin } from 'tailwind-merge';

export const Input = (props: React.HTMLProps<HTMLInputElement>) => {
  return (
    <input
      {...props}
      className={twJoin('shadow-border rounded-2xl bg-dark-green text-gray text-sm px-4 h-10', props.className)}
    />
  );
};
