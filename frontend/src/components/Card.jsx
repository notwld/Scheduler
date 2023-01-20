import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import { Link as RouterLink } from 'react-router-dom'



export default function BasicCard({title, description,route}) {
  return (
    <Card sx={{ width: "18rem" }} variant="outlined">
        <CardActionArea>
      <CardContent>
        <Typography sx={{ fontSize: 30 }} color="text.secondary" gutterBottom>
         {title}
        </Typography>
        
        <Typography variant="body2">
            {description}
        </Typography>
      </CardContent>
      <CardActions>
        {/* <RouterLink to={route} style={{textDecoration:"none", marginLeft:"auto"}} >
        <Button size="small" variant="outlined">Try</Button>
        </RouterLink> */}
        <Button size="small" sx={{textDecoration:"none", marginLeft:"auto"}} variant="outlined" component={RouterLink} to={route}>Try</Button>
      </CardActions>
      </CardActionArea>
    </Card>
  );
}