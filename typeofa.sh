hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-files /home/hadoop/Desktop/mtypeofa.py,/home/hadoop/Desktop/rtypeofa.py \
-mapper mtypeofa.py \
-reducer rtypeofa.py \
-input /home/hadoop/Desktop/data.csv \
-output /output

