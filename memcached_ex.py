from pymemcache.client.base import Client

if __name__ == '__main__':
    client = Client(('172.26.12.92', 11211))

    client.flush_all()
    # client.set('some_key', 'some_value')
    # result = client.get('some_key')
    # print(client.get('euler$cache.euler_data_view.321965446094127104'))
    # client.delete('dlp$cache.dlp_arithmetic_env.10000')
    # kyes = ['dlp$cache.dlp_arithmetic_env.10000', 'dlp$cache.dlp_arithmetic_env.10001']
    # client.delete_many(kyes)
    # print(result)
    print("ok")
