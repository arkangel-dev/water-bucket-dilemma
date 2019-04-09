import random
import time

bucket_volume = [3,5]
bucket_empty = [3,5]
bucket_amount = [0,0]

def transfer_water(bucketb, bucketa, dump_excess):
	#print("Transferring Water :")
	if dump_excess != True:
		# bucketa.amount += bucketb.amount
		# if bucketa.amount > bucketa.volume:
		#	bucketb.amount = bucketa.amount - bucketa.volume
		# else:
		#	bucketb.amount = 0
		bucket_amount[bucketa] += bucket_amount[bucketb]
		if bucket_amount[bucketa] > bucket_volume[bucketa]:
			bucket_amount[bucketb] = bucket_amount[bucketa] - bucket_volume[bucketa]
			bucket_amount[bucketa] = bucket_volume[bucketa]
		else:
			bucket_amount[bucketb] = 0
	else:
		# bucketa.amound += bucketb.amount
		# if bucketa.amount > bucketa.volume:
		#	bucketa.amount = bucketa.volume
		# bucketb.amount = 0
		bucket_amount[bucketa] += bucket_amount[bucketb]
		if bucket_amount[bucketa] > bucket_volume[bucketa]:
			bucket_amount[bucketa] = bucket_volume[bucketa]
		bucket_amount[bucketb] = 0

def fill_bucket(bucket_index):
	#print("Filling bucket")
	bucket_amount[bucket_index] = bucket_volume[bucket_index]
	
def dump_bucket(bucket_index):
	#print("Dumping water")
	bucket_amount[bucket_index] = 0
	
continue_main_loop = True
continue_sub_loop = True
action_choices = [1,2,3]
bucket_choices = [0,1]
overflow = [True, False]
steps = 0
stepList = []
target = 4

while continue_main_loop:
	while continue_sub_loop:
		steps += 1
		current_action = 0
		# choices are the following:
		# if both buckets are empty:
		#	fill up random bucket...
		# if one bucket is filled:
		# 	transfer_water...
		# if either bucket has water:
		#	transfer_water...
		# if both buckets are filled:
		#	dump a water bucket...
		
		action = random.choice(action_choices)
		bucket = random.choice(bucket_choices)

		if action == 1:
			fill_bucket(bucket)
		elif action == 2:
			dump_bucket(bucket)
		elif action == 3:
			if bucket == 0:
				transf_a = 0
				transf_b = 1
			else:
				transf_a = 1
				transf_b = 0 
			dump_overflow = random.choice(overflow)
			transfer_water(transf_a, transf_b, dump_overflow)
		if action == 3:
			output = " Action : " + str(action) + " | " + str(transf_a) + " => " + str(transf_b) + " | " + str(dump_overflow)
		else:
			output = " Action : " + str(action)
		stepList.append(str(bucket_amount[0]) + " " + str(bucket_amount[1]) + output)
		for x in bucket_amount:
			if x == target:
				print("SOLUTION FOUND IN " + str(steps) + " STEPS!")
				continue_main_loop = False
				continue_sub_loop = False
		#time.sleep(0.5)
		break

printData = "DUMP : \n"
for x in stepList:
	printData += x + "\n"
print(printData)
print("SIMULATION DONE")
	
