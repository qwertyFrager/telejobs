import { twMerge } from 'tailwind-merge';

interface IButtonProps extends React.HTMLProps<HTMLButtonElement> {
  value: string;
  type?: 'submit' | 'reset' | 'button';
}

export const Button = ({ value, ...props }: IButtonProps) => {
  return (
    <button
      {...props}
      className={twMerge(
        'text-main border border-main rounded-xl py-2 w-full hover:opacity-80 active:bg-main active:text-dark-green',
        props.className,
      )}
    >
      {value}
    </button>
  );
};
