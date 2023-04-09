# ece1724

The purpose of the project is to study the performance of the American Fuzzy Lop fuzzer when the American Fuzzy Lop fuzzer completes the fuzzing of the input program with the inputs that are placed on multiple machines.

The technical challenge of the project could be to implement a system with a simple Application Programming Interface that enables users to complete the fuzzing of the input program with multi-system parallelization of the American Fuzzy Lop fuzzer.

The study of the performance of the American Fuzzy Lop fuzzer would be to evaluate the attributes of the American Fuzzy Lop coverage that includes the total paths, the total crashes, and the unique crashes.

The design of the system includes multiple Google Cloud Platform machines that are the worker machines with one Google Cloud Platform machine that is the primary machine that orchestrates the operations of the American Fuzzy Lop fuzzer on the worker Google Cloud Platform machines. The primary Google Cloud Platform machine would provide the results of the American Fuzzy Lop fuzzer to another machine that would read the results of the American Fuzzy Lop fuzzer that was obtained from the worker machine and indicate the combined results of the American Fuzzy Lop fuzzer.

The code of the project is located at https://github.com/singh264/ece1724/tree/project_final_report. The GitHub repository includes the primary script, the worker script, the data of the experiments of the project, the code to obtain the results of the project, and the results of the project.

The adjustment to the American Fuzzy Lop fuzzer is located at https://github.com/singh264/AFL/tree/ece1724_project_final_report. The GitHub repository includes the American Fuzzy Lop fuzzer with the adjustment of logging the attributes of the American Fuzzy Lop coverage that includes the total paths, the total crashes, and the unique crashes during the runtime of the American Fuzzy Lop fuzzer and when the attributes of the American Fuzzy Lop fuzzer coverage is modified during the runtime of the American Fuzzy Lop fuzzer.

