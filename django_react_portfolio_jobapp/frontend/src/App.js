import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './index.css';

const themes = {
  netflix: {
    backgroundColor: '#141414',
    color: '#E50914',
  },
  amazon: {
    backgroundColor: '#131921',
    color: '#FF9900',
  },
  microsoft: {
    backgroundColor: '#F25022',
    color: '#7FBA00',
  },
  google: {
    backgroundColor: '#4285F4',
    color: '#34A853',
  },
};

function PortfolioPage() {
  return (
    <div className="p-8">
      <h1 className="text-4xl font-bold mb-4">Portfolio Overview</h1>
      <p>Select a theme from the dropdown in the navigation to view specific portfolio pages.</p>
    </div>
  );
}

function NetflixPortfolio() {
  return (
    <div style={{ minHeight: '100vh', padding: '2rem', backgroundColor: '#141414', color: '#E50914' }}>
      <h1 className="text-4xl font-bold mb-4">Netflix Theme Portfolio</h1>
      <p>This is a sample portfolio page styled with the Netflix theme.</p>
    </div>
  );
}

function AmazonPortfolio() {
  return (
    <div style={{ minHeight: '100vh', padding: '2rem', backgroundColor: '#131921', color: '#FF9900' }}>
      <h1 className="text-4xl font-bold mb-4">Amazon Theme Portfolio</h1>
      <p>This is a sample portfolio page styled with the Amazon theme.</p>
    </div>
  );
}

function MicrosoftPortfolio() {
  return (
    <div style={{ minHeight: '100vh', padding: '2rem', backgroundColor: '#F25022', color: '#7FBA00' }}>
      <h1 className="text-4xl font-bold mb-4">Microsoft Theme Portfolio</h1>
      <p>This is a sample portfolio page styled with the Microsoft theme.</p>
    </div>
  );
}

function GooglePortfolio() {
  return (
    <div style={{ minHeight: '100vh', padding: '2rem', backgroundColor: '#4285F4', color: '#34A853' }}>
      <h1 className="text-4xl font-bold mb-4">Google Theme Portfolio</h1>
      <p>This is a sample portfolio page styled with the Google theme.</p>
    </div>
  );
}

function JobScraperPage() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    fetch('/api/jobscraper/scrape/')
      .then((response) => response.json())
      .then((data) => setJobs(data.jobs))
      .catch((error) => console.error('Error fetching jobs:', error));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-4xl font-bold mb-4">Job Scraper</h1>
      {jobs.length === 0 ? (
        <p>Loading job listings...</p>
      ) : (
        <table className="min-w-full border border-gray-300">
          <thead>
            <tr className="bg-gray-200">
              <th className="border border-gray-300 px-4 py-2">Job Role</th>
              <th className="border border-gray-300 px-4 py-2">Company Name</th>
              <th className="border border-gray-300 px-4 py-2">Hiring Posted Date</th>
              <th className="border border-gray-300 px-4 py-2">Location</th>
              <th className="border border-gray-300 px-4 py-2">Apply Link</th>
            </tr>
          </thead>
          <tbody>
            {jobs.map((job, index) => (
              <tr key={index} className="odd:bg-white even:bg-gray-100">
                <td className="border border-gray-300 px-4 py-2">{job.job_role}</td>
                <td className="border border-gray-300 px-4 py-2">{job.company_name}</td>
                <td className="border border-gray-300 px-4 py-2">{job.hiring_posted_date}</td>
                <td className="border border-gray-300 px-4 py-2">{job.location}</td>
                <td className="border border-gray-300 px-4 py-2">
                  <a href={job.apply_link} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                    Apply
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

function MyCodesPage() {
  return (
    <div className="p-8">
      <h1 className="text-4xl font-bold mb-4">My Codes</h1>
      <p>This page will display your code snippets or projects.</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <nav className="bg-gray-800 p-4 text-white flex space-x-4">
        <div className="relative group">
          <button className="hover:underline focus:outline-none">
            My Portfolio
          </button>
          <div className="absolute hidden group-hover:block bg-gray-700 mt-1 rounded shadow-lg z-10">
            <Link to="/" className="block px-4 py-2 hover:bg-gray-600">Overview</Link>
            <Link to="/portfolio/netflix" className="block px-4 py-2 hover:bg-gray-600">Netflix Theme</Link>
            <Link to="/portfolio/amazon" className="block px-4 py-2 hover:bg-gray-600">Amazon Theme</Link>
            <Link to="/portfolio/microsoft" className="block px-4 py-2 hover:bg-gray-600">Microsoft Theme</Link>
            <Link to="/portfolio/google" className="block px-4 py-2 hover:bg-gray-600">Google Theme</Link>
          </div>
        </div>
        <Link to="/jobscraper" className="hover:underline">Job Scraper</Link>
        <Link to="/mycodes" className="hover:underline">My Codes</Link>
      </nav>
      <Routes>
        <Route path="/" element={<PortfolioPage />} />
        <Route path="/portfolio/netflix" element={<NetflixPortfolio />} />
        <Route path="/portfolio/amazon" element={<AmazonPortfolio />} />
        <Route path="/portfolio/microsoft" element={<MicrosoftPortfolio />} />
        <Route path="/portfolio/google" element={<GooglePortfolio />} />
        <Route path="/jobscraper" element={<JobScraperPage />} />
        <Route path="/mycodes" element={<MyCodesPage />} />
      </Routes>
    </Router>
  );
}

export default App;
