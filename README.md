# NASA-Hydrology-Challenge

Currently the script written includes a function for requesting a response and downloading the comma separated value file from the URL
provided and a function to create a list of the values held in the file’s rows beyond the first. These were separated for the sake of
creating tests that ensure the URL can be reached and that the format of the data is being provided exactly as promised and expected. The
final function prints out the combined results of the above formatted crudely for readability. Currently, the only evaluation of the
provided data is taking the cosine of the second value in each row and it is included in the print function for the sake of simplicity but
adding functions to reach more complicated conclusions could be written and employed neatly within this function. 
Overall, every file included is simple but written with the expectation of increased complexity in future iterations. The objective results
of the code are not spectacular, but the steps taken to make it accessible by all and the anticipation of challenges to come demonstrate
how this could be an effective way to publish more complex code while maintaining robustness. 
