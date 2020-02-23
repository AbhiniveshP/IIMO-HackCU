import requests
import json
import base64


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    post_request_headers = {"Content-Type": "application/json"}
    es_url = 'http://35.184.166.246:3718'
    es_index = 'matches'
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(type(pubsub_message), pubsub_message)
    pub_json = json.loads(pubsub_message)
    match_info_response = requests.get(
        "http://35.184.166.246:3718/matches/_doc/{}".format(int(pub_json['match_id']))).json()

    # update the entire dictionary only if the match id is found
    if match_info_response['found']:
        match_info = match_info_response['_source']

        # Initialize batsman and bowler dictionaries to setup a player's combined profile
        if pub_json['batsman'] not in match_info:
            match_info[pub_json['batsman']] = {}
        if pub_json['bowler'] not in match_info:
            match_info[pub_json['bowler']] = {}

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total runs (innings 1 and 2 separately), in parallel with balls faced if the player is a batsman
        if 'total_runs_inn1' not in match_info:
            match_info['total_runs_inn1'] = 0
        if 'total_runs_inn2' not in match_info:
            match_info['total_runs_inn2'] = 0
        if 'total_runs' not in match_info:
            match_info['total_runs'] = 0
        if 'total_runs' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_runs'] = 0
        if 'balls_faced' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['balls_faced'] = 0

        #   Update total runs (innings 1 and 2 separately), in parallel with balls faced if the player is a batsman
        if pub_json['inning'] == 1:
            match_info['total_runs_inn1'] += pub_json['total_runs']
        if pub_json['inning'] == 2:
            match_info['total_runs_inn2'] += pub_json['total_runs']
        match_info['total_runs'] += pub_json['total_runs']
        match_info[pub_json['batsman']]['total_runs'] += pub_json['total_runs']
        match_info[pub_json['batsman']]['balls_faced'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initilalize total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the entire match to zero
        if 'total_0s' not in match_info:
            match_info['total_0s'] = 0
        if 'total_1s' not in match_info:
            match_info['total_1s'] = 0
        if 'total_2s' not in match_info:
            match_info['total_2s'] = 0
        if 'total_3s' not in match_info:
            match_info['total_3s'] = 0
        if 'total_4s' not in match_info:
            match_info['total_4s'] = 0
        if 'total_5s' not in match_info:
            match_info['total_5s'] = 0
        if 'total_6s' not in match_info:
            match_info['total_6s'] = 0

        #   Initialize total 0s, 1s, 2s, 3s, 4s, 5s and 6s of the batsman for the entire match to zero
        if 'total_0s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_0s'] = 0
        if 'total_1s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_1s'] = 0
        if 'total_2s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_2s'] = 0
        if 'total_3s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_3s'] = 0
        if 'total_4s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_4s'] = 0
        if 'total_5s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_5s'] = 0
        if 'total_6s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_6s'] = 0

        #   Update total 0s, 1s, 2s, 3s, 4s, 5s and 6s of the match along with the corresponding batsman accordingly
        if pub_json['total_runs'] == 0:
            match_info['total_0s'] += 1
            match_info[pub_json['batsman']]['total_0s'] += 1
        if pub_json['total_runs'] == 1:
            match_info['total_1s'] += 1
            match_info[pub_json['batsman']]['total_1s'] += 1
        if pub_json['total_runs'] == 2:
            match_info['total_2s'] += 1
            match_info[pub_json['batsman']]['total_2s'] += 1
        if pub_json['total_runs'] == 3:
            match_info['total_3s'] += 1
            match_info[pub_json['batsman']]['total_3s'] += 1
        if pub_json['total_runs'] == 4:
            match_info['total_4s'] += 1
            match_info[pub_json['batsman']]['total_4s'] += 1
        if pub_json['total_runs'] == 5:
            match_info['total_5s'] += 1
            match_info[pub_json['batsman']]['total_5s'] += 1
        if pub_json['total_runs'] >= 6:
            match_info['total_6s'] += 1
            match_info[pub_json['batsman']]['total_6s'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initilalize total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the first innings to zero
        if 'total_0s_inn1' not in match_info:
            match_info['total_0s_inn1'] = 0
        if 'total_1s_inn1' not in match_info:
            match_info['total_1s_inn1'] = 0
        if 'total_2s_inn1' not in match_info:
            match_info['total_2s_inn1'] = 0
        if 'total_3s_inn1' not in match_info:
            match_info['total_3s_inn1'] = 0
        if 'total_4s_inn1' not in match_info:
            match_info['total_4s_inn1'] = 0
        if 'total_5s_inn1' not in match_info:
            match_info['total_5s_inn1'] = 0
        if 'total_6s_inn1' not in match_info:
            match_info['total_6s_inn1'] = 0

        #   Update total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the first innings accordingly
        if pub_json['total_runs'] == 0 and pub_json['inning'] == 1:
            match_info['total_0s_inn1'] += 1
        if pub_json['total_runs'] == 1 and pub_json['inning'] == 1:
            match_info['total_1s_inn1'] += 1
        if pub_json['total_runs'] == 2 and pub_json['inning'] == 1:
            match_info['total_2s_inn1'] += 1
        if pub_json['total_runs'] == 3 and pub_json['inning'] == 1:
            match_info['total_3s_inn1'] += 1
        if pub_json['total_runs'] == 4 and pub_json['inning'] == 1:
            match_info['total_4s_inn1'] += 1
        if pub_json['total_runs'] == 5 and pub_json['inning'] == 1:
            match_info['total_5s_inn1'] += 1
        if pub_json['total_runs'] >= 6 and pub_json['inning'] == 1:
            match_info['total_6s_inn1'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initilalize total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the second innings to zero
        if 'total_0s_inn2' not in match_info:
            match_info['total_0s_inn2'] = 0
        if 'total_1s_inn2' not in match_info:
            match_info['total_1s_inn2'] = 0
        if 'total_2s_inn2' not in match_info:
            match_info['total_2s_inn2'] = 0
        if 'total_3s_inn2' not in match_info:
            match_info['total_3s_inn2'] = 0
        if 'total_4s_inn2' not in match_info:
            match_info['total_4s_inn2'] = 0
        if 'total_5s_inn2' not in match_info:
            match_info['total_5s_inn2'] = 0
        if 'total_6s_inn2' not in match_info:
            match_info['total_6s_inn2'] = 0

        #   Update total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the second innings accordingly
        if pub_json['total_runs'] == 0 and pub_json['inning'] == 2:
            match_info['total_0s_inn2'] += 1
        if pub_json['total_runs'] == 1 and pub_json['inning'] == 2:
            match_info['total_1s_inn2'] += 1
        if pub_json['total_runs'] == 2 and pub_json['inning'] == 2:
            match_info['total_2s_inn2'] += 1
        if pub_json['total_runs'] == 3 and pub_json['inning'] == 2:
            match_info['total_3s_inn2'] += 1
        if pub_json['total_runs'] == 4 and pub_json['inning'] == 2:
            match_info['total_4s_inn2'] += 1
        if pub_json['total_runs'] == 5 and pub_json['inning'] == 2:
            match_info['total_5s_inn2'] += 1
        if pub_json['total_runs'] >= 6 and pub_json['inning'] == 2:
            match_info['total_6s_inn2'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total extras and total wickets for the entire match
        if 'total_extras' not in match_info:
            match_info['total_extras'] = 0
        if 'total_wickets' not in match_info:
            match_info['total_wickets'] = 0

        #   Update total extras and total wickets for the entire match
        if pub_json['extra_runs'] != 0:
            match_info['total_extras'] += pub_json['extra_runs']
        if pub_json['dismissal_kind'] != 'Not Dismissed':
            match_info['total_wickets'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total extras and total wickets for the first innings
        if 'total_extras_inn1' not in match_info:
            match_info['total_extras_inn1'] = 0
        if 'total_wickets_inn1' not in match_info:
            match_info['total_wickets_inn1'] = 0

        #   Update total extras and total wickets for the first innings
        if pub_json['extra_runs'] != 0 and pub_json['inning'] == 1:
            match_info['total_extras_inn1'] += pub_json['extra_runs']
        if pub_json['dismissal_kind'] != 'Not Dismissed' and pub_json['inning'] == 1:
            match_info['total_wickets_inn1'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total extras and total wickets for the second innings
        if 'total_extras_inn2' not in match_info:
            match_info['total_extras_inn2'] = 0
        if 'total_wickets_inn2' not in match_info:
            match_info['total_wickets_inn2'] = 0

        #   Update total extras and total wickets for the second innings
        if pub_json['extra_runs'] != 0 and pub_json['inning'] == 2:
            match_info['total_extras_inn2'] += pub_json['extra_runs']
        if pub_json['dismissal_kind'] != 'Not Dismissed' and pub_json['inning'] == 2:
            match_info['total_wickets_inn2'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize and update balls bowled of a particular player if balls bowled
        if 'balls_bowled' not in match_info[pub_json['bowler']]:
            match_info[pub_json['bowler']]['balls_bowled'] = 0

        match_info[pub_json['bowler']]['balls_bowled'] += 1
        #   -------------------------------------------------------------------------------------------------------    #


        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize or update number of wickets for a player if wicket taken
        if pub_json['dismissal_kind'] != 'Not Dismissed':
            if 'wickets' in match_info[pub_json['bowler']]:
                match_info[pub_json['bowler']]['wickets'] += 1
            else:
                match_info[pub_json['bowler']]['wickets'] = 1
        #   -------------------------------------------------------------------------------------------------------    #

        insert_request = requests.post(url="{}/{}/_doc/{}".format(es_url, es_index, match_info['match_id']),
                                       data=json.dumps(match_info),
                                       headers=post_request_headers).json()
        print(insert_request)