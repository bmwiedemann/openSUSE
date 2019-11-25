#
# spec file for package abseil-cpp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover 0
%define libname libabseil%{sover}

%define src_install_dir /usr/src/%{name}

Name:           abseil-cpp
Version:        20190605
Release:        0
Summary:        C++11 libraries which augment the C++ stdlib
License:        Apache-2.0
Url:            https://abseil.io/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  bazel-rules-cc-source
BuildRequires:  bazel-workspaces
BuildRequires:  bazel0.29
BuildRequires:  benchmark-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  patchelf

%description
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package -n %{libname}
Summary:        C++11 libraries which augment the C++ stdlib

%description -n %{libname}
Shared libraries for Abseil, a collection of C++11 libraries
which augment the C++ standard library. It also provides
features incorporated into C++14 and C++17 standards.

%package devel
Summary:        Development files for Abseil
Requires:       %{libname} = %{version}

%description devel
Development files for Abseil, a collection of C++11 libraries
which augment the C++ standard library. It also provides
features incorporated into C++14 and C++17 standards.

%package source
Summary:        Source code of Abseil

%description source
Source code of Abseil, a collection of C++11 libraries
which augment the C++ standard library. It also provides
features incorporated into C++14 and C++17 standards.

%prep
%setup -q

%build
TARGETS=$(bazel query '//... except kind(.*test, //...)')
bazel build \
    -c dbg \
    --color=no \
    %(for opt in %{optflags}; do echo -e "--copt=${opt} \c"; done) \
    --curses=no \
    --genrule_strategy=standalone \
    --host_javabase=@local_jdk//:jdk \
    --override_repository="com_github_google_benchmark=%{_datadir}/bazel-workspaces/benchmark" \
    --override_repository="com_google_googletest=%{_datadir}/bazel-workspaces/gtest" \
    --override_repository="rules_cc=/usr/src/bazel-rules-cc" \
    --spawn_strategy=standalone \
    --strip=never \
    --verbose_failures \
    ${TARGETS}
bazel shutdown

%install
for lib in $(find bazel-bin/absl -name "*.so"|sort); do
    lib_basename=$(basename ${lib} | sed -e "s|^lib|libabsl_|")
    install -D -m0755 ${lib} %{buildroot}%{_libdir}/${lib_basename}.%{sover}
    patchelf --set-soname ${lib_basename}.%{sover} %{buildroot}%{_libdir}/${lib_basename}.%{sover}
    ln -sf ${lib_basename}.%{sover} %{buildroot}%{_libdir}/${lib_basename}
done
for header in $(find . \( -name "*.h" -o -name "*.inc" \) -printf "%%P\n"); do
    install -D -m0644 $header %{buildroot}%{_includedir}/$header
done

