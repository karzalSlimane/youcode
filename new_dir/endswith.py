def ends_with(**kwargs):
   for key,value  in  kwargs.items():
       if value.endswith(".csv"):
           print(f"FILE {key} ENDS WITH .csv")
       else :
           print(f"file {key} entred does not match ")

ends_with(file1 = "slimane.csv",file2 =  "brocode" )
