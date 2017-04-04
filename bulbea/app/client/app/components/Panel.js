import React from 'react'
import ReactDOM from 'react-dom'

class Panel extends React.Component {
	render ( ) {
		let data = this.props.data

		return (
			<div className="panel panel-default">
				<div className="panel-body">
					<div className="text-center">
						<img src={data.plot} className="img-responsive img-thumbnail"/>
					</div>
				</div>
				<div className="panel-footer">
					<div className="row">
						<div className="col-md-6">
							<table className="table-condensed">
								<thead className="text-uppercase">
									<tr>
										<th>Open</th>
										<th>High</th>
										<th>Low</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>{data.open}</td>
										<td>{data.high}</td>
										<td>{data.low}</td>
									</tr>
								</tbody>
							</table>
						</div>
						<div className="col-md-6">

						</div>
					</div>
				</div>
			</div>
		)
	}
}

export default Panel