(function(window, $, Vue){
  'use strict';
  var ws, app;

  (function init(){
    ws = new WebSocket(GetWebSocketURL());

    app = new Vue({
      el: '#simple',
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
    // var msg = {"x":e.clientX+scroll_pos.x, "y": e.clientY+scroll_pos.y}
    //ws.send(JSON.stringify(msg));
    console.log("Yeah", app.message);

    ws.onmessage = function(e) {
      console.log("recieved message: ", e.data);
      var scores = JSON.parse(e.data);
      app.scores = scores;
    };
  }

  function GetWebSocketURL() {
    var loc = window.location;
    return "ws://" + loc.host + "/wsentry";
  }

})(window, jQuery, Vue);
