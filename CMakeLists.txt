cmake_minimum_required(VERSION 3.12)
project(arithmetic LANGUAGES CXX)

find_package(pybind11 REQUIRED)

add_library(arithmetic_cpp SHARED arithmetic.cpp)
set_target_properties(arithmetic_cpp PROPERTIES OUTPUT_NAME "arithmetic")

# installable library
install(TARGETS arithmetic_cpp DESTINATION lib)
install(FILES arithmetic.h DESTINATION include)

# wrapper target
pybind11_add_module(arithmetic bindings.cpp)
target_link_libraries(arithmetic PRIVATE arithmetic_cpp)

add_custom_target(buildlib DEPENDS arithmetic_cpp)
add_custom_target(installlib DEPENDS buildlib
    COMMAND ${CMAKE_COMMAND} --install .
)

add_custom_target(wrapper DEPENDS arithmetic)
add_custom_target(pkg DEPENDS wrapper)