mkdir -p %{buildroot}%{src_install_dir}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libabsl_bad_any_cast_impl.so.0
%{_libdir}/libabsl_bad_optional_access.so.0
%{_libdir}/libabsl_bad_variant_access.so.0
%{_libdir}/libabsl_base.so.0
%{_libdir}/libabsl_city.so.0
%{_libdir}/libabsl_civil_time.so.0
%{_libdir}/libabsl_config.so.0
%{_libdir}/libabsl_debugging_internal.so.0
%{_libdir}/libabsl_demangle_internal.so.0
%{_libdir}/libabsl_dynamic_annotations.so.0
%{_libdir}/libabsl_examine_stack.so.0
%{_libdir}/libabsl_exception_safety_testing.so.0
%{_libdir}/libabsl_failure_signal_handler.so.0
%{_libdir}/libabsl_flag.so.0
%{_libdir}/libabsl_graphcycles_internal.so.0
%{_libdir}/libabsl_handle.so.0
%{_libdir}/libabsl_hash.so.0
%{_libdir}/libabsl_hash_generator_testing.so.0
%{_libdir}/libabsl_hashtablez_sampler.so.0
%{_libdir}/libabsl_int128.so.0
%{_libdir}/libabsl_internal.so.0
%{_libdir}/libabsl_leak_check.so.0
%{_libdir}/libabsl_leak_check_api_disabled_for_testing.so.0
%{_libdir}/libabsl_leak_check_api_enabled_for_testing.so.0
%{_libdir}/libabsl_malloc_internal.so.0
%{_libdir}/libabsl_marshalling.so.0
%{_libdir}/libabsl_mutex_benchmark_common.so.0
%{_libdir}/libabsl_parse.so.0
%{_libdir}/libabsl_per_thread_sem_test_common.so.0
%{_libdir}/libabsl_pow10_helper.so.0
%{_libdir}/libabsl_raw_hash_set.so.0
%{_libdir}/libabsl_registry.so.0
%{_libdir}/libabsl_scoped_set_env.so.0
%{_libdir}/libabsl_spinlock_benchmark_common.so.0
%{_libdir}/libabsl_spinlock_test_common.so.0
%{_libdir}/libabsl_spinlock_wait.so.0
%{_libdir}/libabsl_stack_consumption.so.0
%{_libdir}/libabsl_stacktrace.so.0
%{_libdir}/libabsl_str_format_internal.so.0
%{_libdir}/libabsl_strings.so.0
%{_libdir}/libabsl_symbolize.so.0
%{_libdir}/libabsl_synchronization.so.0
%{_libdir}/libabsl_test_instance_tracker.so.0
%{_libdir}/libabsl_test_util.so.0
%{_libdir}/libabsl_throw_delegate.so.0
%{_libdir}/libabsl_time.so.0
%{_libdir}/libabsl_time_zone.so.0
%{_libdir}/libabsl_usage.so.0

%files devel
%{_includedir}/absl
%{_libdir}/libabsl_bad_any_cast_impl.so
%{_libdir}/libabsl_bad_optional_access.so
%{_libdir}/libabsl_bad_variant_access.so
%{_libdir}/libabsl_base.so
%{_libdir}/libabsl_city.so
%{_libdir}/libabsl_civil_time.so
%{_libdir}/libabsl_config.so
%{_libdir}/libabsl_debugging_internal.so
%{_libdir}/libabsl_demangle_internal.so
%{_libdir}/libabsl_dynamic_annotations.so
%{_libdir}/libabsl_examine_stack.so
%{_libdir}/libabsl_exception_safety_testing.so
%{_libdir}/libabsl_failure_signal_handler.so
%{_libdir}/libabsl_flag.so
%{_libdir}/libabsl_graphcycles_internal.so
%{_libdir}/libabsl_handle.so
%{_libdir}/libabsl_hash.so
%{_libdir}/libabsl_hash_generator_testing.so
%{_libdir}/libabsl_hashtablez_sampler.so
%{_libdir}/libabsl_int128.so
%{_libdir}/libabsl_internal.so
%{_libdir}/libabsl_leak_check.so
%{_libdir}/libabsl_leak_check_api_disabled_for_testing.so
%{_libdir}/libabsl_leak_check_api_enabled_for_testing.so
%{_libdir}/libabsl_malloc_internal.so
%{_libdir}/libabsl_marshalling.so
%{_libdir}/libabsl_mutex_benchmark_common.so
%{_libdir}/libabsl_parse.so
%{_libdir}/libabsl_per_thread_sem_test_common.so
%{_libdir}/libabsl_pow10_helper.so
%{_libdir}/libabsl_raw_hash_set.so
%{_libdir}/libabsl_registry.so
%{_libdir}/libabsl_scoped_set_env.so
%{_libdir}/libabsl_spinlock_benchmark_common.so
%{_libdir}/libabsl_spinlock_test_common.so
%{_libdir}/libabsl_spinlock_wait.so
%{_libdir}/libabsl_stack_consumption.so
%{_libdir}/libabsl_stacktrace.so
%{_libdir}/libabsl_str_format_internal.so
%{_libdir}/libabsl_strings.so
%{_libdir}/libabsl_symbolize.so
%{_libdir}/libabsl_synchronization.so
%{_libdir}/libabsl_test_instance_tracker.so
%{_libdir}/libabsl_test_util.so
%{_libdir}/libabsl_throw_delegate.so
%{_libdir}/libabsl_time.so
%{_libdir}/libabsl_time_zone.so
%{_libdir}/libabsl_usage.so

%files source
%{src_install_dir}

%changelog
