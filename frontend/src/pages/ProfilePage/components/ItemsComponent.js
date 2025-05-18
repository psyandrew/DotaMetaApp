export default function ItemsComponent({data}){
  return(
      <div className="card-section">
        <span className="card-header">
          <h1>ITEMS</h1>
        </span>
        <div className="cards-container">
        {
          data.map((x)=>(
            <div className="item-cards">
              <img className='img-matchup' alt={x['item_name']} src={require(`../../../styles/assets/item_icons/${x['item_name'].replace(/\s/g, '').toLowerCase()}.png`)} />
              <p> {x['item_name']} </p>
              <p> win rate:</p>
              <p className="match-up-numbers"> {x['win_rate']}%</p>
            </div>
          )) 
        }
        </div>
      </div>
  )
}