from torch.utils.tensorboard import SummaryWriter
import sys

writer = SummaryWriter("/home/users/u7439300/workspace/52results/tensor_logs")

def get_hit_rates(file_path):
    hit_rates = []
    with open(file_path, "r") as f:
        for line in f:
            if "Hit-rate:" in line:
                hit_rates.append(float(line.split(" ")[4]) / 100)
    return hit_rates

def main():
    all_hit_rates = []
    for i in [1, 2, 4, 8, 16, 32]:
        file_path = "/home/users/u7439300/workspace/52results/result_{}.txt".format(i)
        hit_rates = get_hit_rates(file_path)
        all_hit_rates.append(hit_rates)
        for j, hit_rate in enumerate(hit_rates):
            writer.add_scalar("result_{}GB".format(i), hit_rate, j)
    # Draw all hit rates in one graph
    for i, hit_rates in enumerate(all_hit_rates):
        # writer.add_scalar("Hit rates", tag_scalar_dict={"1GB": hit_rates[0], "2GB": hit_rates[1], "4GB": hit_rates[2], "8GB": hit_rates[3], "16GB": hit_rates[4], "32GB": hit_rates[5]}, global_step=i)
        for j, hit_rate in enumerate(all_hit_rates[i]):
            writer.add_scalars("Hit rates", tag_scalar_dict={str(2**i) + "GB": hit_rate}, global_step=j)
    writer.close()

if __name__ == '__main__':
    main()