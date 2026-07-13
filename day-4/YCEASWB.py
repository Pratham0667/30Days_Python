
text = "You cannot end a sentence with because because because is a conjunction"

becOcc = text.index("because")
print(f"THE 1st OCC OF BECUASE : {becOcc}")

lastOcc = text.rfind("because")
print(f"LAST OCC OF BECAUSE : {lastOcc}")


sliced = text.find("because because because")
printing = text[sliced : sliced+len("because because because")]
print(f"PHASE ONLY BECUASE : {printing}")


