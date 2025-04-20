README - FDS Assignment II
Name: Manisha Bhalla
Roll Number: G24AI1073

Contents:
---------
1. mapper_task1.py - Cleansing and parsing user actions
2. reduce_task1.py: Simply pass through valid records for further processing
3. mapper_task2.py: Emit (UserID_ActionType) as key and count as value.
4. reduce_task2.py: Aggregate counts for each user-action pair.
5. mapper_task3.py Defines metric (likes + shares); uses thresholding and combiners for optimization.
6. mapper_task4.py Reduce-side join between activity logs and user profile; rationale
explained

To Run:
-------
Assuming Hadoop streaming:

hadoop jar hadoop-streaming.jar \
  -input social_media_logs.txt \
  -output output_dir \
  -mapper mapper1.py \
  -reducer reducer1.py

Ensure Python is executable and input files are available.
