load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load(":genrule_repository.bzl", "genrule_repository")
load(":repository_locations.bzl", "REPOSITORY_LOCATIONS")
load(":target_recipes.bzl", "TARGET_RECIPES")
load(
    "@bazel_tools//tools/cpp:windows_cc_configure.bzl",
    "find_vc_path",
    "setup_vc_env_vars",
)
load("@bazel_tools//tools/cpp:lib_cc_configure.bzl", "get_env_var")

# dict of {build recipe name: longform extension name,}
PPC_SKIP_TARGETS = {"luajit": "envoy.filters.http.lua"}

def _repository_impl(name, **kwargs):
    # `existing_rule_keys` contains the names of repositories that have already
    # been defined in the Bazel workspace. By skipping repos with existing keys,
    # users can override dependency versions by using standard Bazel repository
    # rules in their WORKSPACE files.
    existing_rule_keys = native.existing_rules().keys()
    if name in existing_rule_keys:
        # This repository has already been defined, probably because the user
        # wants to override the version. Do nothing.
        return

    loc_key = kwargs.pop("repository_key", name)
    location = REPOSITORY_LOCATIONS[loc_key]

    # Git tags are mutable. We want to depend on commit IDs instead. Give the
    # user a useful error if they accidentally specify a tag.
    if "tag" in location:
        fail(
            "Refusing to depend on Git tag %r for external dependency %r: use 'commit' instead." %
            (location["tag"], name),
        )

    # HTTP tarball at a given URL. Add a BUILD file if requested.
    http_archive(
        name = name,
        urls = location["urls"],
        sha256 = location["sha256"],
        strip_prefix = location.get("strip_prefix", ""),
        **kwargs
    )

def _build_recipe_repository_impl(ctxt):
    # modify the recipes list based on the build context
    recipes = _apply_dep_blacklist(ctxt, ctxt.attr.recipes)

    # Setup the build directory with links to the relevant files.
    ctxt.symlink(Label("//bazel:repositories.sh"), "repositories.sh")
    ctxt.symlink(Label("//bazel:repositories.bat"), "repositories.bat")
    ctxt.symlink(
        Label("//ci/build_container:build_and_install_deps.sh"),
        "build_and_install_deps.sh",
    )
    ctxt.symlink(Label("//ci/build_container:recipe_wrapper.sh"), "recipe_wrapper.sh")
    ctxt.symlink(Label("//ci/build_container:Makefile"), "Makefile")
    for r in recipes:
        ctxt.symlink(
            Label("//ci/build_container/build_recipes:" + r + ".sh"),
            "build_recipes/" + r + ".sh",
        )
    ctxt.symlink(Label("//ci/prebuilt:BUILD"), "BUILD")

    # Run the build script.
    command = []
    env = {}
    if ctxt.os.name.upper().startswith("WINDOWS"):
        vc_path = find_vc_path(ctxt)
        current_path = get_env_var(ctxt, "PATH", None, False)
        env = setup_vc_env_vars(ctxt, vc_path)
        env["PATH"] += (";%s" % current_path)
        env["CC"] = "cl"
        env["CXX"] = "cl"
        env["CXXFLAGS"] = "-DNDEBUG"
        env["CFLAGS"] = "-DNDEBUG"
        command = ["./repositories.bat"] + recipes
    else:
        command = ["./repositories.sh"] + recipes

    print("Fetching external dependencies...")
    result = ctxt.execute(
        command,
        environment = env,
        quiet = False,
    )
    print(result.stdout)
    print(result.stderr)
    print("External dep build exited with return code: %d" % result.return_code)
    if result.return_code != 0:
        print("\033[31;1m\033[48;5;226m External dependency build failed, check above log " +
              "for errors and ensure all prerequisites at " +
              "https://github.com/envoyproxy/envoy/blob/master/bazel/README.md#quick-start-bazel-build-for-developers are met.")

        # This error message doesn't appear to the user :( https://github.com/bazelbuild/bazel/issues/3683
        fail("External dep build failed")

