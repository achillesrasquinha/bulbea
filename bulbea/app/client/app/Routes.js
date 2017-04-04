import React from 'react';
import { Route, IndexRoute } from 'react-router'

import Config from './Config'
import Home from './pages/Home'

const Routes = (
	<Route path = {Config.URL.BASE}>
		<IndexRoute component = {Home}/>
	</Route>
)

export default Routes