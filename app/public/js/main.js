(function(window, $, Vue){
  'use strict';
  var ws, app;

  (function init(){
    ws = new WebSocket(GetWebSocketURL());

    app = new Vue({
      el: '#vote',
      data: {
        message: "Hello Vue.js",
        font:"",
        scores: [],
        vote: ""
      },
      methods:{
        magnify: function(){
            this.font = "font-size:20px;color:red"
        },
        addScore: function(item){
          var msg = {"name": item.name, "score": item.score+1};
          ws.send(JSON.stringify(msg));
        }
      }
    })
    addListener();
  })();


  function addListener() {
    ws.onmessage = function(e) {
      var scores = JSON.parse(e.data);
      app.scores = scores;
    };
  }

  function GetWebSocketURL() {
    var loc = window.location;
    return "ws://" + loc.host + "/wsentry";
  }

})(window, jQuery, Vue);
