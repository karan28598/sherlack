import os  
import wolframalpha 

from flask import Flask, request, Response, redirect


try:
    import config       # Import config.py file 
    wol_id = config.wolframalpha['app_id']   # assign APP_ID from config.py to wol_id
except:
    wol_id = os.environ.get('APP_ID')   # load envoironment variable


if not wol_id:        # if wol_id is not present display error and exit
    import sys
    print 'No config.py found exisiting...'
    sys.exit(0)


app = Flask(__name__)     # initiate flask app

client = wolframalpha.Client(wol_id)      # this is from Wolframa moudule. Initiate Client using Wol_id


@app.route('/sherlack',methods=['post'])
def sherlack():
    text = request.values.get('text')    # Get Query
    try:
        res = client.query(text)       # Get result from Wolframalpha API.
    except UnicodeEncodeError:    # if coudln't get the response show error.
        return Response(('Sorry I did\'t get you. Would you please simplify your query?'
                        '%s is not valid input.' % text),
                        content_type='text\plain; charset=utf-8')
    resp_qs = ['Top Answer for "%s"\n' % text]    # if Query is successful show result.
    resp_qs.extend(next(res.results).text)     # iterate the result 

    return Response(''.join(resp_qs),
                    content_type='text/plain; chatset=utf-8')     # return response.

@app.route('/')
def hello():      # if someone tries to open the link directy redirect him somewhere 
    return redirect('https://github.com/karan28598/sherlack')


if __name__ == '__main__':   
    port = int(os.environ.get('PORT',5000))    # run your app on local
    app.run(host='0.0.0.0', port=port)