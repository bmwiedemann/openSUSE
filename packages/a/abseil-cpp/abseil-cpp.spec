#
# spec file for package abseil-cpp
#
# Copyright (c) 2024 SUSE LLC
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


%global soversion so.2401.0.0
%global lname_suffix 2401_0_0
%if 0%{?gcc_version} < 7
%global with_gcc 7
%endif
Name:           abseil-cpp
Version:        20240116.2
Release:        0
Summary:        C++11 libraries which augment the C++ stdlib
License:        Apache-2.0
URL:            https://abseil.io/
Source0:        https://github.com/abseil/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?with_gcc}
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  pkgconfig
# PATCH-FIX-OPENSUSE options-{old,cxx17}.patch Ensure ABI stability regardless of compiler options
%if 0%{?suse_version} && 0%{?suse_version} < 1550
Patch0:         options-old.patch
Patch1:         cmake.patch
%else
Patch0:         options-cxx17.patch
%endif
# upstream patch to prevent GTest error with CMake 3.30
Patch2:         abseil-cmake-gtest-testonly.patch

%description
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package -n libabsl_lite_%{lname_suffix}
Summary:        C++11 libraries which augment the C++ stdlib - lite
Obsoletes:      abseil-cpp < %{version}-%{release}
Provides:       abseil-cpp = %{version}-%{release}

%description -n libabsl_lite_%{lname_suffix}
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

This package provides the subset needed by protobuf-lite.

%package -n libabsl_%{lname_suffix}
Summary:        C++11 libraries which augment the C++ stdlib - others
Obsoletes:      abseil-cpp < %{version}-%{release}
Obsoletes:      libabsl2401_0_0 < %{version}-%{release}
Provides:       abseil-cpp = %{version}-%{release}

%description -n libabsl_%{lname_suffix}
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package devel
Summary:        Header files for Abseil
Requires:       libabsl_%{lname_suffix}
Requires:       libabsl_lite_%{lname_suffix}

%description devel
Abseil is a collection of C++11 libraries which augment the C++
standard library.
This package contains headers and build system files for it.

%prep
%autosetup -p1

%build
%if 0%{?with_gcc}
export CC="gcc-%{with_gcc}"
export CXX="g++-%{with_gcc}"
%endif
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%check
%ctest

# SLE12 doed not define this macro
%if %{undefined ldconfig_scriptlets}
%post -n libabsl_lite_%{lname_suffix} -p /sbin/ldconfig
%postun  -n libabsl_lite_%{lname_suffix} -p /sbin/ldconfig

%post -n libabsl_%{lname_suffix} -p /sbin/ldconfig
%postun  -n libabsl_%{lname_suffix} -p /sbin/ldconfig

%else
%ldconfig_scriptlets -n libabsl_lite_%{lname_suffix}
%ldconfig_scriptlets -n libabsl_%{lname_suffix}
%endif

%files -n libabsl_lite_%{lname_suffix}
%license LICENSE
%{_libdir}/libabsl_base.%{soversion}
%{_libdir}/libabsl_city.%{soversion}
%{_libdir}/libabsl_cord.%{soversion}
%{_libdir}/libabsl_cord_internal.%{soversion}
%{_libdir}/libabsl_cordz_functions.%{soversion}
%{_libdir}/libabsl_cordz_handle.%{soversion}
%{_libdir}/libabsl_cordz_info.%{soversion}
%{_libdir}/libabsl_crc32c.%{soversion}
%{_libdir}/libabsl_crc_cord_state.%{soversion}
%{_libdir}/libabsl_crc_internal.%{soversion}
%{_libdir}/libabsl_debugging_internal.%{soversion}
%{_libdir}/libabsl_demangle_internal.%{soversion}
%{_libdir}/libabsl_examine_stack.%{soversion}
%{_libdir}/libabsl_exponential_biased.%{soversion}
%{_libdir}/libabsl_hash.%{soversion}
%{_libdir}/libabsl_int128.%{soversion}
%{_libdir}/libabsl_kernel_timeout_internal.%{soversion}
%{_libdir}/libabsl_log_globals.%{soversion}
%{_libdir}/libabsl_log_internal_check_op.%{soversion}
%{_libdir}/libabsl_log_internal_format.%{soversion}
%{_libdir}/libabsl_log_internal_globals.%{soversion}
%{_libdir}/libabsl_log_internal_log_sink_set.%{soversion}
%{_libdir}/libabsl_log_internal_message.%{soversion}
%{_libdir}/libabsl_log_internal_nullguard.%{soversion}
%{_libdir}/libabsl_log_internal_proto.%{soversion}
%{_libdir}/libabsl_log_sink.%{soversion}
%{_libdir}/libabsl_low_level_hash.%{soversion}
%{_libdir}/libabsl_malloc_internal.%{soversion}
%{_libdir}/libabsl_raw_hash_set.%{soversion}
%{_libdir}/libabsl_raw_logging_internal.%{soversion}
%{_libdir}/libabsl_spinlock_wait.%{soversion}
%{_libdir}/libabsl_stacktrace.%{soversion}
%{_libdir}/libabsl_str_format_internal.%{soversion}
%{_libdir}/libabsl_strerror.%{soversion}
%{_libdir}/libabsl_string_view.%{soversion}
%{_libdir}/libabsl_strings.%{soversion}
%{_libdir}/libabsl_strings_internal.%{soversion}
%{_libdir}/libabsl_symbolize.%{soversion}
%{_libdir}/libabsl_synchronization.%{soversion}
%{_libdir}/libabsl_throw_delegate.%{soversion}
%{_libdir}/libabsl_time.%{soversion}
%{_libdir}/libabsl_time_zone.%{soversion}

