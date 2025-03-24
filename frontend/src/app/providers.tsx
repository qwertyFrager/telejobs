export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <div
      id="root"
      className="text-gray"
      style={{
        // backgroundImage: `url(${Bg.src})`,
        backgroundPosition: 'center top',
        backgroundRepeat: 'no-repeat',
      }}
    >
      {children}
    </div>
  );
}
