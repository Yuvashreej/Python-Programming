movie = ["Leo", "Jawan", "Leo", "Master", "Jawan", "Beast"]
duplicate=[]
for i in movie:
       count=movie.count(i)
       if count>1 and i not in duplicate:
           duplicate.append(i)
print(duplicate)
           
           
            
        
            
    
    