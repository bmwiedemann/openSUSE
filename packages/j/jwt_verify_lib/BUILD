licenses(["notice"])  # Apache 2

package(default_visibility = ["//visibility:public"])

exports_files(["LICENSE"])

cc_library(
    name = "jwt_verify_lib",
    srcs = [
        "src/check_audience.cc",
        "src/jwks.cc",
        "src/jwt.cc",
        "src/status.cc",
        "src/struct_utils.h",
        "src/verify.cc",
    ],
    hdrs = [
        "jwt_verify_lib/check_audience.h",
        "jwt_verify_lib/jwks.h",
        "jwt_verify_lib/jwt.h",
        "jwt_verify_lib/status.h",
        "jwt_verify_lib/verify.h",
    ],
    deps = [
        "@abseil_strings//:abseil_strings",
        "@abseil_time//:abseil_time",
        "@openssl//:openssl-lib",
        "//external:protobuf",
    ],
)
