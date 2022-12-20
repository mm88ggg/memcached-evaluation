import os
import subprocess
import argparse
import time
import socket

def run_cmd(cmd):
    print("Running command: {}".format(cmd))
    val = os.popen(cmd)
    res = ""
    for line in val.readlines():
        res += line
    print("Command output:\n{}".format(res))
    return res

def save_file(filename, content):
    print("Saving file: {}".format(filename))
    with open(filename, "w") as f:
        f.write(content)

def start_memcached(mem_size, port=11211):
    mem_size = mem_size * 1024
    print("Starting memcached")
    run_cmd("/home/users/u7439300/memcached/memcached-1.6.17/build/bin/memcached -m {} -p {} -d".format(mem_size, port))

def start_rpc_replay(mem_size, port=11211):
    print("Starting rpc_replay")
    run_cmd("/home/users/u7439300/rpc-perf/rpc-perf/target/release/rpc-replay --poolsize 100 --workers 8 --rate 1000000 --endpoint 0.0.0.0:11211 --trace /home/users/u7439300/rpc-perf/trace/cluster52.zst > /home/users/u7439300/workspace/test_script/result_{}.txt".format(mem_size))

def save_stats(mem_size, port=11211):
    def recvall(sock):
        BUFF_SIZE = 4096 # 4 KiB
        data = b''
        while True:
            part = sock.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                # either 0 or end of data
                break
        return data
    print("Saving stats")
    # run_cmd("telnet localhost {} > /home/users/u7439300/workspace/test_script/stats_{}.txt".format(port, mem_size))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", port))
    s.send(b"stats\r\n")
    data = recvall(s)
    s.close()
    save_file("/home/users/u7439300/workspace/test_script/stats_{}.txt".format(mem_size), data.decode("utf-8"))

def stop_memcached():
    print("Stopping memcached")
    run_cmd("pkill memcached")

def run(port=11211):
    print("Running test script")
    for mem_size in [1, 2, 4, 8, 16, 32]:
        start_memcached(mem_size, port)
        time.sleep(5)
        start_rpc_replay(mem_size, port)
        save_stats(mem_size, port)
        stop_memcached()
        time.sleep(5)

def main():
    port = 11211

    # Input parameters
    # -p: port
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port", type=int)
    args = parser.parse_args()
    if args.port:
        port = args.port

    run(port)

def test():
    stop_memcached()

if __name__ == '__main__':
    main()
    # test()