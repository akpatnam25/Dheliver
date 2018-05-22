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
    
    // Enumerates an array.
    var enumerate = function(v) { var k=0; return v.map(function(e) {e._index = k++;});};
    
    function get_memos_url(start_index, end_index) {
        var pp = {start_index: start_index,
                  end_index: end_index
                 };
        return memos_url + "?" + $.param(pp);
    }
    
    // Initial retrieval of memos
    self.get_memos = function() {
        $.getJSON(get_memos_url(0, 10), function(data) {
            self.vue.memos = data.memos;
            self.vue.has_more = data.has_more;
            self.vue.logged_in = data.logged_in;
            enumerate(self.vue.memos);
        })
    };
    
    // Get more memos
    self.get_more_memos = function() {
        var num_memos = self.vue.memos.length;
        $.getJSON(get_memos_url(num_memos, num_memos + 10), function(data) {
            self.extend(self.vue.memos, data.memos);
            self.vue.has_more = data.has_more;
            enumerate(self.vue.memos);
        })
    }
    
    // Add memo toggle button
    self.add_memo_button = function() {
        self.vue.is_adding_memo = !self.vue.is_adding_memo;
    };
    
    // Submit new memo form
    self.add_memo_form = function() {
        $.post(add_memo_url,
            {
                title: self.vue.form_title,
                memo: self.vue.form_memo
            },
            function (data) {
                $.web2py.enableElement($("#add_memo_submit"));
                self.vue.memos.unshift(data.memo);
                enumerate(self.vue.memos);
                self.vue.form_title = '';
                self.vue.form_memo = '';
            });
        self.vue.is_adding_memo = !self.vue.is_adding_memo;
    };
    
    // Delete the memo
    self.delete_memo = function(memo_index) {
        $.post(del_memo_url,
            { memo_id: self.vue.memos[memo_index].id },
            function () {
                self.vue.memos.splice(memo_index, 1);
                enumerate(self.vue.memos);
            }
        )
    };
    
    // Toggle public/private for memo
    self.toggle_public = function(memo_index) {
        $.post(tog_public_url,
            { memo_id: self.vue.memos[memo_index].id },
            function (data) {
                self.vue.memos[memo_index].is_public = data.toggle
            });
    };
    
    // Edit memo save
    self.edit_memo_save = function(memo_index) {
        $.post(edit_memo_url,
            {
                memo_id: self.vue.memos[memo_index].id,
                title: self.vue.edit_title,
                memo: self.vue.edit_memo
            },
            function (data) {
                $.web2py.enableElement($("#edit_memo_submit"));
                self.vue.memos[memo_index].title = self.vue.edit_title;
                self.vue.memos[memo_index].memo = self.vue.edit_memo;
                self.vue.edit_title = '';
                self.vue.edit_memo = '';
            });
        self.vue.selected_id = -1;
    };
    
    // Button for memo editing
    self.edit_memo_button = function(memo_index) {
        self.vue.selected_id = memo_index;
        self.vue.edit_title = self.vue.memos[memo_index].title;
        self.vue.edit_memo = self.vue.memos[memo_index].memo;
    };
    
    // Button for cancelling an edit
    self.cancel_edit_button = function() {
        self.vue.selected_id = -1;
        self.vue.edit_title = '';
        self.vue.edit_memo = '';
    };
    
    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            memos: [],
            logged_in: false,
            has_more: false,
            is_adding_memo: false,
            form_title: null,
            form_memo: null,
            selected_id: -1
        },
        methods: {
            get_more_memos: self.get_more_memos,
            add_memo_button: self.add_memo_button,
            add_memo_form: self.add_memo_form,
            delete_memo: self.delete_memo,
            toggle_public: self.toggle_public,
            edit_memo_save: self.edit_memo_save,
            edit_memo_button: self.edit_memo_button,
            cancel_edit_button: self.cancel_edit_button
        }

    });
    
    self.get_memos();
    $("#vue-div").show();
    
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
