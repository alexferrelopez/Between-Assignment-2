#include <pybind11/pybind11.h>
#include "arithmetic.h"

namespace py = pybind11;

PYBIND11_MODULE(arithmetic, m) {
    m.doc() = "Arithmetic bindings for assignment 2";
    m.def("sum", &sum, "A function that adds two numbers");
}