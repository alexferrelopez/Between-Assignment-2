# Arithmetic Library – Build & Run

## Build the project

```bash
mkdir build && cd build
cmake ..
make pkg
python3 -c "import arithmetic; print(arithmetic.sum(10,11))"

cd ..
pip install .
python3 -c "import arithmetic; print(arithmetic.sum(10,11))"
```
