import React from 'react'
import ReactDOM from 'react-dom'

import Config from './../Config'

import SearchForm from './../components/SearchForm'
import Panel from './../components/Panel'

class Home extends React.Component {
	constructor ( ) {
		super ( )

		this.onSubmit = this.onSubmit.bind(this)

		this.state    = Home.DEFAULT_STATES
	}

	onSubmit (query) {
		let tokens = query.split(' ')
		let source = tokens[0]
		let ticker = tokens[1]

		let params = { source: source, ticker: ticker }

		let that   = this

		$.post(Config.URL.PREDICT, params, function (data) {
			let response = JSON.parse(data)
			let status   = response.status

			if ( status == "success" ) {
				console.log(response.data)
				that.setState({
					data: response.data
				})
			}
		})
	}

	render ( ) {
		return (
			<div className="container">
				<div className="row">
					<div className="col-md-2"></div>
					<div className="col-md-8">
						<div className="form-group">
							<SearchForm onSubmit={this.onSubmit}/>
						</div>
						<Panel data={this.state.data}/>
					</div>
					<div className="col-md-2"></div>
				</div>
			</div>
		)
	}
}

Home.DEFAULT_STATES = 
{
	data: { }
}

export default Home