import './offer_card.css';
import React, { useState } from 'react';
import connectIcon from './assets/connect-icon.svg';
import collaborateIcon from './assets/collaborate-icon.svg';
import optimizeIcon from './assets/optimize-icon.svg';

export default function Offers(props) {
    const [isHovered, setHovered] = useState(false);
    const cardStyle = {
        boxShadow: isHovered ? '0px 4px 10px 0px rgba(0, 0, 0, 0.25)' : '0px 0px 4px 0px rgba(0, 0, 0, 0.25)',
        background: isHovered? "#FCB276": "inherit"
    };
    const iconStyle  = {
        background: isHovered ? '#7BBBFB': '#DBEDFF',
        boxShadow: isHovered ? '0px 4px 10px 0px rgba(0, 0, 0, 0.25)': null
    };

    let icon = null;
    if (props.header === "Connect") {
        icon = connectIcon;
    } else if (props.header === "Collaborate") {
        icon = collaborateIcon;
    } else {
        icon = optimizeIcon;
    }

    return(
    <div
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        className='offer-card'
        style={cardStyle}
    >
        <div className='offer-icon' style={iconStyle}>
            <img src={icon} alt='connect'/>
        </div>
        <p>{props.header}</p>
        <p className='desc'>{props.desc}</p>
    </div>
    );
}
