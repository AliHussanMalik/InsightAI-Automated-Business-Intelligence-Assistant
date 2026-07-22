import React from 'react';
import { Palette } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';

export const ThemeSelector = () => {
  const { theme, changeTheme, themes } = useTheme();

  return (
    <div className="theme-selector">
      <Palette size={16} className="theme-selector-icon" />
      <select
        className="custom-select"
        value={theme}
        onChange={(e) => changeTheme(e.target.value)}
        aria-label="Select Application Theme"
      >
        {themes.map((t) => (
          <option key={t.id} value={t.id}>
            {t.name}
          </option>
        ))}
      </select>
    </div>
  );
};
