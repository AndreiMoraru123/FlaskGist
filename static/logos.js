// Badges for programming languages

const logoMap = {
  js: { name: 'JavaScript', color: '#f7df1e' },
  py: { name: 'Python', color: '#3572A5' },
  html: { name: 'HTML', color: '#e34c26' },
  css: { name: 'CSS', color: '#563d7c' },
  java: { name: 'Java', color: '#b07219' },
  c: { name: 'C', color: '#555' },
  cs: { name: 'C#', color: '#178600' },
  cpp: { name: 'C++', color: '#f34b7d' },
  rb: { name: 'Ruby', color: '#701516' },
  go: { name: 'Go', color: '#375eab' },
  swift: { name: 'Swift', color: '#ffac45' },
  sh: { name: 'Shell', color: '#89e051' },
  rs: { name: 'Rust', color: '#dea584' },
  hs: { name: 'Haskell', color: '#5e5086' },
  lua: { name: 'Lua', color: '#000080' },
  erl: { name: 'Erlang', color: '#b83998' },
  ex: { name: 'Elixir', color: '#6e4a7e' },
  ps1: { name: 'PowerShell', color: '#012456' }
};

const Logo = ({ fileExt }) => {
  const { name, color } = logoMap[fileExt];

  return (
    <span className="tag">
      <span style={{ backgroundColor: color }} className="square"></span>
      {name}
    </span>
  );
};

export default Logo;
