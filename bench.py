import perf

def function_to_bench():
    a = 1 + 1

runner = perf.Runner()
runner.bench_func('Some function', function_to_bench)
