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
    var enumerate = function(v) { var k=0; return v.map(function(e) {e._idx = k++;});};

    function get_memos_url(start_idx, end_idx) {
        var pp = {
            start_idx: start_idx,
            end_idx: end_idx
        };
        return memos_url + "?" + $.param(pp);
    }

     self.get_memos = function () {
        $.getJSON(get_memos_url(0, 10), function (data) {
            self.vue.checklists = data.checklists;
            self.vue.has_more_memo = data.has_more_memo;
            self.vue.logged_in = data.logged_in;
            enumerate(self.vue.checklists);
        })
    };


    self.get_more_memo = function () {
        var num_memos = self.vue.checklists.length;
        $.getJSON(get_memos_url(num_memos, num_memos + 10), function (data) {
            self.vue.has_more_memo = data.has_more_memo;
            self.extend(self.vue.checklists, data.checklists);
            enumerate(self.vue.checklists);
        });
    };

      self.add_memo_button = function () {
        // The button to add a track has been pressed.
        self.vue.is_adding_memo = !self.vue.is_adding_memo;
    };



    self.add_memo = function () {
        // The submit button to add a track has been added.
        $.post(add_memo_url,
            {
                title: self.vue.form_title,
                description: self.vue.form_description
            },
            function (data) {
                $.web2py.enableElement($("#add_memo_submit"));
                self.vue.checklists.unshift(data.checklist);
                enumerate(self.vue.checklists);
            });
    };



    self.delete_memo = function(memo_idx) {
        $.post(del_memo_url,
            { memo_id: self.vue.checklists[memo_idx].id },
            function () {
                self.vue.checklists.splice(memo_idx, 1);
                enumerate(self.vue.checklists);
            }
        )
    };



    self.select_memo = function(memo_idx) {
        var checklist = self.vue.checklists[memo_idx];
        if (self.vue.selected_mid === checklist.id) {
            // Deselect track.
            self.vue.selected_mid = -1;
        } else {
            // Select it.
            self.vue.selected_idx = memo_idx;
            self.vue.selected_mid = checklist.id;
            self.vue.selected_url = checklist.memos_url;
        }

    };

     self.edit_memo_button = function () {
        // The button to add a track has been pressed.
        self.vue.is_editing_memo = !self.vue.is_editing_memo;
    };

    self.edit_memo = function(memo_idx) {
        $.post(edit_memo_url,
            {
                memo_id: self.vue.checklists[memo_idx].id,
                title: self.vue.form_title,
                description: self.vue.form_description
            },
            function (data) {
                self.vue.checklists.splice(memo_idx, 1, data.checklist);
                $.web2py.enableElement($("#edit_memo_submit"));
                enumerate(self.vue.checklists);
            });
    };

//    self.toggle_visibility= function() {
////        var checklist = self.vue.checklists[memo_idx];
//        self.vue.is_public = !self.vue.is_public;
//
//
//    };

    self.toggle_visibility = function(memo_idx) {
        var checklist = self.vue.checklists[memo_idx];
//        checklist.is_public = !checklist.is_public;
        self.vue.is_public = !self.vue.is_public;

        $.post(toggle_visibility_url,
        {
//            memo_id: self.vue.checklists.id
              memo_id: self.vue.checklists[memo_idx].id
        },
        function () {
            var idx = null;
            for (var i = 0; i < self.vue.checklists.length; i++) {
                if (self.vue.checklists[i].id === checklist) {
                    enumerate(self.vue.checklists);
                    idx = i + 1;
                    break;
                }
            }

        })

    };



    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {

            logged_in: false,


            is_adding_memo: false,
            is_editing_memo: false,
            checklists: [],
            has_more_memo: false,
            form_title: null,
            form_description: null,
            selected_mid: -1,
            is_public: false

        },
        methods: {

            get_more_memo: self.get_more_memo,
            add_memo_button: self.add_memo_button,
            add_memo: self.add_memo,
            delete_memo: self.delete_memo,
            select_memo: self.select_memo,
            edit_memo_button: self.edit_memo_button,
            edit_memo: self.edit_memo,
            toggle_visibility: self.toggle_visibility,
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

