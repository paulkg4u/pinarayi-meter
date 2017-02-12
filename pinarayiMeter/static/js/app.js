var pinarayiMeter = angular.module('pinarayiMeter', []);

angular.module('pinarayiMeter').controller('homePageController', function($scope, $rootScope, $http) {
    $scope.selectedCategory = 'agriculture';

    $scope.$watch(function() {
        return $scope.selectedCategory;
    }, function() {
        if (!$rootScope.categoryData[$scope.selectedCategory]) {
        	$scope.loadingCategoryData = true;
            $http({
                method: 'GET',
                url: '/promise/api/category',
                params: {
                    'type': 'minimal',
                    'categoryList': $scope.selectedCategory
                }
            }).then(function successCallback(response) {
            	$rootScope.selectedCategory = response.data;
            	$scope.loadingCategoryData = false;
            }, function errorCallback(response) {
                console.log(response.data);
                $scope.loadingCategoryData = false;
            });
        }
    }, true);

    $rootScope.loadingStats = true;
    $http({
        method: 'GET',
        url: '/promise/api/status'
    }).then(function successCallback(response) {
        $scope.status = response.data;
        $rootScope.loadingStats = false;
    }, function errorCallback(response) {
        console.log(response);
        $rootScope.loadingStats = false;
    });

});
pinarayiMeter.run(function($rootScope, $http) {
    $rootScope.baseURL = '127.0.0.1:8000';
    $rootScope.categoryData = {
        'agriculture': null,
        'education': null,
        'industries': null,
        'lawandorder': null,
        'it': null,
        'tourism': null,
        'infrastructure': null,
        'humandevelopment': null,
        'health':null
    };
});

angular.module('pinarayiMeter').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
