# Copyright 2017 Istio Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
#
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

def mixerapi_repositories(bind=True):
    BUILD = """
# Copyright 2018 Istio Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
#
load("@com_google_protobuf//:protobuf.bzl", "cc_proto_library")

cc_proto_library(
    name = "mixer_api_cc_proto",
    srcs = glob(
        ["mixer/v1/*.proto"],
    ),
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
    visibility = ["//visibility:public"],
    deps = [
        "//external:cc_gogoproto",
        "//external:cc_wkt_protos",
        "//external:rpc_status_proto",
    ],
)

cc_proto_library(
    name = "mixer_client_config_cc_proto",
    srcs = glob(
        ["mixer/v1/config/client/*.proto"],
    ),
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
    visibility = ["//visibility:public"],
    deps = [
        ":mixer_api_cc_proto",
    ],
)

cc_proto_library(
    name = "authentication_policy_config_cc_proto",
    srcs = glob(
        ["envoy/config/filter/http/authn/v2alpha1/*.proto",
         "authentication/v1alpha1/*.proto",
         "common/v1alpha1/*.proto",
        ],
    ),
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
    visibility = ["//visibility:public"],
    deps = [
        "//external:cc_gogoproto",
    ],
)

cc_proto_library(
    name = "jwt_auth_config_cc_proto",
    srcs = glob(
        ["envoy/config/filter/http/jwt_auth/v2alpha1/*.proto", ],
    ),
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
    visibility = ["//visibility:public"],
    deps = [
        "//external:cc_gogoproto",
    ],
)

cc_proto_library(
    name = "tcp_cluster_rewrite_config_cc_proto",
    srcs = glob(
        ["envoy/config/filter/network/tcp_cluster_rewrite/v2alpha1/*.proto", ],
    ),
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
    visibility = ["//visibility:public"],
    deps = [
        "//external:cc_gogoproto",
    ],
)

filegroup(
    name = "global_dictionary_file",
    srcs = ["mixer/v1/global_dictionary.yaml"],
    visibility = ["//visibility:public"],
)

"""
    native.new_local_repository(
        name = "mixerapi_git",
        path = "../istio-api-1.1.0snapshot.2+git20181102",
        build_file_content = BUILD,
    )
    if bind:
        native.bind(
            name = "mixer_api_cc_proto",
            actual = "@mixerapi_git//:mixer_api_cc_proto",
        )
        native.bind(
            name = "mixer_client_config_cc_proto",
            actual = "@mixerapi_git//:mixer_client_config_cc_proto",
        )
        native.bind(
            name = "authentication_policy_config_cc_proto",
            actual = "@mixerapi_git//:authentication_policy_config_cc_proto",
        )
        native.bind(
            name = "jwt_auth_config_cc_proto",
            actual = "@mixerapi_git//:jwt_auth_config_cc_proto",
        )
        native.bind(
            name = "tcp_cluster_rewrite_config_cc_proto",
            actual = "@mixerapi_git//:tcp_cluster_rewrite_config_cc_proto",
        )

def protobuf_repositories(load_repo=True, bind=True):
    if load_repo:
        native.local_repository(
            name = "com_google_protobuf",
            path = "/usr/src/protobuf",
        )

    if bind:
        native.bind(
            name = "protoc",
            actual = "@com_google_protobuf//:protoc",
        )

        native.bind(
            name = "protocol_compiler",
            actual = "@com_google_protobuf//:protoc",
        )

        native.bind(
            name = "protobuf",
            actual = "@com_google_protobuf//:protobuf",
        )

        native.bind(
            name = "cc_wkt_protos",
            actual = "@com_google_protobuf//:cc_wkt_protos",
        )

        native.bind(
            name = "cc_wkt_protos_genproto",
            actual = "@com_google_protobuf//:cc_wkt_protos_genproto",
        )

        native.bind(
            name = "protobuf_compiler",
            actual = "@com_google_protobuf//:protoc_lib",
        )

        native.bind(
            name = "protobuf_clib",
            actual = "@com_google_protobuf//:protoc_lib",
        )

def cc_gogoproto_repositories(bind=True):
    BUILD = """
# Copyright 2017 Istio Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
#
licenses(["notice"])
load("@com_google_protobuf//:protobuf.bzl", "cc_proto_library")
exports_files(glob(["google/**"]))
cc_proto_library(
    name = "cc_gogoproto",
    srcs = [
        "gogoproto/gogo.proto",
    ],
    include = ".",
    default_runtime = "//external:protobuf",
    protoc = "//external:protoc",
    visibility = ["//visibility:public"],
    deps = [
        "//external:cc_wkt_protos",
    ],
)
"""
    native.new_local_repository(
        name = "gogoproto_git",
        build_file_content = BUILD,
        path = "/usr/src/protoc-gen-gogo",
    )

    if bind:
        native.bind(
            name = "cc_gogoproto",
            actual = "@gogoproto_git//:cc_gogoproto",
        )

        native.bind(
            name = "cc_gogoproto_genproto",
            actual = "@gogoproto_git//:cc_gogoproto_genproto",
        )

def googleapis_repositories(bind=True):
    GOOGLEAPIS_BUILD_FILE = """
package(default_visibility = ["//visibility:public"])

load("@com_google_protobuf//:protobuf.bzl", "cc_proto_library")

cc_proto_library(
    name = "rpc_status_proto",
    srcs = [
        "google/rpc/status.proto",
    ],
    visibility = ["//visibility:public"],
    protoc = "//external:protoc",
    default_runtime = "//external:protobuf",
    deps = [
        "//external:cc_wkt_protos",
    ],
)
"""
    native.new_local_repository(
        name = "com_github_googleapis_googleapis",
        build_file_content = GOOGLEAPIS_BUILD_FILE,
        path = "/usr/src/googleapis",
    )

    if bind:
        native.bind(
            name = "rpc_status_proto",
            actual = "@com_github_googleapis_googleapis//:rpc_status_proto",
        )
        native.bind(
            name = "rpc_status_proto_genproto",
            actual = "@com_github_googleapis_googleapis//:rpc_status_proto_genproto",
        )

def mixerapi_dependencies():
     protobuf_repositories(load_repo=False, bind=True)
     cc_gogoproto_repositories()
     googleapis_repositories()
     mixerapi_repositories()
