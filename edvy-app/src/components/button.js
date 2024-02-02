import './button.css';
import signupIcon from './assets/signup-icon.svg';
import postIcon from './assets/post-icon.svg';
import React, { useState } from 'react';

export default function Button(props) {
    const [isHovered, setHovered] = useState(false);
    const buttonStyle = {
        boxShadow: isHovered ? '0px 4px 4px 0px rgba(0, 0, 0, 0.25)' : 'none',
        fontWeight: isHovered? "Bold": "inherit"
      };
    const icon = props.text === "sign-up"? signupIcon: postIcon

    return(
    <button className="sign-up-button"
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        style={buttonStyle}
    >
        {isHovered && <div className="button-icon">
            <img src={icon} alt="icon"/>
        </div>}
        <p style={buttonStyle}>{props.text}</p>
    </button>
    );
}
