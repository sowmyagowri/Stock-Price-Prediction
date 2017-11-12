angular.module('MainCtrl', []).controller('MainController', function($scope,$timeout, $q, $log,$location) {

	$scope.tagline = 'Stock Price Prediction!';
	$scope.resources = ['static/css/videos/overviewBg.mp4'],
	$scope.poster = 'http://placehold.it/2000&text=you%20may%20want%20to%20have%20a%20poster',
	$scope.fullScreen = false,
	$scope.muted = true,
	$scope.zIndex = '22'
	$scope.pausePlay = false,
	$scope.currentResourceIdx = 0;
	$scope.playInfo = {};
	$scope.overView = function () {
	$location.path("/overview");
	}
	var self = this;
	self.simulateQuery = false;
	self.isDisabled    = false;

	// ******************************
	// Internal methods
	// ******************************

	/**
	 * Search for companies... use $timeout to simulate
	 * remote dataservice call.
	 */
	$scope.querySearch = function  (query) {
		var results = query ? self.companies().filter( self.createFilterFor(query) ) : self.companies(),
				deferred;
		if (self.simulateQuery) {
			deferred = $q.defer();
			$timeout(function () { deferred.resolve( results ); }, Math.random() * 1000, false);
			return deferred.promise;
		} else {
			return results;
		}
	}

	$scope.searchTextChange = function (text) {
		$log.info('Text changed to ' + text);
	}

	$scope.selectedItemChange = function (item) {
		$log.info('Item changed to ' + JSON.stringify(item));
		$location.path("/overview");
	}

	/**
	 * Build `companies` list of key/value pairs
	 */
	self.loadAll = function () {
		var allCompanies = 'A, AA';

		return allCompanies.split(/, +/g).map( function (company) {
			return {
				value: company.toLowerCase(),
				display: company
			};
		});
	}

	// list of `company` value/display objects
	self.companies        = self.loadAll;

	/**
	 * Create filter function for a query string
	 */
	self.createFilterFor = function (query) {
		var lowercaseQuery = angular.lowercase(query);

		return function filterFn(company) {
			return (company.value.indexOf(lowercaseQuery) === 0);
		};
	}
});
