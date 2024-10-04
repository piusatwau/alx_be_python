class abnormal_vitals(Exception):
    pass
def check_vitals(sbp):
    if sbp < 50:
        raise abnormal_vitals(f"SBP cannot be less than 50 mmg, {sbp} is too low, that patient is dead")

try:
    sbp = int(input("please enter the SBP of the patient: "))
    check_vitals(sbp)
    print(f"SBP is {sbp}")
except abnormal_vitals as e:
    print(e)