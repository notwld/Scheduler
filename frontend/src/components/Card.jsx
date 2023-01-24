import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import { useNavigate } from 'react-router-dom';


export default function BasicCard({ title, description, route,isThreaded }) {
    const navigate = useNavigate();
    return (
        <Card sx={{ width: ["100%", "18rem"] }} variant="outlined">
            <CardActionArea>
                <CardContent>
                    <Typography sx={{ fontSize: [20, 30] }} color="text.secondary" gutterBottom>
                        {title}
                    </Typography>
                    <Typography variant="body2">
                        {description}
                    </Typography>
                </CardContent>
                <CardActions>
                    {/* <Button size="small" sx={{ textDecoration: "none", marginLeft: "auto" }} variant="outlined" component={RouterLink} to={route}>Try</Button> */}
                    <Button size="small" sx={{ textDecoration: "none", marginLeft: "auto" }} variant="outlined" onClick={() => navigate(route,{
                        state: {
                            isThreaded: isThreaded
                        }
                    })}>Try</Button>
                </CardActions>
            </CardActionArea>
        </Card>
    );
}