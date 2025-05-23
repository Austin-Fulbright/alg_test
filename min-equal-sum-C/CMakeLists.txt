cmake_minimum_required(VERSION 3.10)
project(min_equal_sum C)

set(CMAKE_C_STANDARD 11)

add_library(min_equal_sum STATIC
	src/min_equal_sum.c
)

add_executable(run_tests
	src/main.c
)


target_link_libraries(run_tests PRIVATE min_equal_sum)
target_include_directories(run_tests PRIVATE src)

