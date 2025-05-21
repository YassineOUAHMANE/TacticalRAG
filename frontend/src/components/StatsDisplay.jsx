import React, { useEffect, useState } from 'react';
import { fetchStats } from '../../frontend/src/api/api';

const StatsDisplay = () => {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    const getStats = async () => {
      const data = await fetchStats();
      setStats(data);
    };
    getStats();
  }, []);

  if (!stats) return <div>Chargement des statistiques...</div>;

  return (
    <div>
      <h3>Statistiques</h3>
      <pre>{JSON.stringify(stats, null, 2)}</pre>
    </div>
  );
};

export default StatsDisplay;
