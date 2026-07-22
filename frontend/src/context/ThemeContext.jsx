import React, { createContext, useContext, useState, useEffect } from 'react';

const ThemeContext = createContext();

export const THEMES = [
  { id: 'dark-blue', name: 'Dark Blue (Neon)', label: 'Dark Blue' },
  { id: 'white', name: 'Pure White', label: 'White' },
];

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(() => {
    const saved = localStorage.getItem('insightai_theme');
    return (saved === 'dark-blue' || saved === 'white') ? saved : 'dark-blue';
  });

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('insightai_theme', theme);
  }, [theme]);

  const changeTheme = (newTheme) => {
    if (THEMES.some((t) => t.id === newTheme)) {
      setTheme(newTheme);
    }
  };

  return (
    <ThemeContext.Provider value={{ theme, changeTheme, themes: THEMES }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};
