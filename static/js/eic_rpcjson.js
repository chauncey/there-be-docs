
YUI.add('eic_rpcjson', function(Y) {
  var rpc = Y.namespace('Rpc');

  var callback = {
    method: 'post',
    timeout: 3000,
    sync: true,
    headers: { 'Content-Type': 'application/json'}
  }

  rpc.send = function(uri, data) {
    callback.data = data;
    request = Y.io(uri, callback);
    rpc.resp = Y.JSON.parse(request.responseText);
  }

});
