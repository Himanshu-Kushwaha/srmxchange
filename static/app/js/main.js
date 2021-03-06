import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route, IndexRoute, browserHistory} from 'react-router';

import Layout from './Layout';
import Latest from './pages/Latest';
import ExperienceSpeaks from './pages/ExperienceSpeaks';
import ListViewPage from './pages/ListViewPage';
import MultiListViewPage from './pages/MultiListViewPage';
import SimpleDetailViewPage from './pages/SimpleDetailViewPage';
import ListView from './components/ModelViews/ListView';
import DetailView from './components/ModelViews/DetailView';
import Available from './pages/Available';
import GenericPanelItem from './components/GenericPanelItem';
import GenericThumbnailItem from './components/GenericThumbnailItem';
import GenericMediaItem from './components/GenericMediaItem';
import {BASE_URL} from './constants';
import axios from 'axios';

const app = document.getElementById('app');

if(window.localStorage.hasOwnProperty('route')){
    browserHistory.push(window.localStorage.getItem('route'));
}

browserHistory.listen(function(ev) {
    window.localStorage.setItem('route',ev.pathname);
});


axios.get('/app/get_route/')
    .then(({data})=>{
	console.log(data.route); 
	browserHistory.push(BASE_URL+data.route);})
    .catch((error)=>0); 


const routes = (
	<Route path={BASE_URL} component={Layout}>
	<IndexRoute component={MultiListViewPage}
	 title={['Wanted','Available']}
	 class={[GenericPanelItem, GenericPanelItem]}
	 model={['wanted','available']} 
	 bsStyle={['info','success']}
	/>
	<Route title='Wanted' class={GenericPanelItem} path='wanted' model='wanted' 
		bsStyle='info' orderings={['-created','-num_views']} component={ListViewPage} />
	<Route title='Wanted' class={GenericPanelItem} path='wanted/:id' model='wanted' 
		bsStyle='info' component={SimpleDetailViewPage} />
	<Route title='Available' class={GenericPanelItem} path='available' model='available' 
		bsStyle='success' orderings={['-created','-num_views']} component={ListViewPage} />
	<Route title='Project' class={GenericThumbnailItem} path='project' model='project' 
		bsStyle='info' orderings={['-created','-num_views']} component={ListViewPage} />
	<Route title='Event' class={GenericThumbnailItem} path='event' model='event' 
		bsStyle='info' orderings={['-created','-num_views']} component={ListViewPage} />
	<Route title='Experience Speaks' class={GenericMediaItem} path='story' model='story' 
		bsStyle='info' orderings={['-created','-num_views']} component={ListViewPage} />
	<Route path='*' component={Latest} />
	</Route>);

ReactDOM.render(
	<Router history={browserHistory}>
	{routes}
	</Router>
	, app);










