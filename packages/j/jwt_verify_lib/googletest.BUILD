licenses(["notice"])  # Apache 2

cc_library(
    name = "googletest",
    hdrs = glob([
        "thirdparty_build/include/gmock/**/*.h",
        "thirdparty_build/include/gtest/**/*.h",
    ]),
    copts = ["-I/usr/include/gtest"],
    linkopts = [
        "-lgmock",
        "-lgmock_main",
        "-lgtest",
        "-lgtest_main",
    ],
    visibility = ["//visibility:public"],
    linkstatic=False,
)
