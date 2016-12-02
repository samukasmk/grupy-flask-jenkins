from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return '''
<h1>Welcome to silly project of Samuka!</h1>
<p>Avaliable endpoints:</p>
<ul>
  <li><b>/</b> - this page</li>
  <li><b>/ping</b> - example of rest api with json response</li>
  <li><b>/modal</b> - exemple of html divs</li>
</ul>

<h3>More contacts: samuel@smk.net.br</h3>
'''

@app.route('/ping')
def ping():
    return jsonify(ping='pong')

@app.route('/modal')
def modal():
    return """
    <html>
    <head></head>
    <body>
    <!-- Modal content-->
    <div class="modal-content">
      <div class="modal-header">
        <h4 id="modal-title" class="modal-title">Modal Header</h4>
      </div>
      <div class="modal-body">
        <p>Some text in the modal.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
      </div>
    </div>
    </body>
    </html>"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
