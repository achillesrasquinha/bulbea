import React from 'react'
import ReactDOM from 'react-dom'

class SearchForm extends React.Component {
	constructor ( ) {
		super ( )

		this.onChange = this.onChange.bind(this)
		this.onSubmit = this.onSubmit.bind(this)

		this.state    = SearchForm.DEFAULT_STATES
	}

	onChange (event) {
		this.setState({
			[event.target.name]: event.target.value
		})
	}

	onSubmit (event) {
		if ( ! event.isDefaultPrevented() ) {
			event.preventDefault()
		}

		let query = this.state.query

		if ( $.trim(query).length ) {
			this.props.onSubmit(query)
		}
	}

	render ( ) {
		return (
			<form onChange={this.onChange} onSubmit={this.onSubmit}>
				<div className="input-group">
					<input className="form-control" placeholder="Search..." name="query"/>
					<div className="input-group-btn">
						<button className="btn btn-default">
							<i className="fa fa-fw fa-search"></i>
						</button>
					</div>
				</div>
			</form>
		)
	}
}

SearchForm.DEFAULT_STATES =
{
	query: null
}

export default SearchForm
