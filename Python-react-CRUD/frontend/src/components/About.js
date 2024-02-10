import loremIpsum from "react-lorem-ipsum";
import React, {Fragment} from "react";

export const About = () => (
    <Fragment>
        <h1> About </h1>
        <p>{loremIpsum(300)}</p>
        <p>{loremIpsum(300)}</p>    
    </Fragment>
)