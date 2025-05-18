import {useState } from "react";


import { RosterFetch, RankDistributionFetch  } from '../../globalcomponents/EffectHooks.js'
import {default as Header} from '../../globalcomponents/HeaderHomepage.js' 
import HomePageTable from './components/HomePageTable.js'
import Loading from '../../globalcomponents/Loading.js'
import RankedChart from  './components/RankDistributionCurve v2.js'
import Intro from  './components/Intro.js'

import '../../styles/HomePageStyle.css'


export default function HomePage() {

  const [meta, setMeta] = useState(null);
  const [rankDistribution, setRankDistribution] = useState(null);

  RosterFetch(setMeta)
  RankDistributionFetch(setRankDistribution)

  console.log(meta)

    return (
        <>
          <Header classID={'homepage-header-overlay'} />
          <Intro />
          { 
            meta === null || rankDistribution === null ? (<Loading />)
            : ( <div className="homepage-container">
                  <RankedChart rankDistribution={rankDistribution} />
                  <HomePageTable meta={meta}/>
                </div>
              )
          }
        </> 
    );


}


