import { Box, Container, Typography } from '@mui/material'
import React from 'react'
import { LightMode, DarkMode } from '@mui/icons-material'
import BasicModal from './Modal';

export default function Header({ darkMode, toggleDarkMode }) {
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    return (
        <Container id="margin-dense" margin="dense" style={{ marginTop: "25px" }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>

                <Typography variant="h2" onClick={handleOpen} sx={{ flexGrow: 1, cursor: 'pointer' }}>
                    Scheduler
                </Typography>
                <BasicModal open={open} handleClose={handleClose} />
                {darkMode ? (
                    <LightMode onClick={toggleDarkMode} sx={{ cursor: 'pointer' }} />
                ) : (
                    <DarkMode onClick={toggleDarkMode} sx={{ cursor: 'pointer' }} />
                )}

            </Box>
        </Container>

    )
}
