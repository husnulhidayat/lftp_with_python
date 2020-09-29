# slightly malformed input data
# date format 2020-2-23
# if input_start example start at 2020-02-28 and end date 2020-03-02, it's will be produced file (2020-02-28 until 2020-03-01)
input_start=$1
input_end=$2

# After this, startdate and enddate will be valid ISO 8601 dates,
# or the script will have aborted when it encountered unparseable data
# such as input_end=abcd
startdate=$(date -I -d "$input_start") || exit -1
enddate=$(date -I -d "$input_end")     || exit -1

d="$startdate"
while [ "$d" != "$enddate" ]; do 
  echo $d
  d=$(date -I -d "$d + 1 day")
  yesterday=$(date -I -d "$d - 1 day")
  mkdir -p $your_dir_loc
  sh init_load_v2.sh $yesterday
done
