import aadpy.attitude as att
import numpy as np


if __name__ == "__main__":
    """
    Corrrect answers:  
    case1 = [5.551115123125783e-17,5.551115123125783e-17,1.0]
    case2 = [0.33333333333333337,-0.33333333333333337,-0.33333333333333337]
    
    """


    mrp_n_r = att.MRP(mrp=np.array([-1.0/3, 1.0/3, -1.0/3]))
    mrp_n_r = mrp_n_r.inverse_rotation()
    quat_n_r = att.AttitudeConverter.mrp_to_quat(mrp_n_r)

    # Part 1
    mrp_b_n_1 = att.MRP(mrp=np.array([1.0/3, 1.0/3, 1.0/3]))
    mrp_b_r_1 = mrp_b_n_1 + mrp_n_r
    print("Part 1 MRP B/R=", mrp_b_r_1)

    quat_b_n_1 = att.AttitudeConverter.mrp_to_quat(mrp_b_n_1)
    quat_b_r_1 = quat_n_r * quat_b_n_1
    mrp_b_r_1_quat = att.AttitudeConverter.quat_to_mrp(quat_b_r_1)
    print("Part 1 MRP from Quat B/R=", mrp_b_r_1_quat)


    # Part 2
    mrp_b_n_2 = att.MRP(mrp=np.array([-1.0 / 3, -1.0 / 3, -1.0 / 3]))
    mrp_b_r_2 = mrp_b_n_2 + mrp_n_r
    print("Part 2 MRP B/R=", mrp_b_r_2)


    quat_b_n_2 = att.AttitudeConverter.mrp_to_quat(mrp_b_n_2)
    quat_b_r_2 =  quat_n_r * quat_b_n_2
    mrp_b_r_2_quat = att.AttitudeConverter.quat_to_mrp(quat_b_r_2)
    print("Part 2 MRP from Quat B/R=", mrp_b_r_2_quat)





