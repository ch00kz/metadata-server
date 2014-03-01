$(document).ready(function() {
	function ActionVewModel() {
		var self = this;
		self.actionData = ko.observableArray();
		var actionUrl = '/api/v1/activity/';
		$.get(actionUrl,{},function(data){
			self.actionData(data.objects);
		});
	}
	var container = $('#dashboard-container');
	ko.applyBindings(new ActionVewModel(), container[0]);
});

