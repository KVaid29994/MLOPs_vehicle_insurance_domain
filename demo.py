# #below code is to check the logging config
# from src.logger import logging

# logging.debug("This is a debug message.")
# # logging.info("This is an info message.")
# # logging.warning("This is a warning message.")
# # logging.error("This is an error message.")
# # logging.critical("This is a critical message.")

# # # below code is to check the exception config
# from src.logger import logging
# from src.exception import MyException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise MyException(e, sys) from e


from src.pipline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()

# from pymongo import MongoClient
# client = MongoClient("mongodb+srv://kanhavaid:nJDJ3axxgLzCq23M@cluster0.bfctecs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# db = client["Proj1"]
# collection = db["Proj1-data"]
# print(collection.count_documents({}))

# from src.pipline.training_pipeline import TrainPipeline

# if __name__ == "__main__":
#     pipeline = TrainPipeline()
#     pipeline.run_pipeline()
#     print("✅ Training pipeline executed successfully.")