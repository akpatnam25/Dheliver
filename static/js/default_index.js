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

    self.log_time = function (event){
        self.vue.time = event.target.name;
        if (self.vue.location === 'cowell'){
          self.vue.cowell = true;
          self.vue.crown = false;
          self.vue.ten = false;
          self.vue.porter = false;
          self.vue.rcc = false;
        }
        else if (self.vue.location === 'crown'){
          self.vue.cowell = false;
          self.vue.crown = true;
          self.vue.ten = false;
          self.vue.porter = false;
          self.vue.rcc = false;
        }
        else if (self.vue.location === 'ten'){
          self.vue.cowell = false;
          self.vue.crown = false;
          self.vue.ten = true;
          self.vue.porter = false;
          self.vue.rcc = false;
        }
        else if (self.vue.location === 'porter'){
          self.vue.cowell = false;
          self.vue.crown = false;
          self.vue.ten = false;
          self.vue.porter = true;
          self.vue.rcc = false;
        }
        else {
          self.vue.cowell = false;
          self.vue.crown = false;
          self.vue.ten = false;
          self.vue.porter = false;
          self.vue.rcc = true;
        }
        if (self.vue.time === 'breakfast'){
          self.vue.breakfast = true;
          self.vue.lunch = false;
          self.vue.dinner = false;
        }
        else if (self.vue.time === 'lunch'){
          self.vue.breakfast = false;
          self.vue.lunch = true;
          self.vue.dinner = false;
        }
        else {
          self.vue.breakfast = false;
          self.vue.lunch = false;
          self.vue.dinner = true;
        }
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
          cowell: false,
          crown: false,
          ten: false,
          porter: false,
          rcc: false,
          breakfast: false,
          lunch: false,
          dinner: false
        },
        methods: {
          log_location: self.log_location,
          log_time: self.log_time,
          cash_order: function (event) {
              alert('Your order has been processed as a cash payment! Please pay $5 when the delivery arrives. Thankyou for using Dheliver!')
          }
        }

    });

    $("#vue-div").show();
    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
