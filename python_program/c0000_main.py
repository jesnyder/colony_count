

from c0100_count_colony import count_colony
from c0200_plot_colony_count import plot_colony_count

def main():
    """

    """

    print("running main")

    # retrieve measurements
    count_colony()

    # plot number of colonies found
    plot_colony_count()

    print("completed main")


if __name__ == "__main__":
    main()
