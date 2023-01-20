import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { useState } from 'react';
import Header from './components/Header';

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const darkTheme = createTheme({
    palette: {
      mode: darkMode ? 'dark' : 'light',
    },
  });
  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Header toggleDarkMode={toggleDarkMode} />
    </ThemeProvider>
  );
}

export default App;
