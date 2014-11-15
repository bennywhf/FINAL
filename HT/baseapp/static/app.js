(function(){
  var app = angular.module('bulletinapp', []);
  
  var formc = app.controller('form', function(){
	this.on = true;
	
	this.toggle = function(){
		this.on = !this.on;
	}
  });
  
  var hover= app.controller('hover',function(){
	this.hovers=1;
	
	this.setHover = function(hover){
		this.hovers=hover;
	};
	
	this.isSelected = function(hovers){
		return hovers===this.hovers;
	};	
  });
  
  var tabs = app.controller('tabs',function(){
	
	this.tab=1;
	
	this.setTab = function(t){
		this.tab=t;
	};
	
	this.isSelected = function(tab){
		return tab===this.tab;
	};
  });

  var login = app.controller('login', function(){
    this.bar = false;
    this.toggle = function(){
        this.bar = !(this.bar);
    };
  });


})();