%files -n libabsl_%{lname_suffix}
%license LICENSE
%{_libdir}/libabsl_bad_any_cast_impl.%{soversion}
%{_libdir}/libabsl_bad_optional_access.%{soversion}
%{_libdir}/libabsl_bad_variant_access.%{soversion}
%{_libdir}/libabsl_civil_time.%{soversion}
%{_libdir}/libabsl_cordz_sample_token.%{soversion}
%{_libdir}/libabsl_crc_cpu_detect.%{soversion}
%{_libdir}/libabsl_die_if_null.%{soversion}
%{_libdir}/libabsl_failure_signal_handler.%{soversion}
%{_libdir}/libabsl_flags_commandlineflag_internal.%{soversion}
%{_libdir}/libabsl_flags_commandlineflag.%{soversion}
%{_libdir}/libabsl_flags_config.%{soversion}
%{_libdir}/libabsl_flags_internal.%{soversion}
%{_libdir}/libabsl_flags_marshalling.%{soversion}
%{_libdir}/libabsl_flags_parse.%{soversion}
%{_libdir}/libabsl_flags_private_handle_accessor.%{soversion}
%{_libdir}/libabsl_flags_program_name.%{soversion}
%{_libdir}/libabsl_flags_reflection.%{soversion}
%{_libdir}/libabsl_flags_usage_internal.%{soversion}
%{_libdir}/libabsl_flags_usage.%{soversion}
%{_libdir}/libabsl_graphcycles_internal.%{soversion}
%{_libdir}/libabsl_hashtablez_sampler.%{soversion}
%{_libdir}/libabsl_leak_check.%{soversion}
%{_libdir}/libabsl_log_entry.%{soversion}
%{_libdir}/libabsl_log_flags.%{soversion}
%{_libdir}/libabsl_log_initialize.%{soversion}
%{_libdir}/libabsl_log_internal_conditions.%{soversion}
%{_libdir}/libabsl_log_internal_fnmatch.%{soversion}
%{_libdir}/libabsl_log_severity.%{soversion}
%{_libdir}/libabsl_periodic_sampler.%{soversion}
%{_libdir}/libabsl_random_distributions.%{soversion}
%{_libdir}/libabsl_random_internal_distribution_test_util.%{soversion}
%{_libdir}/libabsl_random_internal_platform.%{soversion}
%{_libdir}/libabsl_random_internal_pool_urbg.%{soversion}
%{_libdir}/libabsl_random_internal_randen_hwaes_impl.%{soversion}
%{_libdir}/libabsl_random_internal_randen_hwaes.%{soversion}
%{_libdir}/libabsl_random_internal_randen_slow.%{soversion}
%{_libdir}/libabsl_random_internal_randen.%{soversion}
%{_libdir}/libabsl_random_internal_seed_material.%{soversion}
%{_libdir}/libabsl_random_seed_gen_exception.%{soversion}
%{_libdir}/libabsl_random_seed_sequences.%{soversion}
%{_libdir}/libabsl_scoped_set_env.%{soversion}
%{_libdir}/libabsl_statusor.%{soversion}
%{_libdir}/libabsl_status.%{soversion}
%{_libdir}/libabsl_vlog_config_internal.%{soversion}

%files devel
%license LICENSE
%doc README.md
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so
%{_libdir}/pkgconfig/absl_*.pc

%changelog
