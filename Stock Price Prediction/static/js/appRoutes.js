angular.module('appRoutes', [])
.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {

	$routeProvider

		// home page
		.when('/', {
			templateUrl: 'static/views/home.html',
			controller: 'MainController'
		})

		.when('/prediction', {
			templateUrl: 'static/views/prediction.html',
			controller: 'PredictionController'
		})
		
		.when('/overview', {
			templateUrl: 'static/views/overview.html',
			controller: 'OverviewController'
		});

	$locationProvider.html5Mode(true);

}])
.run( function($rootScope, $location, LoginService) {

    // register listener to watch route changes
    $rootScope.$on( "$routeChangeStart", function(event, next, current) {
	 		if(next.templateUrl== "static/views/overview.html"){
				$location.path("/prediction");
			}
    });
 });
