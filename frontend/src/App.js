import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { useState } from 'react';
import Header from './components/Header';
import Home from './components/Home';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import FCFS from './components/FCFS'
import Priority from './components/Priority'
import SJF from './components/SJF'
import RoundRobins from './components/RoundRobins'
import Output from './components/Output';


function App() {
  const [darkMode, setDarkMode] = useState(true);
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
        <Route path="/fcfs" element={<FCFS />} />
        <Route path="/sjf" element={<SJF />} />
        <Route path="/roundrobins" element={<RoundRobins />} />
        <Route path="/priority" element={<Priority />} />
        <Route path="/output" element={<Output />} />
        <Route path="/fcfs-threaded" element={<FCFS />} />
        <Route path="/sjf-threaded" element={<SJF />} />
        <Route path="/roundrobins-threaded" element={<RoundRobins />} />
        <Route path="/priority-threaded" element={<Priority />} />
        <Route path="/output-threaded" element={<Output />} />
      </Routes>
    </ThemeProvider>
    </BrowserRouter>
  );
}

export default App;
