import { AttachemntIcon } from '@/shared/icons/AttachemntIcon';
import { SendMessageIcon } from '@/shared/icons/SendMessageIcon';
import { useState } from 'react';
import { twMerge } from 'tailwind-merge';

const ChatInput = () => {
  const [value, setValue] = useState<string>();

  return (
    <div className="py-3 px-5 bg-dark-green border-t border-dirty-green flex items-start gap-4">
      <button>
        <AttachemntIcon />
      </button>
      <textarea
        className="bg-dark-green outline-none"
        style={{
          width: '100%',
        }}
        placeholder="Message..."
        value={value}
        onChange={(e) => setValue(e.target.value)}
      ></textarea>
      <button disabled={value?.length === 0}>
        <SendMessageIcon
          fill={value?.length === 0 ? '#768C9E' : '#5EB5F7'}
          className={twMerge('transition-all', value?.length === 0 ? 'rotate-90' : '')}
        />
      </button>
    </div>
  );
};

export default ChatInput;
