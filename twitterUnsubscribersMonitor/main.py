from google.cloud import storage
import datetime
import twint
import json

storage_client = storage.Client()
bucket = storage_client.get_bucket('twitter_followers')


def get_followers(request):
    c = twint.Config()
    c.Username = 'robimalco'
    c.Pandas = True
    c.Hide_output = True
    twint.run.Followers(c)
    Followers_df = twint.storage.panda.Follow_df
    blob_json = json.dumps({
        'followers': Followers_df.loc[Followers_df.index[0], 'followers']
    })
    date = datetime.datetime.now()
    blob_name = str(date)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(json.dumps(blob_json))
    return 'OK'
