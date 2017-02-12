import cvfy

app = cvfy.register('nongh:220.227.149.70:9799245:5001:8000:54.158.186.33')

@cvfy.crossdomain
@app.listen()
def concat():
        
    ## receiving the data
    alltext = cvfy.getTextArray()
   
    ## processing the data
    joined_and_uppercase = (alltext[0] + ' ' + alltext[1])
    
    ## sending back the data
    cvfy.sendTextArray([joined_and_uppercase])
    return 'OK'
        
app.run()
