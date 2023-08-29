"""
Created on Thu Feb 20 16:29:48 2023

@author: jesseazizi
"""

def nitter_splitter(handles,delimiter,URL,per_URL):
    
    current_URL_index=-1 # Keeps track of which URL to add handles to
    nitter_URLs=[] # Contains all of the nitter URLs that will be created
    
    # Compiling all of the handles into a list
    new_handles=handles.split(delimiter)
    
    # Writing all of the URLs into nitter_URLs
    for i in range(len(new_handles)): # For every element in new_handles...
        new_handles[i]+="," # Append a comma to the end of the element
        if (i%per_URL)==0: # If we've reached the maximum number of handles per URL...
           current_URL_index=current_URL_index+1 # Increment current_URL_index by 1
           nitter_URLs+=[URL] # Append a new element to nitter_URLs containing just the beginning of the URL
           nitter_URLs[current_URL_index]+="/" # Append a forward slash to the new element in nitter_URLs
        nitter_URLs[current_URL_index]+=new_handles[i] # Append a handle (including the comma) to the current URL
        
    # Return the new list of nitter URLs
    return nitter_URLs
        
def main():
    the_handles=open("handles.txt","r")
    print(nitter_splitter(the_handles.read(),"\n","nitter.lunar.icu",20))
    
main()