import { BarChart, Bar, XAxis, YAxis, LabelList, ResponsiveContainer} from 'recharts';



function ProfileCardComponent({data}) {

 const ratingsChartData = [ 
                            { name:'PICK%', rate: data['pick_rate'].toString()  },
                            { name:'WIN%',  rate: data['success_rate']  },
                            { name:'BAN%',  rate: data['ban_rate']    }
                          ] 


  return(
                <div className="profile-card">
                  <span className="profile-card-header" >
                    <img className='profile-card-img' alt={`${data['hero_id']}`} src={require(`../../../styles/assets/hero_icons/${data['hero_id']}.jpeg`)} />
                    <span className="profile-card-header-text">
                      <h1 className='profile-card-name'>{data['name']} </h1>
                      <p className='profile-card-attr'>{data['attribute']} Hero</p>
                      <img alt={`${data['attribute']}`}  src={require(`../../../styles/assets/${data['attribute'].slice(0,3)}.png`)}/>
                    </span>
                  </span>               
                  <ResponsiveContainer width="89%" height={200}>
                      <BarChart  data={ ratingsChartData } layout="vertical">

                        <XAxis type="number" domain={[0,100]} />
                        <YAxis dataKey="name" stroke="#86c232"  type="category"/>
                        
                        <Bar  dataKey="rate" barSize={20}  fill="#86c232"  >
                          <LabelList dataKey="rate" formatter={(value) => `${value}%`} position="right" stroke="white" />
                        </Bar>
                      </BarChart>
                  </ResponsiveContainer>

                  <div className='profile-card-impact'>
                    <span>
                      <h3 className="impact-numbers">{data['KDA']}</h3>
                      <h3>KDA</h3>
                    </span>
                    <span>
                      <h3 className="impact-numbers">{data['GPM']}</h3>
                      <h3>GPM</h3>
                    </span>
                    <span >
                      <h3 className="impact-numbers">{data['XPM']}</h3>
                      <h3>XPM</h3>
                    </span>
                  </div> 
                </div>
          );
  
} 



export default ProfileCardComponent;
