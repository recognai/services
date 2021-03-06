from server.server import APP, get_model

# Pre-load English model
get_model('en')

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('0.0.0.0', 7000, APP)
    print('Listening on port: 7000')
    httpd.serve_forever()
