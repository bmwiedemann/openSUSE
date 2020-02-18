package(default_visibility = ["//visibility:public"])

load(
    "@envoy//bazel:envoy_build_system.bzl",
    "envoy_cc_binary",
)

envoy_cc_binary(
    name = "envoy",
    repository = "@envoy",
    deps = [
        # Cilium filters.
        "@cilium_proxy//cilium:bpf_metadata_lib",
        "@cilium_proxy//cilium:network_filter_lib",
        "@cilium_proxy//cilium:l7policy_lib",
        "@cilium_proxy//cilium:tls_wrapper_lib",

        "@envoy//source/exe:envoy_main_entry_lib",
    ],
)
