import {useState} from "react";
import RosterRow from "./RosterRow.js"
import ImportImagesAll from '../../../globalcomponents/ImportImagesAll'

//imports all images
const svg_icon = ImportImagesAll(require.context('../../../styles/assets/svg', false, /\.(png|jpe?g|svg)$/));

export default function TablePop({meta}) {
  //sort for ascending/ descending and which column to sort with
  const [sortOrder, setsortOrder] = useState('asc')
  const [sortValue, setSortValue] = useState('KDA')

  //sort Logic
  const sortRoster = (sortArg) => {
    sortOrder === 'asc' ? setsortOrder('desc') : setsortOrder('asc')
    setSortValue(sortArg)
  }


   const HpTableHead =({inOrderOf, setHeaderValue,  sortingValueBy, pTag}) => {

    return(
      <td className={"hptable-head click-enable " + (sortingValueBy === setHeaderValue ? 'mark-active' : '')} onClick={()=>sortRoster(setHeaderValue)} >
        <span className="hptable-headspan">
          <p>{pTag}</p>
          <img className={ sortingValueBy !== setHeaderValue ?  'hide': null } alt='' src={inOrderOf === 'asc' ? svg_icon['chevup.svg'] : svg_icon['chevdown.svg']}/>
        </span>
      </td>
    )
  }


  return(
      <table>
          <thead className="hptable-head">
            <tr>
              <td className= "hptable-head"> Hero </td>
              <td className= "hptable-head"> Type </td>
              <HpTableHead inOrderOf={sortOrder} setHeaderValue={'KDA'} sortingValueBy={sortValue} pTag={'KDA'}/>
              <HpTableHead inOrderOf={sortOrder} setHeaderValue={'GPM'} sortingValueBy={sortValue} pTag={'GPM'} />
              <HpTableHead inOrderOf={sortOrder} setHeaderValue={'XPM'} sortingValueBy={sortValue} pTag={'XPM'} />
            </tr>
          </thead>
          <tbody>
            {
              sortOrder === 'asc' ? meta.sort((a, b) => b[sortValue] - a[sortValue])
                .map((x,i) => (
                  <RosterRow   heroDetails={[x['name'], x['hero_id'] , x['attribute'].slice(0,3) + '.png', x['KDA'], x['GPM'], x['XPM']]} rowKey={i} />
                ))  : meta.sort((a, b) => a[sortValue] - b[sortValue])
                .map((x,i) => (
                  <RosterRow   heroDetails={[x['name'], x['hero_id'] , x['attribute'].slice(0,3) + '.png', x['KDA'], x['GPM'], x['XPM']]} rowKey={i} />
                )) 
            }
          </tbody>
        </table>
    )
}