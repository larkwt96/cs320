import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = [
        [1000, 0.0705251693725586, 0.0044748783111572266, 144612, 8009],
        [2000, 0.5548849105834961, 0.0055730342864990234, 1111222, 16009],
        [3000, 1.8668849468231201, 0.008086919784545898, 3699832, 24009],
        [4000, 4.440575122833252, 0.01099705696105957, 8710442, 32009],
        [5000, 8.798875093460083, 0.013614654541015625, 16943052, 40009],
    ]
    for i in range(len(data)):
        print('n:{} dctime:{} dptime:{} dccalls:{} dpreads:{}'.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]))

    n_arr = [data[i][0] for i in range(len(data))]
    dctime_arr = [data[i][1] for i in range(len(data))]
    dptime_arr = [data[i][2] for i in range(len(data))]
    dccalls_arr = [data[i][3] for i in range(len(data))]
    dpreads_arr = [data[i][4] for i in range(len(data))]

    f, (timegr, callgr) = plt.subplots(1, 2)
    timegr.plot(n_arr, dctime_arr, 'b-')
    timegr.plot(n_arr, dptime_arr, 'r-')
    timegr.set_title('DC Time (blue) vs DP Time (red)')
    callgr.plot(n_arr, dccalls_arr, 'b-')
    callgr.plot(n_arr, dpreads_arr, 'r-')
    callgr.set_title('DC Calls (blue) vs DP Reads (red)')

    plt.show()
