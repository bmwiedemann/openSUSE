licenses(["notice"])  # Apache 2

cc_library(
    name = "bssl_wrapper_lib",
    hdrs = glob(["thirdparty_build/include/opensslcbs/**/*.h"]),
    copts = ["-I/usr/include/opensslcbs"],
    linkopts = [
        "-lopenssl_cbs_lib",
    ],
    visibility = ["//visibility:public"],
    linkstatic=False,
)
