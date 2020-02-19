def calculate(amount, bracket):
  return [ (min(amount,band[1])-band[0])*.01*bracket[band] for band in bracket.keys() if amount>=band[0]]

rate=500
amount=(20*12*rate)
employerNiBracket={(0,719*12):0,(719.01*12,1000000):13.8}
employeeNiBracket={(0,719*12):0,(719.01*12,4167*12):12,(4167.01*12,1000000):2}
taxBracket={(0,50000):20,(50001,150000):40,(150000,1000000):45}

employerNi=calculate(amount,employerNiBracket)
employerNiAmount=sum(employerNi)
employerNiAdjustedAmt=amount-employerNiAmount
print("employerNi for brackets" + str(employerNi) + ",sum:" + str(employerNiAmount) + ",employerNi %" + str(employerNiAmount/amount))

tax=calculate(employerNiAdjustedAmt, taxBracket)
taxAmount=sum(tax)
print("tax for brackets" + str(tax) + ",sum:" + str(taxAmount) + ",tax %" + str(taxAmount/amount))

employeeNi=calculate(employerNiAdjustedAmt, employeeNiBracket)
employeeNiAmount=sum(employeeNi)
print("employeeNi for brackets" + str(employeeNi) + ",sum:" + str(employeeNiAmount) + ",employeeNi %" + str(employeeNiAmount/amount))

apprenticeShipLevy=.005*employerNiAdjustedAmt
print("Apprenticeship levy at .05% " + str(apprenticeShipLevy))

takeHome=amount-taxAmount-employeeNiAmount-employerNiAmount-apprenticeShipLevy 
print("take home per month " + str(takeHome/12) + ",% take home " + str(takeHome/amount))
