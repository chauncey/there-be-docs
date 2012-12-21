//$Id$

YUI.add('yui-help', function(Y) {
  var help = Y.namespace('Help');
  help.init = function (txt) {
    var fin = function(e) {
      e.preventDefault();
      if( typeof helptxt[e.target.get('id')] != 'undefined' ) {
        panel.set('bodyContent', '<div id="yuihelp">' + helptxt[e.target.get('id')] + '</div>');
        panel.show();
      }
    };
    var panel = new Y.Overlay({
      srcNode: document.BODY,
      width: "200px",
      visible: false,
      close: false
    });
    panel.render().hide();
    panel.set('align', {points: [Y.WidgetPositionAlign.TR, Y.WidgetPositionAlign.TR]});
    Y.one('form').delegate('focus', fin, 'input');
    Y.one('form').delegate('blur', function(){panel.hide();}, 'input');
    Y.one(document.body).delegate('mouseover', fin, 'form');
    Y.one(document.body).delegate('mouseout', function(){panel.hide();}, 'form');
  }
});

