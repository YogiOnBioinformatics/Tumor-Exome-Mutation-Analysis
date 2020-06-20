"""
Author: Yogindra Raghav
"""

import pandas
import os 

# if main program being run 
if __name__ =="__main__": 

    """
    Loading Files
    """
    # change directory 
    os.chdir("vanallen-assessment/mafs/")
    # prefix of file names 
    prefix = os.path.abspath(os.curdir)+"/Patient-" 
    # replace backwards slashes with forwards slashes 
    prefix = prefix.replace("\\\\", "/") 
    prefix = prefix.replace("\\", "/") 
    # suffix of file names 
    suffix = ".somatic.snvs.maf"
    # maintain list of Pandas dataframes
    pandas_list = []

    # for loop to load all files 
    for num in range(0,50): 
        # create full file name 
        file_name = prefix+str(num)+suffix
        # load file 
        temp_file = pandas.read_table(file_name, sep="\t", header=0)
        # append to list 
        pandas_list.append(temp_file)

    """
    Appending All Dataframes To One Dataframe
    """
    # create empty variable 
    appended_dataframe = None 
    # iteratively append all dataframes 
    for table in pandas_list: 
        # if first time 
        if appended_dataframe is None: 
            appended_dataframe = table
        # append 
        else: 
            appended_dataframe = appended_dataframe.append(table, ignore_index=True)
  
    """
    Subseting For Non-Silent Mutations
    """
    # subset for non-silent mutations 
    non_silent= \
        appended_dataframe[appended_dataframe.Variant_Classification!=\
        "Silent"]
    """

    index_list = []
    for num in range(0, 11247): 
        index_list.append(num)
    
    non_silent = non_silent.reindex(index_list)
    
    # get value counts of each gene 
    common_mutations = \
        non_silent.query('Hugo_Symbol').value_counts()
	
	"""
    
    print(non_silent)
    