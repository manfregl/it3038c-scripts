
#!/bin/bash

# This scipt downloads covid data and displays it


DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
PENDING=$(echo $DATA | jq '.[0].pending')
ICURN=$(echo $DATA | jq '.[0].inIcuCurrently')
TODAY=$(date)


echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negtive COVID cases and $PENDING pending cases. There are currently $ICURN people in the ICU right now. "
