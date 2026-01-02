import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import OctofitLogo from './components/OctofitLogo';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <OctofitLogo />
          <h1 style={{ margin: 0 }}>Octofit Tracker</h1>
        </header>
        <nav className="nav">
          <Link className="App-link" to="/activities">Activities</Link>
          <Link className="App-link" to="/leaderboard">Leaderboard</Link>
          <Link className="App-link" to="/teams">Teams</Link>
          <Link className="App-link" to="/users">Users</Link>
          <Link className="App-link" to="/workouts">Workouts</Link>
        </nav>
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
