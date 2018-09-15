@route('/', method='GET')
def main():
    return "hi\n"


# I've been bitten by using 'localhost' instead of 'listening on all interfaces' (whatever that means) by using 0.0.0.0...
# I was able to curl on an instance but not from other AWS instances
# Also, check inbound rules on an instance to make sure the port that's open is reachable via certain ips and security groups
run(host='0.0.0.0', port=8080, debug=True)
