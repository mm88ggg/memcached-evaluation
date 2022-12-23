# Building Memcached

## Download and Install

```
wget http://memcached.org/latest
move latest m.tar.gz
mv latest m.tar.gz
tar -zxvf m.tar.gz
cd memcached-1.6.17/
./configure --prefix=/home/users/u7439300/memcached/memcached-1.6.17/build
make && make test && make install
```

## Run

### Parameters

-p port (11211 by default)

-m max memory (Megabytes)

-v detailed information

-vv very detailed information

### Example

```
./memcached -p 11211 -m 32768 -vv
```

# Running evaluation

I have uploaded the 'run.py.'

The script will do the evaluation process via rpc-replay.

The whole process is 

1. Start memcached
2. Start rpc-replay
3. Save the results and status
4. Close memcached
5. Repeat 1-4 with memcached sizes of 1G, 2G, 4G, 8G, 16G, 32G

After getting the result, we need to plot them.

I have uploaded the python code and results on the Github. Here's the link:

https://github.com/mm88ggg/memcached-evaluation

## How to plot the results by Tensorboard

First, install the PyTorch and Tensorboard.

```
pip3 install torch
pip3 install tensorboard
```

Then, run the tensorboard with path to the results folder.

```
tensorboard --logdir=path/to/result
```

Finally, you can open it with your browser.
