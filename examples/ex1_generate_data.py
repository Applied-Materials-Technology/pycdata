'''
================================================================================
pycdata: generate camera data example
================================================================================
'''
import time
import pycdata


def main() -> None:
    run_time: float = 1
    timer = pycdata.Timer(run_time)
    timer.start()

    print("="*80)
    print("Starting cycles.")
    print("="*80)

    count: int  = 0
    num_cycles = 10
    while count < num_cycles:
        if timer.finished():
            timer.start()
            count += 1
            print(f"Cycle {count} finished at {time.perf_counter()}s.")

    print("="*80)
    print("Cycles finished.")
    print("="*80)


if __name__ == '__main__':
    main()