def _default_envoy_build_config_impl(ctx):
    ctx.file("WORKSPACE", "")
    ctx.file("BUILD.bazel", "")
    ctx.symlink(ctx.attr.config, "extensions_build_config.bzl")

_default_envoy_build_config = repository_rule(
    implementation = _default_envoy_build_config_impl,
    attrs = {
        "config": attr.label(default = "@envoy//source/extensions:extensions_build_config.bzl"),
    },
)

def _default_envoy_api_impl(ctx):
    ctx.file("WORKSPACE", "")
    ctx.file("BUILD.bazel", "")
    api_dirs = [
        "bazel",
        "docs",
        "envoy",
        "examples",
        "test",
        "tools",
    ]
    for d in api_dirs:
        ctx.symlink(ctx.path(ctx.attr.api).dirname.get_child(d), d)

_default_envoy_api = repository_rule(
    implementation = _default_envoy_api_impl,
    attrs = {
        "api": attr.label(default = "@envoy//api:BUILD"),
    },
)

# Bazel native C++ dependencies. For the dependencies that doesn't provide autoconf/automake builds.
def _cc_deps():
    native.local_repository(
        name = "grpc_httpjson_transcoding",
        path = "/usr/src/grpc-httpjson-transcoding",
    )
    native.bind(
        name = "path_matcher",
        actual = "@grpc_httpjson_transcoding//src:path_matcher",
    )
    native.bind(
        name = "grpc_transcoding",
        actual = "@grpc_httpjson_transcoding//src:transcoding",
    )

def _go_deps(skip_targets):
    # Keep the skip_targets check around until Istio Proxy has stopped using
    # it to exclude the Go rules.
    if "io_bazel_rules_go" not in skip_targets:
        native.local_repository(
            name = "com_github_golang_protobuf",
            path = "/usr/src/protoc-gen-go",
        )
        native.local_repository(
            name = "org_golang_x_tools",
            path = "../golang-org-x-tools",
        )
        native.local_repository(
            name = "io_bazel_rules_go",
            path = "/usr/src/bazel-rules-go",
        )
        native.local_repository(
            name = "bazel_gazelle",
            path = "/usr/src/bazel-gazelle",
        )

def _envoy_api_deps():
    # Treat the data plane API as an external repo, this simplifies exporting the API to
    # https://github.com/envoyproxy/data-plane-api.
    if "envoy_api" not in native.existing_rules().keys():
        _default_envoy_api(name = "envoy_api")

    native.bind(
        name = "api_httpbody_protos",
        actual = "@googleapis//:api_httpbody_protos",
    )
    native.bind(
        name = "http_api_protos",
        actual = "@googleapis//:http_api_protos",
    )

def envoy_dependencies(path = "@envoy_deps//", skip_targets = []):
    envoy_repository = repository_rule(
        implementation = _build_recipe_repository_impl,
        environ = [
            "CC",
            "CXX",
            "CFLAGS",
            "CXXFLAGS",
            "LD_LIBRARY_PATH",
        ],
        # Don't pretend we're in the sandbox, we do some evil stuff with envoy_dep_cache.
        local = True,
        attrs = {
            "recipes": attr.string_list(),
        },
    )

    # Ideally, we wouldn't have a single repository target for all dependencies, but instead one per
    # dependency, as suggested in #747. However, it's much faster to build all deps under a single
    # recursive make job and single make jobserver.
    recipes = depset()
    for t in TARGET_RECIPES:
        if t not in skip_targets:
            recipes += depset([TARGET_RECIPES[t]])

    envoy_repository(
        name = "envoy_deps",
        recipes = recipes.to_list(),
    )

    for t in TARGET_RECIPES:
        if t not in skip_targets:
            native.bind(
                name = t,
                actual = path + ":" + t,
            )

    # Treat Envoy's overall build config as an external repo, so projects that
    # build Envoy as a subcomponent can easily override the config.
    if "envoy_build_config" not in native.existing_rules().keys():
        _default_envoy_build_config(name = "envoy_build_config")

    # The long repo names (`com_github_fmtlib_fmt` instead of `fmtlib`) are
    # semi-standard in the Bazel community, intended to avoid both duplicate
    # dependencies and name conflicts.
    _io_opentracing_cpp()
    _com_lightstep_tracer_cpp()
    _com_github_grpc_grpc()
    _com_github_nanopb_nanopb()
    _com_google_protobuf()

    _cc_deps()
    _go_deps(skip_targets)
    _envoy_api_deps()

