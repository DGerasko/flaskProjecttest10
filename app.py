from flask import Flask, jsonify
from google_sheets.google_sh import read_from_google_sheet, write_to_google_sheet
from github_api.github_info import get_github_user_info

app = Flask(__name__)

#Number of rows in our google sheet
cnt = 2


@app.route('/api/get_from_google_sheet', methods=['GET'])
def get_from_google_sheet():
    data = read_from_google_sheet(to_element=f"C{cnt}")
    return data


@app.route('/api/add_to_google_sheet/<string:name>', methods=['GET'])
def get_task(name):
    global cnt
    values = get_github_user_info(name)
    data = [
        {"range": f"A{cnt}:C{cnt}",
         "majorDimension": "COLUMNS",
         "values": [[values['login']], [values['id']], [values['url']]]}
    ]
    cnt = cnt + 1
    write_to_google_sheet(data=data)
    return jsonify({'values': values}), 201


if __name__ == '__main__':
    app.run()
