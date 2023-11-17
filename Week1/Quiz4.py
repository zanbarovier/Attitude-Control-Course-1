import aadpy.attitude as att
import numpy as np

if __name__ == "__main__":
    dcm = att.DCM(dcm=np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
    prv = att.AttitudeConverter.dcm_to_prv(dcm)
    print("Short positive rotation=", prv.short_positive_phi())
    print("e_hat=", prv.phi_deg_e_hat[1])
