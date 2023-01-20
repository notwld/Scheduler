import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';



export default function BasicCard({title, description}) {
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
        <Button size="small">Run</Button>
      </CardActions>
      </CardActionArea>
    </Card>
  );
}