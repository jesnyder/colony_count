
from c0101_retrieve_measurements import retrieve_measurements
from c0102_parse_name_and_count import parse_name_and_count
from c0103_format_count_by_name import format_count_by_name

def count_colony():
    """

    """

    print("running count_colony")

    df_result, df_summary = retrieve_measurements()

    record_name_master, count_master = parse_name_and_count()

    format_count_by_name()

    print("completed count_colony")


if __name__ == "__main__":
    count_colony()
