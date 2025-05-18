import ImportImagesAll from '../../../globalcomponents/ImportImagesAll'

const attribute_icon = ImportImagesAll(require.context('../../../styles/assets', false, /\.(png|jpe?g|svg)$/));

const hero_icon = ImportImagesAll(require.context('../../../styles/assets/hero_icons', false, /\.(png|jpe?g|svg)$/));



export default function RosterRow ({heroDetails, rowKey }) {

    return(
      <tr className={"hptable-row " + (rowKey % 2 === 0 ? 'evencolor' : 'oddcolor')}>
        <td>
          <span className="hptable-row-1" onClick={() => window.location.href='/hero/' + heroDetails[1]}>
            <img className="hero-icon" alt={hero_icon[heroDetails[1] + '.jpeg']} src={hero_icon[heroDetails[1] + '.jpeg']}/>
            <p> {heroDetails[0]} </p>
          </span>
        </td>
        <td> <img className="attr-icon" alt='hero attribute' src={attribute_icon[heroDetails[2]]}/></td>
        <td> <p className="row-numbers ">  {heroDetails[3]} </p></td>
        <td> <p className="row-numbers">  {heroDetails[4]}  </p></td>
        <td> <p className="row-numbers">  {heroDetails[5]} </p></td>
      </tr>
    )
  }
