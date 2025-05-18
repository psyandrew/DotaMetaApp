import { BarChart, Bar, XAxis, YAxis, LabelList, Legend,  ResponsiveContainer} from 'recharts';


export default function FacetsComponent({data}){
  
  console.log(data)

  return(
      <div className="chart-card">
        <span className="card-header">
          <h1>FACETS</h1>
        </span>
          <ResponsiveContainer width="90%" height="90%">
            <BarChart data={data} width="100" height={200} layout="vertical">>
              <YAxis dataKey="facet_name"  formatter={(value) => `${value.trim()}`}  width={120} stroke="#86c232"  type="category"/>
              <XAxis  type="number" domain={[0,100]} />
              <Bar   dataKey="win_rate" barSize={15}  fill="#86c232"  >
                <LabelList dataKey="win_rate" formatter={(value) => `${value}%`} position="right" stroke="white" />
              </Bar>
              <Bar   dataKey="pick_rate" barSize={15}  fill="#fffc52"  >
                <LabelList dataKey="pick_rate" formatter={(value) => `${value}%`} position="right" stroke="white" />
              </Bar>
              <Legend formatter={(value) => `${value.replace('_'," ")}`}/>
            </BarChart>
          </ResponsiveContainer>
      </div>
  )
}