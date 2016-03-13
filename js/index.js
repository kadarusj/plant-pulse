var DEF_ERROR = "ERROR loading data from datastore";

var IndexCtrl = function($scope, $http, $modal, $log, $window, localStorageService, $sce) {
	$scope.in_progress_txt = "Loading ...";
	$scope.show_plant_table = true;
	
	$scope.init = function() {
		/*
		$scope.show_plant_table = false;
		$scope.show_inprogress = true;
		$scope.show_error_alert = false;
		
	  	$http.get('/plant-data')
	  	.then(function(response) {
			$scope.load_plant_table(response);
		}, function(response) {
			$scope.error_alert_msg = DEF_ERROR +": "+ response;
			$scope.show_error_alert = true;
			$scope.show_inprogress = false;
	  	});
		*/
		$scope.show_plant_table = true;
		$scope.load_plant_table();
	};
	
	$scope.load_plant_table = function() {
		$('#plant-table').DataTable({
			"ajax": "/plant-data",
        	"columns": [
            	{ "data": "timestamp" },
				{ "data": "node_id" },
				{ "data": "pod_id" },
				{ "data": "node_location" },
				{ "data": "lux" },
				{ "data": "broadband" },
            	{ "data": "infrared" },
				{ "data": "air_temp" },
				{ "data": "humidity" },
				{ "data": "heat_index" },
				{ "data": "soil_temp" },
				{ "data": "soil_moist1" },
				{ "data": "soil_moist2" },
				{ "data": "plant_volt" },
				{ "data": "batt_volt" }
        	],
			"columnDefs": [
				{
			    	"render": function ( data, type, row ) {
						var utc = moment.utc(data);
						utc.local();
						
			        	return utc.format("L") +" "+ utc.format("LT");
			        },
			        "targets": 0
				}
			],
			"order": [[ 0, "desc" ]]
		});
		/*
		$scope.show_inprogress = false;
		*/
	};
	
	angular.element(document).ready(function () {
		//$scope.init();
		$scope.load_plant_table();
	});
};