$(document).ready(function() {

	function ProjectVewModel() {
		var self = this;
		self.projectList = ko.observableArray();
		self.selectedProject = ko.observable({"name":""});
		var projectSnippetsUrl = '/api/v1/project-snippets/';
		getAndStoreList(projectSnippetsUrl,self.projectList);
		self.projectClick = function (project){
			var projectUrl = '/api/v1/projects/' + project.id + '/';
			getAndStoreObject(projectUrl,self.selectedProject);
		};
	}
	var container = $('#projects-container');
	ko.applyBindings(new ProjectVewModel(), container[0]);
});
