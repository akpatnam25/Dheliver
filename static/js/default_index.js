// This is the js for the default/order.html view.

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
        var k=0;
        return v.map(function(e) {e._idx = k++;});
    };

    self.log_location = function (event) {
        self.vue.location = event.target.name;
        console.log(self.vue.location);
    };

    self.log_time = function (event) {
        self.vue.time = event.target.name;
        console.log(self.vue.time);
        console.log("SENDING");
        $.post(get_menu_url,
            {
              location: self.vue.location,
              time: self.vue.time
            },
            function (data){
              self.vue.menu = data;
              console.log(self.vue.menu);
              self.vue.show = true;
        })
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
          location: null,
          time: null,
          menu: [],
          show: false
        },
        methods: {
          log_location: self.log_location,
          log_time: self.log_time,
        }

    });

    $("#vue-div").show();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
