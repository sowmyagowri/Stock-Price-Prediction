var app = angular.module("PredictionCtrl", []);

app.controller("PredictionController", function ($scope, $http) {

	$scope.predictstockprices = function(){


		$http.get('/prediction',JSON.stringify(data)).then(function (response) {

			var values = response.data[0].value;
			var xTicks = [];
			xTicks.push(values[0]);
			for (var i = 1 ; i < values.length; i++) {
				xTicks.push(values[0]+i);
			}

			$scope.stockPricesData =  [
			  {
			    "key": response.data[1].label,
			    "values": response.data[1].value
			  },
			  {
			    "key": response.data[2].label,
			    "values": response.data[2].value
			  }
			]

			nv.addGraph(function() {
		    var chart = nv.models.cumulativeLineChart()
		                  .x(function(d) { return d[0] })
		                  .y(function(d) { return d[1]/100}) //adjusting, 100% is 1.00, not 100 as it is in the data
		                  .color(d3.scale.category10().range())
		                  .useInteractiveGuideline(true)
		                  ;

		     chart.xAxis
		        .tickValues( xTicks)
		        .axisLabel('Year');

		      chart.yAxis
        		.tickFormat(d3.format(',.1%'))
        		.axisLabel('Stock Price in $');

		      d3.select('#stockPricesChart svg')
		        .datum($scope.stockPricesData)
		        .call(chart);


		    //TODO: Figure out a good way to do this automatically
		    nv.utils.windowResize(chart.update);

	    	return chart;
  		});
	})
	}
});
