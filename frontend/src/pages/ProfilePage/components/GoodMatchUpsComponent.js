export default function GoodMatchUpsComponent({data}){
  return(
      <div className="card-section">
        <span className="card-header"> 
          <h1>Good Match ups</h1>
        </span>
        <div className="cards-container">
          {
            data.map((x)=>(
              <div className="matchup-cards">
                <img onClick={() => window.location.href='/hero/' + x['counters'].toLowerCase().replace(' ', '')} className='img-matchup' alt="placeholder" src={require(`../../../styles/assets/hero_icons/${x['counters'].replace(/\s/g, '').toLowerCase()}.jpeg`)} />
                <p className='card-name' onClick={() => window.location.href='/hero/' + x['counters'].toLowerCase().replace(' ', '')}>{x['counters']}</p>
                <p> win rate:</p>
                <p className="match-up-numbers">{x['win_rate']}%</p>
              </div>
            )) 
          }
        </div>
      </div>
  )
}