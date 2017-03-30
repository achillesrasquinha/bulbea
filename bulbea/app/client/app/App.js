import React from 'react'

class App extends React.Component {
	constructor ( ) {
		super()

		this.onSubmit = this.onSubmit.bind(this);
	}

	onSubmit (event) {
		if ( ! event.isDefaultPrevented() ) {
			event.preventDefault()
		}
	}

    render ( ) {
      return (
      	<div className="container">
      		<form onSubmit={this.onSubmit}>
	      		<div className="form-group">
	      			<div className="input-group">
	      				<input className="form-control" type="text" placeholder="Search for a share"/>
	      				<div className="input-group-btn">
	      					<button className="btn btn-default">
	      						<i className="fa fa-fw fa-search"></i>
	      					</button>
	      				</div>
	      			</div>
	      		</div>
	      	</form>
      		<div className="panel panel-default">
      			<div className="panel-body">
      				<div className="row">
      					<div className="col-md-9">
      						
      					</div>
      					<div className="col-md-3">

      					</div>
      				</div>
      			</div>
      		</div>
      	</div>
      )
    }
}

export default App
