import cy_example
import py_example
import time

if __name__ == "__main__":
    # start = time.time()
    # cy_example.main(cy_example.foo)
    # end = time.time()
    # print("cyexample | elapsed seconds:", end-start)

    start = time.time()
    py_example.main()
    end = time.time()
    print("pyexample | elapsed seconds:", end-start)
