aws lambda invoke --payload fileb://event.json \
--function-name grid-maker ./output.txt

aws lambda invoke --payload "{}" \
--function-name hello_world ./output.txt

aws log tail /var/log/hello_world --follow --format json
