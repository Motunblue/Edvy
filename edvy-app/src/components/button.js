import './button.css';
import signupIcon from './assets/signup-icon.svg';
import postIcon from './assets/post-icon.svg';
import React, { useState } from 'react';
//import { useHistory } from 'react-router-dom';

export default function Button(props) {
    const [isHovered, setHovered] = useState(false);
    const buttonStyle = {
        boxShadow: isHovered ? '0px 4px 4px 0px rgba(0, 0, 0, 0.25)' : 'none',
        fontWeight: isHovered? "Bold": "inherit"
      };
    const icon = props.text === "sign-up"? signupIcon: postIcon
    //const handleButtonClick = () => {
        // Navigate to another route when the button is clicked
        //history.push('/your/destination/route');
    //};

    return(
    <button
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        style={buttonStyle}
        //onClick={handleButtonClick}
    >
        {isHovered && <div className="button-icon">
            <img src={icon} alt="icon"/>
        </div>}
        <p style={buttonStyle}>{props.text}</p>
    </button>
    );
}
