var plantPulseApp = angular.module('plantPulseApp', ['LocalStorageModule', 'ui.bootstrap']);

plantPulseApp.directive('compiled', function($compile) {
    return {
        restrict: 'A',
        replace: true,
        link: function (scope, ele, attrs) {
            scope.$watch(attrs.compiled, function(html) {
                ele.html(html);
                $compile(ele.contents())(scope);
            });
        }
    };
});

plantPulseApp.directive('onEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
			if(event.which === 13) {
				scope.$apply(function (){
                    scope.$eval(attrs.onEnter);
                });

                event.preventDefault();
            }
        });
    };
});

plantPulseApp.filter('unsafe', function($sce) {
    return function(val) {
		if (val === undefined || val === null) {
			return "";
		}
        return $sce.trustAsHtml(val);
    };
});

plantPulseApp.filter('isodate', function() {
	return function(sfdate) {
		var chat_moment = moment(sfdate, "YYYY-MM-DDTHH:mm:ss.000+0000");
		if (chat_moment === null || chat_moment === undefined) {
			chat_moment = moment(sfdate, "YYYY-MM-DDTHH:mm:ssZ");
		}
		return chat_moment.local().format("MM/DD HH:mma");
	};
});