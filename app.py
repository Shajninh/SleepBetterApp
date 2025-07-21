# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
import model



# -- Initialization section --
app = Flask(__name__)
name = ""
age = ""
sHour = ""
sMin = ""
sAP = ""
wHour = ""
wMin = ""
wAP = ""
slept_amount = 0
user_slept = ""
user_cycle = 0
user_times = ""
user_rec = ""

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
  if request.method == 'post':
    return 'Try again.'
  else:
    global name
    global age
    global sHour
    global sMin
    global sAP
    global wHour
    global wMin
    global wAP
    global slept_amount
    global user_slept
    global user_cycle
    global user_times
    global user_rec
    name = request.form['name']
    age = request.form['age']
    sHour = request.form['sleep hour']
    sMin = request.form['sleep minute']
    sAP = request.form['sAP']
    wHour = request.form['wake hour']
    wMin = request.form['wake minute']
    wAP = request.form['wAP']

    if not name.strip() or not age.strip() or not sHour.strip() or not sMin.strip() or not sAP.strip() or not wHour.strip() or not wMin.strip() or not wAP.strip():
      return redirect("https://calculator-final.kayleechen.repl.co")
  
    slept_amount = model.sleep_calc(int(sHour), int(sMin), sAP.upper(), int(wHour), int(wMin), wAP.upper())
    user_slept = model.user_sleep(slept_amount)
    user_cycle = model.cycle(int(sHour), int(sMin), sAP.upper(), int(wHour), int(wMin), wAP.upper())
    user_times = model.cycle_time(int(sHour), int(sMin), sAP.upper(), int(wHour), int(wMin), wAP.upper())
    print(user_times)
    user_rec = model.age_rec(int(age), int(sHour), int(sMin), sAP.upper(), int(wHour), int(wMin), wAP.upper())
    return render_template('results.html', name = name, slept_amount = slept_amount, user_cycle = user_cycle, user_slept = user_slept, user_times = user_times, user_rec = user_rec)

@app.route('/results2')
def results2():
  return render_template('results2.html', name = name, age = age, slept_amount = slept_amount, user_cycle = user_cycle, user_slept = user_slept, user_times = user_times, user_rec = user_rec)

@app.route('/results3')
def results3():
  return render_template('results3.html', name = name, age = age, slept_amount = slept_amount, user_cycle = user_cycle, user_slept = user_slept, user_times = user_times, user_rec = user_rec)

@app.route('/test')
def test():
  return render_template('test.html', name = name, age = age, slept_amount = slept_amount, user_cycle = user_cycle, user_slept = user_slept, user_times = user_times, user_rec = user_rec)
  

# Keeps us in debug mode
app.run(host='0.0.0.0', port=81, debug=True)