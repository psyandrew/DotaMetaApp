export default function header({classID}){


  return(
    <div className="header">
      <div className='hero-profile-overlay'>
        <div className='logo' onClick={() => window.location.href='http://localhost:3000/'}>
        </div>
      </div>
    </div>
  )
}