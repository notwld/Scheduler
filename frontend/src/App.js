import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { useState } from 'react';
import Header from './components/Header';
import Home from './components/Home';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

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
    <BrowserRouter>
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Header toggleDarkMode={toggleDarkMode} darkMode={darkMode} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/fcfs" element={<Home />} />
        <Route path="/sjf" element={<Home />} />
        <Route path="/roundrobins" element={<Home />} />
        <Route path="/priority" element={<Home />} />
      </Routes>
    </ThemeProvider>
    </BrowserRouter>
  );
}

export default App;
