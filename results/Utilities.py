class Utilities:
    SECONDS_IN_24_HOURS = 24 * 60 * 60
    STATISTICS = ["total_crashes", "total_paths", "unique_crashes"]

    @staticmethod
    def is_data_in_the_log_file(file_data: str) -> bool:
        return len(file_data) > 4

    @staticmethod
    def obtain_the_time(line: str) -> float:
        return float(line.split(" ")[0]) / 60 / 60

    @staticmethod
    def obtain_the_statistic(line: str) -> int:
        return int(line.split(" ")[1])