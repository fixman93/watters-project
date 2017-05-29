(function () {
	'use strict';

	var module = angular.module('ngToggleBodyClass', []);

	module.directive('toggleBodyClass', function() {
		return {
			restrict: 'A',
			link: function ($scope, $elem, $attrs) {
				var $bodyClass = $attrs.toggleBodyClass || '';
				var $is_toggled = false;
				var $body  = angular.element(document.body);

				$scope.$on('$destroy', function() {
					if ($bodyClass) {
						$body.removeClass($bodyClass);
					}
				});
				
				$elem.on('click touchend', function() {
			        if ($bodyClass) {
			        	if(!$is_toggled){
			        		$body.addClass($bodyClass);
			        	}else{
			        		$body.removeClass($bodyClass);
			        	}
						$is_toggled = !$is_toggled;
					}
			    });
			}
		}
	});
}());
