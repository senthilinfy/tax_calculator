def calculate(calc_type,amount, bracket):
  result=[ (min(amount,band[1])-band[0])*.01*bracket[band] for band in bracket.keys() if amount>=band[0]]
  resultSum=sum(result)
  print(calc_type+ "for brackets" + str(result) + ",sum:" + str(resultSum) + ",tax %" + str(resultSum/amount))
  return resultSum

rate=500
amount=(20*12*rate)
employerNiBracket={(0,719*12):0,(719.01*12,1000000):13.8}
employeeNiBracket={(0,719*12):0,(719.01*12,4167*12):12,(4167.01*12,1000000):2}
taxBracket={(0,50000):20,(50001,150000):40,(150000,1000000):45}

employerNiAmount=calculate("employerni", amount,employerNiBracket)
employerNiAdjustedAmt=amount-employerNiAmount
taxAmount=calculate("tax", employerNiAdjustedAmt, taxBracket)
employeeNiAmount=calculate("employeeni", employerNiAdjustedAmt, employeeNiBracket)

apprenticeShipLevy=.005*employerNiAdjustedAmt
print("Apprenticeship levy at .05% " + str(apprenticeShipLevy))

takeHome=amount-taxAmount-employeeNiAmount-employerNiAmount-apprenticeShipLevy
print("take home per month " + str(takeHome/12) + ",% take home " + str(takeHome/amount))
