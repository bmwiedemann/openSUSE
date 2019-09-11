licenses(["notice"])  # Apache 2

cc_library(
    name = "bssl_wrapper_lib",
    hdrs = glob(["thirdparty_build/include/bssl_wrapper/**/*.h"]),
    copts = ["-I/usr/include/bssl_wrapper"],
    linkopts = [
        "-lbssl_wrapper_lib",
    ],
    visibility = ["//visibility:public"],
    linkstatic=False,
)
