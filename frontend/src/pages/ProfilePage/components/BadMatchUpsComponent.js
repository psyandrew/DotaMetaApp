export default function BadMatchUpsComponent({data}){
  


  

  return(
      <div className="card-section">
        <span className="card-header"> 
          <h1>Bad Match ups</h1>
        </span>
        <div className="cards-container">
        {
          data.map((x)=>(
            <div className="matchup-cards" >
              <img onClick={() => window.location.href='http://localhost:3000/hero/' + x['countered'].toLowerCase().replace(' ', '')} className='img-matchup' alt="placeholder" src={require(`../../../styles/assets/hero_icons/${x['countered'].replace(/\s/g, '').toLowerCase()}.jpeg`)} />
              <p className='card-name' onClick={() => window.location.href='http://localhost:3000/hero/' + x['countered'].toLowerCase().replace(' ', '')}>{x['countered']}</p>
              <p> win rate:</p>
              <p className="match-up-numbers">{x['win_rate']}%</p>
            </div>
          )) 
        }
        </div>
      </div>
  )
}