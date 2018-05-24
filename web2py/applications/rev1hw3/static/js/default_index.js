// This is the js for the default/index.html view.

var app = function() {

	var self = {};

	Vue.config.silent = false; // show all warnings

	// Extends an array
	self.extend = function(a, b) {
		for (var i = 0; i < b.length; i++) {
			a.push(b[i]);
		}
	};
	
	// Sends the contents of the new memo form to the server
	self.new_memo = function() {
		$.post(memo_new_url, {
			// Data
			title: self.vue.form_new_memo_title,
			content: self.vue.form_new_memo_content
		}, function(data) {
			// On success, close and add the new item to the top of the memo list
			self.vue.new_memo_open = false;
			
			self.vue.checklists.unshift(self.prepare_memo(data.new_memo, false));
		})
	}
	
	// Sends the contents of the new memo form to the server
	self.memo_edit = function(checklist) {
		$.post(memo_edit_url, {
			// Data
			id: checklist.id,
			title: checklist.edit_title,
			memo: checklist.edit_memo
		}, function(data) {
			// On success, stop editing and update local record
			var newChecklist = self.find_memo(checklist.id)
			newChecklist.title = checklist.edit_title;
			newChecklist.memo = checklist.edit_memo;
			newChecklist.is_editing = false;
		})
	}
	
	// Clears the data from the new memo form fields
	self.form_new_memo_clear = function() {
		self.vue.form_new_memo_title = null;
		self.vue.form_new_memo_content = null;
	}
	
	// Asks the server to toggle the public status of the memo who's id is passed
	self.toggle_memo_toggle_public = function(id) {
		$.post(memo_toggle_public_url, {
			id: id,
		}, function(data) {
			// On success, toggle local record
			var checklist = self.find_memo(id);
			checklist.is_public = !checklist.is_public;
		})
	}
	
	// Deletes a memo from the server with the given id
	self.memo_delete = function(id) {
		$.post(memo_delete_url, {
			id: id,
		}, function(data) {
			// On success, remove local record
			var i = self.find_memo_index(id);
			self.vue.checklists.splice(i, 1);
		})
	}
	
	// Fill the required memo fields for editing
	// Must be called before being introduced to Vue
	self.prepare_memo = function(checklist, is_editing = null) {
		// Data needed for editing
		if (is_editing !== null) {
			checklist.is_editing = is_editing;
		}
		checklist.edit_title = checklist.title;
		checklist.edit_memo = checklist.memo;
		return checklist;
	}

	
	// Complete as needed.
	self.vue = new Vue({
		el: "#vue-div",
		delimiters: ['${', '}'],
		unsafeDelimiters: ['!{', '}'],
		data: {
			// Booleans
			logged_in: false,
			new_memo_open: false,
			
			// Data
			checklists: null,
			email: null,
			
			// New memo form
			form_new_memo_title: null,
			form_new_memo_content: null
		},
		methods: {
			new_memo: self.new_memo,
			form_new_memo_clear: self.form_new_memo_clear,
			toggle_memo_toggle_public: self.toggle_memo_toggle_public,
			memo_delete: self.memo_delete,
			memo_edit: self.memo_edit,
			prepare_memo: self.prepare_memo,
		}

	});
	
	
	// Methods not included in Vue
	
	// Finds and returns the index of a memo in Vue by id
	self.find_memo_index = function(id) {
		for (var i = 0; i < self.vue.checklists.length; i++) {
			if (self.vue.checklists[i].id == id) {
				return i;
			}
		}
		
		// Couldn't find a match
		return null;
	}
	
	// Finds and returns a memo object in Vue by id
	self.find_memo = function(id) {
		return self.vue.checklists[self.find_memo_index(id)];
	}
	
	// Always get the basic page information
	self.get_index = function() {
		$.getJSON(index_url, function(data) {
			for (var i = 0; i < data.checklists.length; i++) {
				data.checklists[i] = self.prepare_memo(data.checklists[i], false);
			}
			
			self.vue.logged_in = data.logged_in;
			self.vue.checklists = data.checklists;
			self.vue.email = data.email;
		})
	}
	
	self.get_index();
	
	return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
