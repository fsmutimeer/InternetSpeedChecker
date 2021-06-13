import speedtest as st

test = st.Speedtest()
print('Server Loading Please wait....')

test.get_servers()
print('Please Wait It takes a moment to get the ideal server...')

best_server = test.get_best_server()
print(best_server)

print('Executing Download Server Please wait...')

download_result = test.download()

print('Executing Upload Test Please wait...')

upload_result = test.upload()

ping_result = test.results.ping

print(download_result)
print(upload_result)
print(ping_result)

print(f'Download Speed {download_result / 1024 /1024: .3f} Mbps')
print(f'Upload Speed {upload_result / 1024 /1024: .3f} Mbps')
print(f'Ping Results {ping_result: .3f} ms')