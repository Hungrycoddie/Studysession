import speedtest

st = speedtest.Speedtest()

option = int(input('''
Press 1 to check your internet speed:
Press 2 to check your internet speed and share the results online:
'''))

if option == 1:
    print(st.download())
    print(st.upload())
elif option == 2:
    st.get_servers([])
    st.get_best_server()
    st.download()
    st.upload()
    res = st.results.dict()
    print(res)
else:
    print('Please enter a valid option')