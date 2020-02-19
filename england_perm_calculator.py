amount=66000
taxBracket={(0,12500):0,(12501,50000):20,(50001,150000):40,(150000,1000000):45}
employeeNiBracket={(0,719*12):0,(719.01*12,4167*12):12,(4167.01*12,1000000):2}



tax=[ (min(amount,band[1])-band[0])*.01*taxBracket[band] for band in taxBracket.keys() if amount>=band[0]]
taxAmount=sum(tax)
print("tax for brackets" + str(tax) + ",sum:" + str(taxAmount) + ",tax %" + str(taxAmount/amount))

employeeNi=[ (min(amount,band[1])-band[0])*.01*employeeNiBracket[band] for band in employeeNiBracket.keys() if amount>=band[0]]
employeeNiAmount=sum(employeeNi)
print("employeeNi for brackets" + str(employeeNi) + ",sum:" + str(employeeNiAmount) + ",employeeNi %" + str(employeeNiAmount/amount))



takeHome=amount-taxAmount-employeeNiAmount

print("take home per month " + str(takeHome/12) + ",% take home " + str(takeHome/amount))
