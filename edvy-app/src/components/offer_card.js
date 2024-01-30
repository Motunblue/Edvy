import './offer_card.css';
import React, { useState } from 'react';
import connectIcon from './assets/connect-icon.svg';

export default function Offers(props) {
    const [isHovered, setHovered] = useState(false);
    const buttonStyle = {
        boxShadow: isHovered ? '0px 4px 4px 0px rgba(0, 0, 0, 0.25)' : 'none',
        fontWeight: isHovered? "Bold": "inherit"
      };
    //const icon = props.text === "sign-up"? signupIcon: postIcon

    return(
    <div
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        className='offer-card'
    >
        <div className='offer-icon'><img src={connectIcon} alt='connect'/></div>
        <p>{props.header}</p>
        <p>{props.desc}</p>
    </div>
    );
}
