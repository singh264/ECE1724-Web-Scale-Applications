from pathlib import Path


class Machine:
    def __init__(self, path: Path) -> None:
        self.__path = path
        self.__cluster_size = self.__obtain_the_cluster_size()
        self.__machine_number = self.__obtain_the_machine_number()
        self.__statistic_name = self.__obtain_the_statistic_name()
        self.__gnu_coreutils_program = self.__obtain_the_gnu_coreutils_program()
     
    @property
    def path(self) -> Path:
        return self.__path
 
    @property
    def cluster_size(self) -> int:
        return self.__cluster_size
    
    @property
    def machine_number(self) -> int:
        return self.__machine_number
    
    @property
    def statistic_name(self) -> str:
        return self.__statistic_name

    @property
    def gnu_coreutils_program(self) -> str:
        return self.__gnu_coreutils_program

    def __obtain_the_cluster_size(self) -> int:
        cluster_size = -1
        path_attributes = str(self.__path).split("/")
        if "1_machine" in path_attributes:
            cluster_size = 1
        elif "3_machine" in path_attributes:
            cluster_size = 3
        elif "5_machine" in path_attributes:
            cluster_size = 5
        
        return cluster_size

    def __obtain_the_machine_number(self) -> int:
        machine_number = -1
        path_attributes = str(self.__path).split("/")
        if "machine_1" in path_attributes:
            machine_number = 1
        elif "machine_2" in path_attributes:
            machine_number = 2
        elif "machine_3" in path_attributes:
            machine_number = 3
        elif "machine_4" in path_attributes:
            machine_number = 4
        elif "machine_5" in path_attributes:
            machine_number = 5
        
        return machine_number

    def __obtain_the_gnu_coreutils_program(self) -> str:
        file_name = self.__path.stem

        return file_name.split("_")[3]
    
    def __obtain_the_statistic_name(self) -> str:
        file_name = self.__path.stem
        file_name_attributes = file_name.split("_")

        return f"{file_name_attributes[1]}_{file_name_attributes[2]}"
