import React from 'react';
import {Thumbnail, Label, Badge, Button} from 'react-bootstrap';
import {Link} from 'react-router';
import {pure} from 'recompose';
import {browserHistory} from 'react-router';
import Timestamp from './Timestamp';
import UserThumb from './UserThumb';
import Markdown from './Markdown';
 
const GenericThumbnailItem = React.createClass({render(){
    const maxHeight = {
	maxHeight:'120px',
	overflow:'hidden'
    };
    const margin = {
	marginLeft:'5px' 
    };
    const pk = this.props.id;
    const uri = this.props.uri+ pk + '/';
    const tags = this.props.tag_names.map((label,i)=>(<Label key={i} bsStyle="info" 
        style={margin}>{label}</Label>)); 
    const title = (<span><Link to={uri}>{this.props.title}</Link></span>);
    const tag=(<span>{tags}</span>);
    const footer = (<span>
		    <Timestamp title='created' datetime={this.props.created}/><br/>
		    <UserThumb id={this.props.created_by}/></span>); 
    return (
	    <Thumbnail src={this.props.image} alt={this.props.title}>
	    <div style={maxHeight}>
        <h3>{title}</h3>
        {tag}
	    <Markdown>{this.props.text}</Markdown>
	    </div>
        <Button onClick={()=>browserHistory.push(uri)} bsStyle="primary">more</Button><br />
        {footer}
    </Thumbnail> 
    );
}});

GenericThumbnailItem.propTypes = {
    id:React.PropTypes.number,
    uri:React.PropTypes.string,
    fields:React.PropTypes.object,
    tags:React.PropTypes.array,
    bsStyle:React.PropTypes.string
};
    

export default pure(GenericThumbnailItem);















