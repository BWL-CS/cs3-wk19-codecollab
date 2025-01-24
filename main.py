from flask import Flask, render_template, request, redirect, url_for

# For the CodeCollab, you can discuss anything in this Python script OR the HTML template!

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():

  input_schedule = {
      'Monday': ['Honors CS', 'Free', 'Free', 'AP Calculus', 'AP Literature'],
      'Tuesday': ['Robotics', 'Free', 'Comp Sci', 'Economics', 'Free'],
      'Wednesday': ['AP Calculus', 'Free', 'Robotics', 'Free', 'Comp Sci'],
      'Thursday': ['Free', 'AP Literature', 'Comp Sci', 'Robotics', 'PE'],
      'Friday': ['Economics', 'Robotics', 'Free', 'AP Calculus', 'AP Literature']
  }

  num_periods = max(len(day) for day in input_schedule.values())

  return render_template('index.html', schedule=input_schedule, periods=num_periods)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5421)
