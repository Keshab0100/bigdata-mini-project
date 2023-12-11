hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files /home/hadoop/Desktop/msalecount.py,/home/hadoop/Desktop/rsalecount.py \
-mapper msalecount.py \
-reducer rsalecount.py \
-input /home/hadoop/Desktop/data.csv \
-output /output

