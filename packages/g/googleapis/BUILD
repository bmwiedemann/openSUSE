load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")
load("@io_bazel_rules_go//proto:def.bzl", "go_proto_library")
load("@com_github_grpc_grpc//bazel:cc_grpc_library.bzl", "cc_grpc_library")

filegroup(
    name = "api_httpbody_protos_src",
    srcs = [
        "google/api/httpbody.proto",
    ],
    visibility = ["//visibility:public"],
)

proto_library(
    name = "api_httpbody_protos_proto",
    srcs = [":api_httpbody_protos_src"],
    deps = ["@com_google_protobuf//:descriptor_proto"],
    visibility = ["//visibility:public"],
)

cc_proto_library(
    name = "api_httpbody_protos",
    deps = [":api_httpbody_protos_proto"],
    visibility = ["//visibility:public"],
)

py_proto_library(
    name = "api_httpbody_protos_py",
    srcs = [
        "google/api/httpbody.proto",
    ],
    include = ".",
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
    visibility = ["//visibility:public"],
    deps = ["@com_google_protobuf//:protobuf_python"],
)

go_proto_library(
    name = "api_httpbody_go_proto",
    importpath = "google.golang.org/genproto/googleapis/api/httpbody",
    proto = ":api_httpbody_protos_proto",
    visibility = ["//visibility:public"],
    deps = [
      ":descriptor_go_proto",
    ],
)

filegroup(
    name = "http_api_protos_src",
    srcs = [
        "google/api/annotations.proto",
        "google/api/http.proto",
    ],
    visibility = ["//visibility:public"],
)

go_proto_library(
    name = "descriptor_go_proto",
    importpath = "github.com/golang/protobuf/protoc-gen-go/descriptor",
    proto = "@com_google_protobuf//:descriptor_proto",
    visibility = ["//visibility:public"],
)

proto_library(
    name = "http_api_protos_proto",
    srcs = [":http_api_protos_src"],
    deps = ["@com_google_protobuf//:descriptor_proto"],
    visibility = ["//visibility:public"],
)

cc_proto_library(
    name = "http_api_protos",
    deps = [":http_api_protos_proto"],
    visibility = ["//visibility:public"],
)

py_proto_library(
    name = "http_api_protos_py",
    srcs = [
        "google/api/annotations.proto",
        "google/api/http.proto",
    ],
    include = ".",
    default_runtime = "@com_google_protobuf//:protobuf_python",
    protoc = "@com_google_protobuf//:protoc",
    visibility = ["//visibility:public"],
    deps = ["@com_google_protobuf//:protobuf_python"],
)

go_proto_library(
    name = "http_api_go_proto",
    importpath = "google.golang.org/genproto/googleapis/api/annotations",
    proto = ":http_api_protos_proto",
    visibility = ["//visibility:public"],
    deps = [
      ":descriptor_go_proto",
    ],
)

filegroup(
     name = "rpc_status_protos_src",
     srcs = [
         "google/rpc/status.proto",
     ],
     visibility = ["//visibility:public"],
)

proto_library(
     name = "rpc_status_protos_lib",
     srcs = [":rpc_status_protos_src"],
     deps = ["@com_google_protobuf//:any_proto"],
     visibility = ["//visibility:public"],
)

cc_proto_library(
    name = "rpc_status_protos",
    deps = [":rpc_status_protos_lib"],
    visibility = ["//visibility:public"],
)

go_proto_library(
    name = "rpc_status_go_proto",
    importpath = "google.golang.org/genproto/googleapis/rpc/status",
    proto = ":rpc_status_protos_lib",
    visibility = ["//visibility:public"],
    deps = [
      "@io_bazel_rules_go//proto/wkt:any_go_proto",
    ],
)

py_proto_library(
     name = "rpc_status_protos_py",
     srcs = [
         "google/rpc/status.proto",
     ],
     include = ".",
     default_runtime = "@com_google_protobuf//:protobuf_python",
     protoc = "@com_google_protobuf//:protoc",
     visibility = ["//visibility:public"],
     deps = ["@com_google_protobuf//:protobuf_python"],
)

proto_library(
    name = "tracing_proto_proto",
    srcs = [
        "google/devtools/cloudtrace/v2/trace.proto",
        "google/devtools/cloudtrace/v2/tracing.proto",
    ],
    deps = [
        ":http_api_protos_proto",
        ":rpc_status_protos_lib",
        "@com_google_protobuf//:timestamp_proto",
        "@com_google_protobuf//:wrappers_proto",
        "@com_google_protobuf//:empty_proto",
    ],
)

cc_proto_library(
    name = "tracing_proto_cc",
    deps = [":tracing_proto_proto"],
)

cc_grpc_library(
    name = "tracing_proto",
    srcs = [":tracing_proto_proto"],
    deps = [":tracing_proto_cc"],
    grpc_only = True,
    visibility = ["@io_opencensus_cpp//opencensus:__subpackages__"],
)
