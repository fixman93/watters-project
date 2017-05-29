var wattersControllers = angular.module('wattersControllers', []);

wattersControllers.controller('HomeCtrl', ['$scope', '$rootScope',
  function($scope, $rootScope) {
    $rootScope.page_title = "Home";
  }]);

wattersControllers.controller('LandingCtrl', ['$scope', '$rootScope',
  function($scope, $rootScope) {
    $scope.title = $rootScope.page_title = "Brides";

    $scope.hiddenMenu = false; // extract from cookies / LocalStorage ?
    
    $scope.toggleMenu = function() {
      $scope.hiddenMenu = ! $scope.hiddenMenu; // save to cookies / LocalStorage ?
    }
  }]);

wattersControllers.controller('ProductCtrl', ['$scope', '$routeParams', '$rootScope',
  function($scope, $routeParams, $rootScope) {
    $scope.title = $rootScope.page_title = 'Product #' + $routeParams.productId;
  }]);

wattersControllers.controller('TestCtrl', ['$rootScope',
  function($rootScope) {
    $rootScope.page_title = "Base HTML Elements";
  }]);

wattersControllers.controller('IconsCtrl', ['$rootScope',
  function($rootScope) {
    $rootScope.page_title = "Icons";
  }]);

wattersControllers.controller('404Ctrl', ['$rootScope',
  function($rootScope) {
    $rootScope.page_title = "Page not Found";
  }]);