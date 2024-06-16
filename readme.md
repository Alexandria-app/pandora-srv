# Pandora server

A minimal python socket server that can load arbitrary python scripts, enabling scripting via python in flutter apps.


## Message passing

The server sends and receives data in the following manner,

* All messages are `utf-8` encoded. 

#### Request 

(length\<space>\content) :

    length : length of the *bytes* of the content
    
    content : the message in bytes utf-8 encoded

*Note only the first space will be considered in case of a request*

eg : 
    
    0 44 What do you get if you multiply six by nine?

#### Response 

(result\<space>\length\<space>\content) :

    result : if there is a error 1, 0 otherwise 
    
    length : length of the *bytes* of the content
    
    content : the message in bytes utf-8 encoded

*Note only the first 2 spaces will be considered in case of a response*
 
eg : 
    
    # successfull response
    0 2 42

    # error response 
    1 5 error 
    

## Directory structure 

Most files and folders outside the `app` dir are CI configuration files and generally should not be touched.

the `test` and the `app` dirs are the core of the application.
