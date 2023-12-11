hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files /home/hadoop/Desktop/mcountacc.py,/home/hadoop/Desktop/rcountacc.py \
-mapper mcountacc.py \
-reducer rcountacc.py \
-input /home/hadoop/Desktop/data.csv \
-output /output

