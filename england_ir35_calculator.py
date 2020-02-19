rate=630
amount=(20*12*rate)
employerNiBracket={(0,719*12):0,(719.01*12,1000000):13.8}
employeeNiBracket={(0,719*12):0,(719.01*12,4167*12):12,(4167.01*12,1000000):2}
taxBracket={(0,50000):20,(50001,150000):40,(150000,1000000):45}

employerNi=[ (min(amount,band[1])-band[0])*.01*employerNiBracket[band] for band in employerNiBracket.keys() if amount>=band[0]]
employerNiAmount=sum(employerNi)
print("employerNi for brackets" + str(employerNi) + ",sum:" + str(employerNiAmount) + ",employerNi %" + str(employerNiAmount/amount))

employerNiAdjustedAmt=amount-employerNiAmount
print("employer ni adjusted gross "+ str(employerNiAdjustedAmt))

tax=[ (min(employerNiAdjustedAmt,band[1])-band[0])*.01*taxBracket[band] for band in taxBracket.keys() if employerNiAdjustedAmt>=band[0]]
taxAmount=sum(tax)
print("tax for brackets" + str(tax) + ",sum:" + str(taxAmount) + ",tax %" + str(taxAmount/amount))

employeeNi=[ (min(employerNiAdjustedAmt,band[1])-band[0])*.01*employeeNiBracket[band] for band in employeeNiBracket.keys() if employerNiAdjustedAmt>=band[0]]
employeeNiAmount=sum(employeeNi)
print("employeeNi for brackets" + str(employeeNi) + ",sum:" + str(employeeNiAmount) + ",employeeNi %" + str(employeeNiAmount/amount))


apprenticeShipLevy=.005*employerNiAdjustedAmt

print("Apprenticeship levy at .05% " + str(apprenticeShipLevy))
takeHome=amount-taxAmount-employeeNiAmount-employerNiAmount-apprenticeShipLevy

print("take home per month " + str(takeHome/12) + ",% take home " + str(takeHome/amount))
