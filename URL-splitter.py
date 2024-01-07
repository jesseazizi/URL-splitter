"""
Created on Thu Feb 20 16:29:48 2023

@author: jesseazizi
"""

def URL_splitter(handles,delimiter,URL,per_URL,URL_separator):
    
    # Keeps track of which URL to add handles to
    current_URL_index=-1
    
    # Contains all of the URLs that will be created
    URLs=[]
    
    # Compiling all of the handles into a list
    new_handles=handles.split(delimiter)
    
    # Writing all of the URLs into the URLs list:
    # For every element in new_handles...
    for i in range(len(new_handles)): 

        # Append the URL separator to the end of the element
        new_handles[i]+=str(URL_separator) 

        # If we've reached the maximum number of handles per URL...
        if (i%per_URL)==0: 
           
           # Increment current_URL_index by 1
           current_URL_index=current_URL_index+1 
           
           # Append a new element to URLs containing just the beginning of the URL
           URLs+=[URL] 
           
           # Append a forward slash to the new element in URLs
           URLs[current_URL_index]+="/"

        # Append a handle (including the comma) to the current URL
        URLs[current_URL_index]+=new_handles[i]

    # Remove the extra separator at the end of each URL
    for i in range(len(URLs)):
        URLs[i]=URLs[i][0:len(URLs[i])-1]
        
    # Return the new list of URLs
    return URLs
        
def main():
    the_handles=open("/Users/jesseazizi/Documents/root/software/Scripts/Python Scripts/URL-splitter/handles.txt","r")
    print(URL_splitter(the_handles.read(),"\n","invidious.fi",20,","))
    
main()