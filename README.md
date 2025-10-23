# Arithmetic Library – Build & Run

## Build the project

```bash
mkdir build && cd build
cmake ..
make pkg

cd ..
python3 -c "import arithmetic; print(arithmetic.sum(10, 11))"
```
