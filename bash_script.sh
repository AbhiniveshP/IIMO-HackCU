gcloud dataflow jobs run files_deliveries-pubsub \
--gcs-location gs://dataflow-templates/latest/GCS_Text_to_Cloud_PubSub \
--parameters inputFilePattern=gs://cuhack/json_files/*.json,outputTopic=projects/dcsc-254706/topics/deliveries

gcloud dataflow jobs run files_matches-pubsub\
 --gcs-location gs://dataflow-templates/latest/GCS_Text_to_Cloud_PubSub\
  --parameters inputFilePattern=gs://cuhack/json_files_matches/*.json,outputTopic=projects/dcsc-254706/topics/matches

gsutil -m cp -r json_files_matches gs://cuhack

gsutil -m cp -r json_files_deliveries gs://cuhack