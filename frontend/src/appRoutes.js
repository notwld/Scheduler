import Home from "./components/Home/Home";
import FCFS from "./components/FCFS/FCFS";
import SJF from "./components/SJF/SJF";
import Priority from "./components/Priority/Priority";
import RoundRobins from "./components/RoundRobins/RoundRobins";


const app_routes = [
    {
        path: '/home',
        name: 'home',
        component: <Home/>
    },
    {
        path: '/about',
        name: 'about',
        component: <About/>
    },
    {
        path: '/fcfs',
        name: 'fcfs',
        component: <FCFS/>
    },
    {
        path: '/sjf',
        name: 'sjf',
        component: <SJF/>
    },
    {
        path: '/priority',
        name: 'priority',
        component: <Priority/>
    },
    {
        path: '/roundrobin',
        name: 'roundrobin',
        component: <RoundRobins/>
    },
   
]

export default app_routes;