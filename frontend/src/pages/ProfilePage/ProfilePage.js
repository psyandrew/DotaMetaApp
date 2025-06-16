import { useState } from "react";
import { useParams } from 'react-router-dom';
import {default as Header} from '../../globalcomponents/HeaderProfile.js'
import Loading from '../../globalcomponents/Loading.js'


import { HeroFetch } from '../../globalcomponents/FetchComponents.js'

import  FacetsComponent  from './components/FacetsComponent.js'
import  LaningComponent  from './components/LaningComponent.js'
import  ItemsComponent  from './components/ItemsComponent.js'
import  GoodMatchUpsComponent  from './components/GoodMatchUpsComponent.js'
import  BadMatchUpsComponent  from './components/BadMatchUpsComponent.js'
import  ProfileCardComponent  from './components/ProfileCardComponent.js'

import '../../styles/ProfilePageStyle.css'




function Profile() {
  const { heroid } = useParams();
  const [heroData, setHeroData] = useState(null);
  

  HeroFetch(heroid, setHeroData)
  
  //console.log(heroData)

  return (
    <div className="profile-body">
      <Header classID={'hero-profile-overlay'}/>  
      {
       heroData === null ? (<Loading/>)
      : (
          <div className="profile">
            <div className="profile-container">
              <ProfileCardComponent data={heroData} />
              <div className="chart-wrap">
                <FacetsComponent data={heroData['facets']} />
                <LaningComponent data={heroData['laning']} />
              </div>
              <GoodMatchUpsComponent data={heroData['good_matchup']} />
              <BadMatchUpsComponent data={heroData['bad_matchup']} />  
              <ItemsComponent data={heroData['items']} />
              <button onClick={() => window.location.href='/'}>HOME</button>  
            </div>
          </div>
          )
      }
    </div> 
    );
  
} 



export default Profile;
