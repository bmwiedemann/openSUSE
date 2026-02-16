#
# spec file for package abseil-cpp
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global soversion so.2601.0.0
%global lname_suffix 2601_0_0
Name:           abseil-cpp
Version:        20260107.1
Release:        0
Summary:        C++ libraries which augment the C++ stdlib
License:        Apache-2.0
URL:            https://abseil.io/
Source0:        https://github.com/abseil/abseil-cpp/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         options-cxx17.patch
Patch1:         test_instance_tracker.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
Abseil is a collection of C++ libraries which augment the C++ standard
library. It also provides features incorporated into later C++ standards.

%define abseil_libs \
%abseil_libpackage -l libabsl_base \
%abseil_libpackage -l libabsl_borrowed_fixup_buffer \
%abseil_libpackage -l libabsl_city \
%abseil_libpackage -l libabsl_civil_time \
%abseil_libpackage -l libabsl_cord \
%abseil_libpackage -l libabsl_cord_internal \
%abseil_libpackage -l libabsl_cordz_functions \
%abseil_libpackage -l libabsl_cordz_handle \
%abseil_libpackage -l libabsl_cordz_info \
%abseil_libpackage -l libabsl_cordz_sample_token \
%abseil_libpackage -l libabsl_crc32c \
%abseil_libpackage -l libabsl_crc_cord_state \
%abseil_libpackage -l libabsl_crc_cpu_detect \
%abseil_libpackage -l libabsl_crc_internal \
%abseil_libpackage -l libabsl_debugging_internal \
%abseil_libpackage -l libabsl_decode_rust_punycode \
%abseil_libpackage -l libabsl_demangle_internal \
%abseil_libpackage -l libabsl_demangle_rust \
%abseil_libpackage -l libabsl_die_if_null \
%abseil_libpackage -l libabsl_examine_stack \
%abseil_libpackage -l libabsl_exponential_biased \
%abseil_libpackage -l libabsl_failure_signal_handler \
%abseil_libpackage -l libabsl_flags_commandlineflag \
%abseil_libpackage -l libabsl_flags_commandlineflag_internal \
%abseil_libpackage -l libabsl_flags_config \
%abseil_libpackage -l libabsl_flags_internal \
%abseil_libpackage -l libabsl_flags_marshalling \
%abseil_libpackage -l libabsl_flags_parse \
%abseil_libpackage -l libabsl_flags_private_handle_accessor \
%abseil_libpackage -l libabsl_flags_program_name \
%abseil_libpackage -l libabsl_flags_reflection \
%abseil_libpackage -l libabsl_flags_usage \
%abseil_libpackage -l libabsl_flags_usage_internal \
%abseil_libpackage -l libabsl_generic_printer_internal \
%abseil_libpackage -l libabsl_graphcycles_internal \
%abseil_libpackage -l libabsl_hash \
%abseil_libpackage -l libabsl_hashtable_profiler \
%abseil_libpackage -l libabsl_hashtablez_sampler \
%abseil_libpackage -l libabsl_int128 -d \-\
%abseil_libpackage -l libabsl_kernel_timeout_internal \
%abseil_libpackage -l libabsl_leak_check \
%abseil_libpackage -l libabsl_log_entry \
%abseil_libpackage -l libabsl_log_flags \
%abseil_libpackage -l libabsl_log_globals \
%abseil_libpackage -l libabsl_log_initialize \
%abseil_libpackage -l libabsl_log_internal_check_op \
%abseil_libpackage -l libabsl_log_internal_conditions \
%abseil_libpackage -l libabsl_log_internal_fnmatch \
%abseil_libpackage -l libabsl_log_internal_format \
%abseil_libpackage -l libabsl_log_internal_globals \
%abseil_libpackage -l libabsl_log_internal_log_sink_set \
%abseil_libpackage -l libabsl_log_internal_message \
%abseil_libpackage -l libabsl_log_internal_nullguard \
%abseil_libpackage -l libabsl_log_internal_proto \
%abseil_libpackage -l libabsl_log_internal_structured_proto \
%abseil_libpackage -l libabsl_log_severity \
%abseil_libpackage -l libabsl_log_sink \
%abseil_libpackage -l libabsl_malloc_internal \
%abseil_libpackage -l libabsl_periodic_sampler \
%abseil_libpackage -l libabsl_poison \
%abseil_libpackage -l libabsl_profile_builder \
%abseil_libpackage -l libabsl_random_distributions \
%abseil_libpackage -l libabsl_random_internal_distribution_test_util \
%abseil_libpackage -l libabsl_random_internal_entropy_pool \
%abseil_libpackage -l libabsl_random_internal_platform \
%abseil_libpackage -l libabsl_random_internal_randen \
%abseil_libpackage -l libabsl_random_internal_randen_hwaes \
%abseil_libpackage -l libabsl_random_internal_randen_hwaes_impl \
%abseil_libpackage -l libabsl_random_internal_randen_slow \
%abseil_libpackage -l libabsl_random_internal_seed_material \
%abseil_libpackage -l libabsl_random_seed_gen_exception \
%abseil_libpackage -l libabsl_random_seed_sequences \
%abseil_libpackage -l libabsl_raw_hash_set \
%abseil_libpackage -l libabsl_raw_logging_internal \
%abseil_libpackage -l libabsl_scoped_set_env \
%abseil_libpackage -l libabsl_spinlock_wait \
%abseil_libpackage -l libabsl_stacktrace \
%abseil_libpackage -l libabsl_status \
%abseil_libpackage -l libabsl_statusor \
%abseil_libpackage -l libabsl_strerror \
%abseil_libpackage -l libabsl_str_format_internal \
%abseil_libpackage -l libabsl_strings \
%abseil_libpackage -l libabsl_strings_internal \
%abseil_libpackage -l libabsl_symbolize \
%abseil_libpackage -l libabsl_synchronization \
%abseil_libpackage -l libabsl_throw_delegate \
%abseil_libpackage -l libabsl_time \
%abseil_libpackage -l libabsl_time_zone \
%abseil_libpackage -l libabsl_tracing_internal \
%abseil_libpackage -l libabsl_utf8_for_code_point \
%abseil_libpackage -l libabsl_vlog_config_internal \
%{nil}
# generator macro for -devel
%define abseil_libpackage(l:d:) Requires: %{-l*}%{-d*}%{lname_suffix} = %{version}

%package devel
Summary:        Header files for Abseil
%{abseil_libs}

%description devel
Abseil is a collection of C++ libraries which augment the C++ standard
library.

This package contains headers and build system files for it.

%define abseil_libpackage(l:d:) %package -n %{-l*}%{-d*}%{lname_suffix} \
Summary: Abseil library lib%{-l*} \
%description -n %{-l*}%{-d*}%{lname_suffix} \
This package contains the %{-l*} library for abseil. \
%files -n %{-l*}%{-d*}%{lname_suffix} \
%%license LICENSE \
%{_libdir}/%{-l*}.%{soversion} \
%ldconfig_scriptlets -n %{-l*}%{-d*}%{lname_suffix} \
%{nil}
%{abseil_libs}

%prep
%autosetup -p1
# create baselibs.conf
echo -n "" > %{SOURCE1}
%define abseil_libpackage(l:d:) echo "%{-l*}%{-d*}%{lname_suffix}" >> %{SOURCE1}
%{abseil_libs}

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/absl
%{_libdir}/cmake/absl
%{_libdir}/libabsl_*.so
%{_libdir}/pkgconfig/absl_*.pc

%changelog
