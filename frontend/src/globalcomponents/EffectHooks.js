import { useEffect }from "react";

// call the whole database
function RosterFetch(setMeta) { 
	useEffect(()=> {
    fetch('https://dotametaapp-production.up.railway.app/roster', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json',},
      }).then(response => {
        if (!response.ok) throw new Error('Network response was not ok')
        return response.json();
      }).then(data => setMeta(data)).catch(error => {console.error('Error fetching data:', error)})           
  }, [])

}

// call 1 hero
function HeroFetch(heroid, setHeroData ) {
 
	useEffect(()=> {
	    fetch(`https://dotametaapp-production.up.railway.app/hero/${heroid}`, {
	        method: 'GET',
	        headers: { 'Content-Type': 'application/json',},
	      }).then(response => {
	        if (!response.ok) throw new Error('Network response was not ok')
	        return response.json();
	      }).then(data => setHeroData(data)).catch(error => {console.error('Error fetching data:', error)})           
	 }, [heroid])

}

// call in playerbase data
function RankDistributionFetch(setRankDistribution) {
 
	useEffect(()=> {
	    fetch("https://api.opendota.com/api/distributions", {
	        method: 'GET',
	        headers: { 'Content-Type': 'application/json',},
	      }).then(response => {
	        if (!response.ok) throw new Error('Network response was not ok')
	        return response.json();
	      }).then(data => setRankDistribution(data)).catch(error => {console.error('Error fetching data:', error)})           
	 }, [])

}


export { RosterFetch, HeroFetch,  RankDistributionFetch};