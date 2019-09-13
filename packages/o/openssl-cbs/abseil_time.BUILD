licenses(["notice"])  # Apache 2

cc_library(
    name = "abseil_time",
    hdrs = glob(["thirdparty_build/include/absl/**/*.h"]),
    copts = ["-I/usr/include/absl"],
    linkopts = [
        "-labsl_base_libbase",
        "-labsl_base_libspinlock_wait",
        "-labsl_numeric_libint128",
        "-labsl_time_internal_cctz_libcivil_time",
        "-labsl_time_internal_cctz_libtime_zone",
        "-labsl_time_libtest_util",
        "-labsl_time_libtime",
    ],
    visibility = ["//visibility:public"],
    linkstatic=False,
)
