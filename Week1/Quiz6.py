import aadpy.attitude as att
import numpy as np

if __name__ == "__main__":
    dcm = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    dcm_obj = att.DCM(dcm=dcm)

    quat_obj = att.AttitudeConverter.dcm_to_quat(dcm_obj)
    print(quat_obj.quaternion)


    dcm_1 = att.AttitudeConverter.quat_to_dcm(quat_obj)
    print(dcm_1)