import { Box, Container, Typography } from '@mui/material'
import React from 'react'
import { LightMode, DarkMode } from '@mui/icons-material'
import BasicModal from './Modal';
import InfoIcon from '@mui/icons-material/Info';
import { useNavigate } from 'react-router-dom';

export default function Header({ darkMode, toggleDarkMode }) {
    const navigate = useNavigate();
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    return (
        <Container id="margin-dense" margin="dense" style={{ marginTop: "25px" }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', '@media (max-width: 600px)': { flexDirection: "column", alignItems: "center" } }}>
                <Typography variant="h2" sx={{ flexGrow: 1, cursor: 'pointer' }} onClick={() => navigate("/")}>
                    Scheduler
                </Typography>


                <BasicModal open={open} handleClose={handleClose} />
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', '@media (max-width: 600px)': { flexDirection: "row", alignItems: "center" } }}>
                    <Typography variant="h6" sx={{ flexGrow: 1, cursor: 'pointer' }} onClick={toggleDarkMode}>
                        {darkMode ? (
                            <LightMode onClick={toggleDarkMode} sx={{ cursor: 'pointer' }} />
                        ) : (
                            <DarkMode onClick={toggleDarkMode} sx={{ cursor: 'pointer' }} />
                        )}
                    </Typography>
                    <Typography variant="h6" sx={{ flexGrow: 1, cursor: 'pointer', marginLeft: "35px" }} onClick={handleOpen}>
                        <InfoIcon />
                    </Typography>
                </Box>

            </Box>
        </Container>

    )
}
