echo "Starting..."

offset=0
limit=100000
output_file="parking_violations.csv"
iteration=0

#get first 100000 rows and write to file
curl "https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?\$limit=${limit}&\$offset=${offset}" > "$output_file"

#get remaining data in increments of 1000 rows and append to file
while true; do
  iteration=$((iteration + 1))
  echo "Iteration: $iteration"

  #prepare API url
  api_url="https://data.cityofnewyork.us/resource/pvqr-7yc4.csv?\$limit=${limit}&\$offset=${offset}"

  #print API url to confirm offset is updating
  echo "API request URL: $api_url"

  #get data and append to file
  curl "$api_url" >> "$output_file"

  #check if all data is there
  if [ $(wc -l < "$output_file") -lt $((offset + limit)) ]; then
    echo "All data fetched."
    break
  fi

  #increment the offset
  offset=$((offset + limit))
done

echo "Data fetched and saved to $output_file"
