var wattersApp = angular.module('wattersApp', [
  'ngRoute',
  'wattersControllers',
  'sticky',
  'ngToggleBodyClass'
]);

wattersApp.directive('body', ['$rootScope',
  function($rootScope){
    return {
      restrict: 'E',
      link: function(scope, elem){
        $rootScope.$on('$routeChangeStart', function (e, next, current) {
          if(current && current.$$route && current.$$route.bodyClass){
            elem.removeClass(current.$$route.bodyClass);
          }
          if(next && next.$$route && next.$$route.bodyClass){
            elem.addClass(next.$$route.bodyClass);
          }
        });
      }
    };
  }
]);

wattersApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: '/partials/home.html',
        controller: 'HomeCtrl',
        bodyClass: 'homepage'
      }).
      when('/brides', {
        templateUrl: '/partials/landingpage.html',
        controller: 'LandingCtrl'
      }).
      when('/products/:productId', {
        templateUrl: '/partials/productpage.html',
        controller: 'ProductCtrl'
      }).
      when('/test', { // this route and file for designer only
        templateUrl: '/partials/test.html',
        controller: 'TestCtrl'
      }).
      when('/icons', { // this route and file for designer only
        templateUrl: '/partials/example-icons.html',
        controller: 'IconsCtrl'
      }).
      otherwise({
        templateUrl: '/partials/404.html',
        controller: '404Ctrl'
      });
  }]);

wattersApp.config(['$httpProvider',
  function($httpProvider) {
      $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  }]);

wattersApp.config(['$locationProvider',
  function($locationProvider) {
      $locationProvider.html5Mode(true);
      $locationProvider.hashPrefix('!');
  }]);