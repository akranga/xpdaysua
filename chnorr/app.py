from chalice import Chalice

import random

app = Chalice(app_name='chnorr')
app.debug = True



@app.route('/')
def index():
    return {'message': 'Herllo, I am mr. Norris'}

def read_facts_file():
  with open("chalicelib/index.txt") as f:
    return f.read().splitlines() 


facts = read_facts_file()



@app.route('/gimme/{num}')
def gimme_fact(num):
  num = int(num)
  return facts[num]



@app.route('/gimme')
def gimme_random_fact():
  num = random.randint(0, len(facts))
  return gimme_fact(num)





# @app.route('/req')
# def request():
#   return app.current_request.to_dict()
#   return app.current_request.stage_vars()



