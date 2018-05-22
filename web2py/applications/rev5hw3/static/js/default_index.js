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

    ///HOMEWORK ATTEMPT 1
    function get_posts_url(start_index, end_index) {
        console.log("get_posts_url");
        var x = {
            start_index: start_index,
            end_index: end_index
        };
        return posts_url + "?" + $.param(x);
    }

    self.get_posts = function () {
        console.log("get_posts");
        var post_len = self.vue.posts.length;
        $.getJSON(get_posts_url(post_len, post_len+10), function (data) {
            console.log(data);
            self.vue.posts = data.posts;
            self.vue.has_more = data.has_more;
            self.vue.logged_in = data.logged_in;
        })
    };

    self.get_zeroposts = function () {
        console.log("self.get_zeroposts");
        var post_len = self.vue.posts.length;
        $.getJSON(get_posts_url(post_len, post_len+0), function (data) {
            console.log(data);
            self.vue.posts = data.posts;
            self.vue.has_more = data.has_more;
            self.vue.logged_in = data.logged_in;
        })
    };


    self.add_post_button = function () {
        // The button to add a track has been pressed.
        if(self.vue.logged_in)
          self.vue.is_adding_post = !self.vue.is_adding_post;
      };

      self.get_more = function () {
        var num_posts = self.vue.posts.length;
        $.getJSON(get_posts_url(num_posts, num_posts + 10), function (data) {
            self.vue.has_more = data.has_more;
            self.extend(self.vue.posts, data.posts);
        });
    };



    self.add_post = function () {
        // The submit button to add a track has been added.
        $.post(add_post_url,
        {
            content: self.vue.form_content,
            title: self.vue.form_title, //////adding title from tyler 
            is_public: false
        },
        function (data) {
            // $.web2py.enableElement($("#add_post_submit"));
            self.vue.posts.unshift(data.post);
            // if posts.length is greater than 10 has_more becomes true
            if (self.vue.posts.length > 10) {
                self.vue.has_more = true;
            }
            self.vue.is_adding_post = !self.vue.is_adding_post;
            self.vue.form_content = "";
            self.vue.form_title = ""; //////adding title from tyler 
        });


        document.location.reload() //TEMPFIX
    };

    self.edit_post_submit = function () {
        // The submit button to add a track has been added.
        $.post(edit_post_url,
        {
            post_content: self.vue.edit_content, // new content
            title: self.vue.edit_title, // new title
            id: self.vue.edit_id //the id
        },
        function (data) {
            self.vue.editing = !self.vue.editing; //close editing box
        });
    };

    self.edit_post = function(post_id) {
        console.log("edit_post");
        self.vue.editing = !self.vue.editing;
        self.vue.edit_id = post_id;
    };


    ///////////////////////////////////////////////////////////////////////////////////
    //TOGGLE FUNCTION
    self.toggle_post = function(post_id) {
        var x = null;
        for (var i = 0; i < self.vue.posts.length; i++) {
            if (self.vue.posts[i].id === post_id) {
                x = i; 
                console.log("vue.posts[i].is_public");
                console.log(self.vue.posts[i].is_public);
                self.vue.posts[i].is_public = !self.vue.posts[i].is_public;
                break;
            }
        }
        $.post(toggle_post_url,
        {
            is_public: self.vue.posts[x].is_public, //////adding title from tyler 
            post_id: post_id
        },
        function (data) {
            // self.vue.posts[x].is_public = !self.vue.posts[x].is_public;
        });
    };
    //////////////////////////////////////////////////////////////////////////////


    self.cancel_edit = function () {
        self.vue.editing = !self.vue.editing; 
        self.vue.edit_id = 0;   
        window.location.reload();//TEMPFIX

    };

    self.cancel_add = function () {
        self.vue.is_adding_post = !self.vue.is_adding_post;
        self.vue.form_content = "";
        self.vue.form_title = ""; //////adding title from tyler  
    };


    self.delete_track = function(post_id) {
        $.post(del_post_url,
        {
            post_id: post_id
        },
        function () {
            var index = null;
            for (var i = 0; i < self.vue.posts.length; i++) {
                if (self.vue.posts[i].id === post_id) {
                    // If I set this to i, it won't work, as the if below will
                    // return false for items in first position.
                    index = i + 1; //just in case it's the zero'th element
                    break;
                }
            }
            if (index) {
                // delete the element associated with the id
                self.vue.posts.splice(index - 1, 1);
                //if posts length is less that 11 has_more is false
                if (self.vue.posts.length < 11) {
                    self.vue.has_more = false;
                }
            }
        }
        )
    };


    ///END OF ATTEMPT 1

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            posts: [],
            get_more: false,
            logged_in: false,
            editing: false,
            is_adding_post: false,
            has_more: false,
            form_content: null,
            form_title:null, //////adding title from tyler 
            edit_content: null,
            is_public:null,
            edit_title: null,
            title:null, ///TEMP ADDITION
            edit_id: 0,
            show: true
        },
        methods: {
            get_more: self.get_more,
            add_post_button: self.add_post_button,
            add_post: self.add_post,
            delete_track: self.delete_track,
            edit_post: self.edit_post,
            get_zeroposts:self.get_zeroposts,
            edit_post_submit: self.edit_post_submit,
            cancel_edit: self.cancel_edit,
            cancel_add: self.cancel_add,
            toggle_post: self.toggle_post
        }

    });

    self.get_posts();
    $("#vue-div").show();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
