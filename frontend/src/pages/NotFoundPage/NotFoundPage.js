import {default as Header} from '../../globalcomponents/HeaderProfile.js'
import pudge404 from '../../styles/assets/pudge404.png'

import '../../styles/NotFoundPageStyle.css'




function NotFoundPage() {

  return (
    <div className="body-404">
      <p className='txt-404'><strong>4<img src={pudge404}  className='pudge-404'/>4</strong></p>
      <p className='txt-pnf'>Page Not Found</p>
      <button className='buton-404' onClick={() => window.location.href = '/'}> HOME </button>  
    </div> 
    );
  
} 



export default NotFoundPage;