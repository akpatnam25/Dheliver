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
    var enumerate = function(v) {
        var k = 0;
        return v.map(function(e) { e._idx = k++; });
    };

    // get_memos_url()
    function get_memos_url(start_index, end_index) {
        var pp = {
            start_index: start_index,
            end_index: end_index,
        };
        return memos_url + "?" + $.param(pp);
    };

    // sort_memos()
    // For a logged_in user, sort self.vue.memos such that the user's memos
    // will appear first.
    function sort_memos() {
        if (self.vue.logged_in) {
            var user_memos = [];
            var public_memos = [];
            for (var i = 0; i < self.vue.memos.length; i++) {
                var memo = self.vue.memos[i];
                if (self.vue.user_email == memo.user_email) {
                    // User Memo
                    user_memos.push(memo);
                } else {
                    // Public Memo
                    public_memos.push(memo);
                }
            }

            // Combine the user_memos with the public_memos.
            self.extend(user_memos, public_memos);

            // Set vue.memos to the sorted list of memos. 
            self.vue.memos = user_memos;
        }
        enumerate(self.vue.memos);
    }

    // add_fetched_memos()
    // Given an array of memos retrieved from the API, add new memos to vue.memos.
    // - New memos' id will not be in vue.memo_ids.
    function add_fetched_memos(fetched_memos) {
        for (var i = 0; i < fetched_memos.length; i++) {
            var memo = fetched_memos[i];
            if (!self.vue.memo_ids.has(memo.id)) {
                self.vue.memos.push(memo);
                self.vue.memo_ids.add(memo.id);
            }
        }
        sort_memos();
    }


    // get_memos()
    // Use the API to fetch the first 10 memos from the server.
    // - Retrieves whether or not the user is logged in.
    // - Retrieves the user's email, if they are logged in.
    // - Retrieves whether or not more memos are available.
    self.get_memos = function() {
        $.getJSON(get_memos_url(0, 10), function(data) {
            self.vue.has_more = data.has_more;
            self.vue.logged_in = data.logged_in;
            self.vue.user_email = data.user_email;
            add_fetched_memos(data.memos);
        })
    };

    // get_more_memos()
    // Use the API to fetch 10 more memos from the server.
    self.get_more_memos = function() {
        var memo_count = self.vue.memos.length;
        $.getJSON(get_memos_url(memo_count, memo_count + 10), function(data) {
            self.vue.has_more = data.has_more;
            add_fetched_memos(data.memos);
        });
    };

    // add_memo_button()
    // Sets the vue.adding_memo boolean to true such that the "Add Memo" Form
    // appears for the user.
    self.add_memo_button = function() {
        if (!self.vue.adding_memo) {
            self.vue.adding_memo = true;
        }
    };

    // add_memo()
    // Use the API to submit the "Add Memo" form's memo to the server.
    // - The new memo is then added to vue.memos.
    self.add_memo = function() {
        if (self.vue.adding_memo) {
            $.post(add_memo_url,
                {
                    title: self.vue.add_form_title,
                    memo: self.vue.add_form_memo,
                }, function (data) {
                    self.vue.adding_memo = false;
                    self.vue.add_form_title = null;
                    self.vue.add_form_memo = null;
                    
                    self.vue.memos.unshift(data.memo);
                    self.vue.memo_ids.add(data.memo.id);
                    sort_memos();
                }
            );
        }
    };

    // cancel_add_button()
    // Sets vue.adding_memo to false and clears the "Add Memo" form, such that
    // it no longer appears for the user.
    self.cancel_add_button = function() {
        if (self.vue.adding_memo) {
            self.vue.adding_memo = false;
            self.vue.add_form_title = null;
            self.vue.add_form_memo = null;
        }
    };

    // edit_memo_button()
    // Show the "Edit Memo" form for the memo corresponding to memo_index.
    self.edit_memo_button = function(memo_index) {
        var memo = self.vue.memos[memo_index];
        var edit_form_fields = {
            title: memo.title,
            memo: memo.memo,
        };
        Vue.set(self.vue.in_progress_edits, memo.id, edit_form_fields);
    }

    // edit_memo()
    // Use the API to submit the "Edit Memo" form for the corresponding memo
    // to the server.
    // - The memo is then updated to correspond to the changes.
    self.edit_memo = function(memo_index) {
        var memo = self.vue.memos[memo_index];
        if (memo.id in self.vue.in_progress_edits) {
            var updated_title = self.vue.in_progress_edits[memo.id].title;
            var updated_memo = self.vue.in_progress_edits[memo.id].memo; 
            $.post(edit_memo_url,
                {
                    memo_id: memo.id,
                    title: updated_title,
                    memo: updated_memo,
                }, function() {
                    Vue.set(self.vue.memos[memo_index], 'title', updated_title);
                    Vue.set(self.vue.memos[memo_index], 'memo', updated_memo);
                    Vue.delete(self.vue.in_progress_edits, memo.id);
                }
            );
        }
    }

    // cancel_edit_button()
    // Cancel the corresponding memo's "Edit Memo" form.
    self.cancel_edit_button = function(memo_index) {
        var memo = self.vue.memos[memo_index];
        if (memo.id in self.vue.in_progress_edits) {
            Vue.delete(self.vue.in_progress_edits, memo.id);
        }
    }

    // delete_memo()
    // Use the API to send a delete request for the corresponding memo.
    // - Removes the memo from vue.memos upon success.
    self.delete_memo = function(memo_index) {
        var memo = self.vue.memos[memo_index];
        $.post(delete_memo_url,
            { memo_id: memo.id },
            function() {
                self.vue.memo_ids.delete(memo.id);
                self.vue.memos.splice(memo_index, 1);
                sort_memos();
            }
        );
    };

    // toggle_memo_visibility()
    // Use the API to send a toggle visibility request for the corresponding memo.
    // - Toggles the is_public field upon success.
    self.toggle_memo_visibility = function(memo_index) {
        var memo = self.vue.memos[memo_index];
        $.post(toggle_memo_visibility_url,
            { memo_id: memo.id },
            function() {
                var is_public = self.vue.memos[memo_index].is_public;
                Vue.set(self.vue.memos[memo_index], 'is_public', !is_public); 
            }
        );
    }

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            logged_in: false,
            user_email: null,

            memos: [],
            memo_ids: new Set([]),
            has_more: false,

            adding_memo: false,
            add_form_title: null,
            add_form_memo: null,

            in_progress_edits: {},
        },
        methods: {
            get_more_memos: self.get_more_memos,

            add_memo: self.add_memo,
            add_memo_button: self.add_memo_button,
            cancel_add_button: self.cancel_add_button,
            
            edit_memo: self.edit_memo,
            edit_memo_button: self.edit_memo_button,
            cancel_edit_button: self.cancel_edit_button,
            
            delete_memo: self.delete_memo,
            toggle_memo_visibility: self.toggle_memo_visibility,
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
