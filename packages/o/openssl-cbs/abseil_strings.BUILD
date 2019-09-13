licenses(["notice"])  # Apache 2

cc_library(
    name = "abseil_strings",
    hdrs = glob(["thirdparty_build/include/absl/**/*.h"]),
    copts = ["-I/usr/include/absl"],
    linkopts = [
        "-labsl_base_libbase",
        "-labsl_base_libthrow_delegate",
        "-labsl_strings_libinternal",
        "-labsl_strings_libstr_format_internal",
        "-labsl_strings_libstrings",
    ],
    visibility = ["//visibility:public"],
    linkstatic=False,
)
