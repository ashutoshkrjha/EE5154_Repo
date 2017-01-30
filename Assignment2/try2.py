# coding: utf-8

#Importing required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nc
import networkx as nx
df = pd.read_csv('isl_wise_train_detail_03082015_v1.csv')

#Creating list of source stations
source_station = df[[8]]
source_station = source_station.values.tolist()
source_station = [item for sublist in source_station for item in sublist]
source_station_set = list(set(source_station))

#Creating list of destination stations (from intermediate stations column)
destination_station = df[[10]]
destination_station = destination_station.values.tolist()
destination_station = [item for sublist in destination_station for item in sublist]
destination_station_set = list(set(destination_station))

#Creating final list of all stations
intermediate_station = df[[3]]
intermediate_station = intermediate_station.values.tolist()
intermediate_station = [item for sublist in intermediate_station for item in sublist]
all_stations = list(set(intermediate_station))

#Creating list of train numbers
train_numbers = df[[0]]
train_numbers = train_numbers.values.tolist()
train_numbers = [item for sublist in train_numbers for item in sublist]
train_numbers_set = list(set(train_numbers))


#Initializing Adjacency Matrix
A = np.zeros((len(all_stations),len(all_stations)))


for train_number in train_numbers_set:
	indexes = [i for i,x in enumerate(train_numbers) if x == train_number]
	length_indexes = len(indexes)
	flag_inner = length_indexes
	for index in indexes:
		src = intermediate_station[index]
		src_index = all_stations.index(src)
		for flag in range(1,flag_inner):
			dest = intermediate_station[index+flag_inner-1]
			dest_index = all_stations.index(dest)
			A[src_index,dest_index] += 1
		flag_inner -= 1

#Now making the intermediate stations as source and destinations as destination

