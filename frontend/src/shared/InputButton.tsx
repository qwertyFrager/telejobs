import { twJoin } from 'tailwind-merge';

interface IInputButton extends React.HTMLProps<HTMLInputElement> {
  buttonText: string;
  handleClick?: () => void;
}

export const InputButton = ({ buttonText, ...props }: IInputButton & { buttonText: string }) => {
  return (
    <div className="relative h-10">
      <input
        {...props}
        className={twJoin(
          'shadow-border rounded-2xl bg-dark-green text-gray text-sm px-4 h-full w-full',
          props.className,
        )}
      />
      <button
        className="bg-dirty-green text-gray p-2 rounded-xl absolute right-1 flex items-center gap-1 top-1/2 -translate-y-1/2"
        style={{ height: 'calc(100% - 8px)' }}
        onClick={props.handleClick}
      >
        {buttonText}
      </button>
    </div>
  );
};
