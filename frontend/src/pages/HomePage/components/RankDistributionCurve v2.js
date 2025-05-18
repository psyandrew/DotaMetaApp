import ImportImagesAll from '../../../globalcomponents/ImportImagesAll';
import { BarChart, Bar, XAxis, Tooltip, ResponsiveContainer } from 'recharts';
import desktopicon from '../../../styles/assets/svg/desktopicon.svg'
import medalsolid from '../../../styles/assets/svg/medalsolid.svg'


const rank_icons = ImportImagesAll(require.context('../../../styles/assets/Medals', false, /\.(webp)$/));



const BarTooltip = ({ active, payload }) => {
  if (active && payload) {

    return (
      <div  className='tooltip'>
        <img className="rank-img" alt={rank_icons[payload[0]['payload']["rank_medal"]]} src={rank_icons[payload[0]['payload']["rank_medal"] + ".webp"]} />
        <p>{payload[0].payload.rank_bracket}</p>
        <p>player count:</p>
        <p>{payload[0].payload.count}</p>
      </div>
    );
  }
  return null;
};



const RankedChart  = ({rankDistribution}) => {

   const maxCount = rankDistribution['ranks']['sum']['count']

  const rankDataPoints =  rankDistribution['ranks']['rows'].map(x => {

                            const rankcategory = x['bin_name'].toString();

                            // Map for medals based on the first digit
                            const medal = {
                              '1': 'Herald',
                              '2': 'Guardian',
                              '3': 'Crusader',
                              '4': 'Archon',
                              '5': 'Legend',
                              '6': 'Ancient',
                              '7': 'Divine'
                            }[rankcategory[0]] || 'Immortal';  // Default to 'Immortal' if not found

                            // Star based on the second digit, default to 0 if no valid star
                            const star = ['1', '2', '3', '4', '5'].includes(rankcategory[1]) ? rankcategory[1] : '';

                            return { rank_medal: `${medal}`, rank_bracket: `${medal} ${star}`, count: x['count'] };
                            });


     return(
      <div className="demographics-container">

        <div className="demographics-txt-container">
          <img className="medal-img" alt='medal-svg' src={medalsolid} />
          <p> This chart illustrates how players are grouped by rank, highlighting the percentages and relative standings within the community.
          Whether you're aiming to improve your own rank or just curious about the competitive landscape and where you fit in,
          this infographic offers a clear view of where players stand overall.</p>
        </div>
        
        <div className="rank-chart-container">
          <img className="rank-img" alt='pc-svg' src={desktopicon} />
          <p>current player count: {maxCount}</p>
          <ResponsiveContainer width="90%" height="70%" minWidth={300} >
            <BarChart data={rankDataPoints}>
              <XAxis dataKey="rank_bracket" />
              <Tooltip content={<BarTooltip/>} />
              <Bar dataKey="count" barSize={10} fill="#86c232"  />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    );
}
export default RankedChart;