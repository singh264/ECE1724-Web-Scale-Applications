import matplotlib.pyplot as plt
from pathlib import Path
from typing import List

from Machine import Machine
from Utilities import Utilities


class Visualizer:
    def __init__(self) -> None:
        self.__data = dict()
        self.__data_directory_path = None

    def initialize_data_directory_path(self) -> Path:
        data_directory_path = Path(input("Provide the data directory path: "))

        self.__data_directory_path = data_directory_path

    def obtain_the_machine_paths(self) -> List[Path]:
        return self.__data_directory_path.rglob(f"afl-fuzz_{statistic_name}_*.txt")

    def initialize_the_data(self, machine: Machine) -> None:
        statistic_name = machine.statistic_name
        cluster_size = machine.cluster_size
        gnu_coreutils_program = machine.gnu_coreutils_program

        if gnu_coreutils_program not in self.__data.keys():
            self.__data[gnu_coreutils_program] = dict()

        if statistic_name not in self.__data[gnu_coreutils_program].keys():
            self.__data[gnu_coreutils_program][statistic_name] = dict()

        plot_data = self.__data[gnu_coreutils_program][statistic_name]
        
        if "time" not in plot_data.keys():
            plot_data["time"] = list(range(Utilities.SECONDS_IN_24_HOURS + 1))
        
        if f"cluster_size={cluster_size}" not in plot_data.keys():
            plot_data[f"cluster_size={cluster_size}"] = [0] * (Utilities.SECONDS_IN_24_HOURS + 1)

    def add_the_log_file_to_the_data(self, machine: Machine) -> None:
        statistic_name = machine.statistic_name
        path = machine.path
        cluster_size = machine.cluster_size
        gnu_coreutils_program = machine.gnu_coreutils_program
        
        file_data = path.read_text().split("\n")
        if Utilities.is_data_in_the_log_file(file_data):
            start_time = Utilities.obtain_the_time(file_data[3])
            plot_data = self.__data[gnu_coreutils_program][statistic_name]
            times_index_seen = set()
            for index in range(3, len(file_data) - 1):
                time = Utilities.obtain_the_time(file_data[index]) - start_time
                statistic = Utilities.obtain_the_statistic(file_data[index])
                time_index = int(time)
                if time <= Utilities.SECONDS_IN_24_HOURS and time_index not in times_index_seen:
                    times_index_seen.add(time_index)
                    plot_data[f"cluster_size={cluster_size}"][time_index] += statistic

    def adjust_the_data(self, statistic_name: str) -> None:
        for gnu_coreutils_program in self.__data.keys():
            plot_data = self.__data[gnu_coreutils_program][statistic_name]
            times = plot_data["time"]
            latest_data_point_time = 0
            for key in plot_data.keys():
                if "cluster_size" in key:
                    cluster_size = key
                    statistics = plot_data[cluster_size]
                    for time in range(len(times)):
                        if statistics[time] > 0:
                            latest_data_point_time = time
                        if (statistics[time] == 0) and (statistics[time - 1] > 0):
                            statistics[time] = statistics[time - 1]
                        elif (statistics[time] > 0) and (statistics[time - 1] > 0):
                            statistics[time] += statistics[time - 1]
            
            plot_data["time"] = times[0:latest_data_point_time] 

            for key in plot_data.keys():
                if "cluster_size" in key:
                    cluster_size = key
                    statistics = plot_data[cluster_size]
                    plot_data[cluster_size] = statistics[0:latest_data_point_time]

    def display_the_data(self, statistic_name: str) -> None:
        for gnu_coreutils_program in self.__data.keys():
            plot_data = self.__data[gnu_coreutils_program][statistic_name]
            times = plot_data["time"]
            for key in sorted(plot_data.keys()):
                if "cluster_size" in key:
                    cluster_size = key
                    statistics = plot_data[cluster_size]
                    label = cluster_size 
                    plt.plot(times, statistics, label=label)
            plt.xlabel("time in hours")
            plt.ylabel(statistic_name)
            plt.title(gnu_coreutils_program)
            plt.legend()
            plt.show()

if __name__ == '__main__':
    visualizer = Visualizer()
    visualizer.initialize_data_directory_path()
    for statistic_name in Utilities.STATISTICS:
        paths = sorted([path for path in visualizer.obtain_the_machine_paths()])
        for path in paths:
            machine = Machine(path)
            visualizer.initialize_the_data(machine)
            visualizer.add_the_log_file_to_the_data(machine)
        visualizer.adjust_the_data(statistic_name)
        visualizer.display_the_data(statistic_name)
