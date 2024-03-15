#Define two empty lists for the time for top and bottom chambers
TstoreBOT = []
TstoreBOT = []
countsBOT = []
CountsBOT = []

with open('StorageCountBOTTOM.csv', 'r') as ifile:
    data = csv.reader(ifile)
    
    counter = 0
    for row in data:
        if counter == 1:
            
            TstoreBOT.append(float(row[0]))
            countsBOT.append(float(row[1]))

            
        else:
            counter+=1
            

with open('StorageCountTOP.csv', 'r') as ifile:
    data = csv.reader(ifile)
    
    counter = 0
    for row in data:
        if counter == 1:
            
            TstoreBOT.append(float(row[0]))
            CountsBOT.append(float(row[1]))

            
        else:
            counter+=1
            
                  
TstoreBOT = np.asarray(TstoreBOT)
countsBOT = np.asarray(countsBOT)
TstoreBOT = np.asarray(TstoreBOT)
CountsBOT = np.asarray(CountsBOT)

Ttop_err = np.sqrt(countsTOP)
Tbot_err = np.sqrt(CountsBOT)


------------------------------------------------



plot.figure(dpi=300)
plot.scatter(TstoreBOT, CountsBOT, marker=None, label='Bottom Chamber')
plot.scatter(TstoreBOT, countsBOT, marker=None, label='Top Chamber')
plot.xlabel('Time')
plot.ylabel('Counts')
plot.title('Storage Counts for Top and Bottom Chambers')
plot.legend()
plot.show()


------------------------------------------------

N1TOP = 70000

def countsTOP(TstoreTOP, t, b): 
    
    CountsTOP = N1TOP*np.exp(-TstoreTOP/t)+b
    return CountsTOP


dof = len(TstoreTOP) - 2 



t_InitialGuess=95
b_InitialGuess=5

popt, pcov = optimize.curve_fit(countsTOP, TstoreTOP, CountsTOP, 
                                p0=[t_InitialGuess, b_InitialGuess], sigma=Ttop_err, maxfev=8000) 

t = popt[0] 
b = popt[1]
errors = np.sqrt(np.diag(pcov))
t_err = errors[0] 
b_err = errors[1]

y_fit = countsTOP(TstoreTOP, t, b)

plot.figure(dpi=300)
plot.errorbar(TstoreTOP, CountsTOP, yerr=Ttop_err, fmt='r.', label = "Top Storage Chamber")
plot.plot(TstoreTOP, y_fit, marker=None, label = "Top Chamber Fit") #draws a fitting line without discrete markers
plot.legend()
plot.ylabel('counts')
plot.xlabel('time')
plot.title('fits') 
plot.show()
