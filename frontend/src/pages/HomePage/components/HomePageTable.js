import {useState} from "react";
import TablePop from "./Tablepop.js"
import TableImp from "./Tableimp.js"


export default function HomePageTable({meta}){
  const [tabActive, setTabActive] = useState('pop')

  return(
      <div className="hptable-container">
        <span className="table-topbox">
          <button className={"table-topbox-button click-enable " + (tabActive === 'pop' ? 'tab-active' : 'tab-sleep')} onClick={()=>setTabActive('pop')}> POPULARITY </button>
          <button className={"table-topbox-button click-enable " + (tabActive === 'imp' ? 'tab-active' : 'tab-sleep')} onClick={()=>setTabActive('imp')}> IMPACT </button>
        </span>
          {
           tabActive === 'pop' ? < TablePop meta={meta}/> : < TableImp meta={meta}/>
          }
      </div>

  )
}