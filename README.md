This repository is used for the storage of files involed in Brett Philips and Jonah Whites AI Project. 
#file descriptions

AIproj.*** files are where the primary model training is happending
Concurrentproj.ipynb is used to train the select model over every year of the dataset
  (note: due to the size of the data set this will take multiple hours and will likely need to be done in atleast 2 baches)
stkdgraph.py is used to generate the graphs compare the data in a by year basis




#additional notes

This code segment is the primary method by which the dataset is being accessed.
##############
import kagglehub
# Download latest version
path = kagglehub.dataset_download("aliafzal9323/chicago-crime-dataset-2024-2026")
#path is /kaggle/input/chicago-crime-dataset-2024-2026/chicago crimes.csv
print("Path to dataset files:", path)

#params: ID Case Number, Date, Block, IUCR, Primary Type, Description, Location Description, Arrest, Domestic, Ward, Community Area,
#FBI Code,  X Coordinate, Y Coordinate,  Year, Updated On, Latitude ,Longitude, Location

df = pd.read_csv(path + "/chicago crimes.csv")
##############