def _io_opentracing_cpp():
    native.local_repository(
        name = "io_opentracing_cpp",
        path = "/usr/src/opentracing-cpp",
    )
    native.bind(
        name = "opentracing",
        actual = "@io_opentracing_cpp//:opentracing",
    )

def _com_lightstep_tracer_cpp():
    native.local_repository(
        name = "com_lightstep_tracer_cpp",
        path = "/usr/src/lightstep-tracer-cpp",
    )
    native.local_repository(
        name = "lightstep_vendored_googleapis",
        path = "/usr/src/lightstep-tracer-cpp/lightstep-tracer-common/third_party/googleapis",
    )
    native.bind(
        name = "lightstep",
        actual = "@com_lightstep_tracer_cpp//:lightstep_tracer",
    )

def _com_google_protobuf():
    native.local_repository(
        name = "com_google_protobuf",
        path = "/usr/src/protobuf",
    )
    native.local_repository(
        name = "com_google_protobuf_cc",
        path = "/usr/src/protobuf",
    )
    native.bind(
        name = "protobuf",
        actual = "@com_google_protobuf//:protobuf",
    )
    native.bind(
        name = "protobuf_clib",
        actual = "@com_google_protobuf//:protoc_lib",
    )
    native.bind(
        name = "protocol_compiler",
        actual = "@com_google_protobuf//:protoc",
    )
    native.bind(
        name = "protoc",
        actual = "@com_google_protobuf_cc//:protoc",
    )

    # Needed for `bazel fetch` to work with @com_google_protobuf
    # https://github.com/google/protobuf/blob/v3.6.1/util/python/BUILD#L6-L9
    native.bind(
        name = "python_headers",
        actual = "@com_google_protobuf//util/python:python_headers",
    )

def _com_github_grpc_grpc():
    native.local_repository(
        name = "com_github_grpc_grpc",
        path = "/usr/src/grpc",
    )

    # Rebind some stuff to match what the gRPC Bazel is expecting.
    native.bind(
        name = "protobuf_headers",
        actual = "@com_google_protobuf//:protobuf_headers",
    )
    native.bind(
        name = "libssl",
        actual = "//external:openssl",
    )
    native.bind(
        name = "cares",
        actual = "//external:ares",
    )

    native.bind(
        name = "grpc",
        actual = "@com_github_grpc_grpc//:grpc++",
    )

    native.bind(
        name = "grpc_health_proto",
        actual = "@envoy//bazel:grpc_health_proto",
    )

    native.bind(
        name = "grpc_alts_fake_handshaker_server",
        actual = "@com_github_grpc_grpc//test/core/tsi/alts/fake_handshaker:fake_handshaker_lib",
    )

def _com_github_nanopb_nanopb():
    native.local_repository(
        name = "com_github_nanopb_nanopb",
        path = "/usr/src/nanopb",
    )

    native.bind(
        name = "nanopb",
        actual = "@com_github_nanopb_nanopb//:nanopb",
    )

def _apply_dep_blacklist(ctxt, recipes):
    newlist = []
    skip_list = dict()
    if _is_linux_ppc(ctxt):
        skip_list = PPC_SKIP_TARGETS
    for t in recipes:
        if t not in skip_list.keys():
            newlist.append(t)
    return newlist

def _is_linux_ppc(ctxt):
    if ctxt.os.name != "linux":
        return False
    res = ctxt.execute(["uname", "-m"])
    return "ppc" in res.stdout
