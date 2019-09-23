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

%define build_folder bazel-bin/_solib_%{_arch}/
%ifarch x86_64
%define build_folder bazel-bin/_solib_k8/
%endif
%ifarch ppc64 ppc64le
%define build_folder bazel-bin/_solib_ppc/
%endif

Name:           abseil-cpp
Version:        20181127
Release:        0
Summary:        C++11 libraries which augment the C++ stdlib
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            https://abseil.io/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://github.com/bazelbuild/bazel-toolchains/archive/bc09b995c137df042bb80a395b73d7ce6f26afbe.tar.gz
Source2:        https://github.com/google/googletest/archive/b4d4438df9479675a632b2f11125e57133822ece.zip
Source3:        https://github.com/google/benchmark/archive/16703ff83c1ae6d53e5155df3bb3ab0bc96083be.zip
BuildRequires:  bazel0.19
BuildRequires:  gcc-c++
BuildRequires:  gtest
BuildRequires:  patchelf

%description
Abseil is a collection of C++11 libraries which augment the C++
standard library. It also provides features incorporated into C++14
and C++17 standards.

%package -n %{libname}
Summary:        C++11 libraries which augment the C++ stdlib
Group:          System/Libraries

%description -n %{libname}
Shared libraries for Abseil, a collection of C++11 libraries
which augment the C++ standard library. It also provides
features incorporated into C++14 and C++17 standards.

%package devel
Summary:        Development files for Abseil
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for Abseil, a collection of C++11 libraries
which augment the C++ standard library. It also provides
features incorporated into C++14 and C++17 standards.

%prep
%setup -q

%build
bazel build \
    -c dbg \
    --color=no \
    %(for opt in %{optflags}; do echo -e "--copt=${opt} \c"; done) \
    --curses=no \
    --distdir=%{_sourcedir} \
    --genrule_strategy=standalone \
    --host_javabase=@local_jdk//:jdk \
    --spawn_strategy=standalone \
    --strip=never \
    --verbose_failures \
    //...
bazel shutdown

%install
install -D -m0755 %{build_folder}/libabsl_Sbase_Slibbase.so %{buildroot}%{_libdir}/libabsl_base_libbase.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sbase_Slibdynamic_Uannotations.so %{buildroot}%{_libdir}/libabsl_base_libdynamic_annotations.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sbase_Slibexception_Usafety_Utesting.so %{buildroot}%{_libdir}/libabsl_base_libexception_safety_testing.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sbase_Slibmalloc_Uinternal.so %{buildroot}%{_libdir}/libabsl_base_libmalloc_internal.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sbase_Slibspinlock_Uwait.so %{buildroot}%{_libdir}/libabsl_base_libspinlock_wait.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sbase_Slibthrow_Udelegate.so %{buildroot}%{_libdir}/libabsl_base_libthrow_delegate.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Scontainer_Slibhash_Ugenerator_Utesting.so %{buildroot}%{_libdir}/libabsl_container_libhash_generator_testing.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Scontainer_Slibraw_Uhash_Uset.so %{buildroot}%{_libdir}/libabsl_container_libraw_hash_set.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Scontainer_Slibtest_Uinstance_Utracker.so %{buildroot}%{_libdir}/libabsl_container_libtest_instance_tracker.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibdebugging_Uinternal.so %{buildroot}%{_libdir}/libabsl_debugging_libdebugging_internal.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibdemangle_Uinternal.so %{buildroot}%{_libdir}/libabsl_debugging_libdemangle_internal.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibexamine_Ustack.so %{buildroot}%{_libdir}/libabsl_debugging_libexamine_stack.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibfailure_Usignal_Uhandler.so %{buildroot}%{_libdir}/libabsl_debugging_libfailure_signal_handler.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibleak_Ucheck_Uapi_Udisabled_Ufor_Utesting.so %{buildroot}%{_libdir}/libabsl_debugging_libleak_check_api_disabled_for_testing.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibleak_Ucheck_Uapi_Uenabled_Ufor_Utesting.so %{buildroot}%{_libdir}/libabsl_debugging_libleak_check_api_enabled_for_testing.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibstacktrace.so %{buildroot}%{_libdir}/libabsl_debugging_libstacktrace.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibstack_Uconsumption.so %{buildroot}%{_libdir}/libabsl_debugging_libstack_consumption.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sdebugging_Slibsymbolize.so %{buildroot}%{_libdir}/libabsl_debugging_libsymbolize.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Shash_Slibcity.so %{buildroot}%{_libdir}/libabsl_hash_libcity.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Shash_Slibhash.so %{buildroot}%{_libdir}/libabsl_hash_libhash.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Snumeric_Slibint128.so %{buildroot}%{_libdir}/libabsl_numeric_libint128.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sstrings_Slibinternal.so %{buildroot}%{_libdir}/libabsl_strings_libinternal.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sstrings_Slibstrings.so %{buildroot}%{_libdir}/libabsl_strings_libstrings.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Sstrings_Slibstr_Uformat_Uinternal.so %{buildroot}%{_libdir}/libabsl_strings_libstr_format_internal.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Ssynchronization_Slibgraphcycles_Uinternal.so %{buildroot}%{_libdir}/libabsl_synchronization_libgraphcycles_internal.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Ssynchronization_Slibper_Uthread_Usem_Utest_Ucommon.so %{buildroot}%{_libdir}/libabsl_synchronization_libper_thread_sem_test_common.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Ssynchronization_Slibsynchronization.so %{buildroot}%{_libdir}/libabsl_synchronization_libsynchronization.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stime_Sinternal_Scctz_Slibcivil_Utime.so %{buildroot}%{_libdir}/libabsl_time_internal_cctz_libcivil_time.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stime_Sinternal_Scctz_Slibtime_Uzone.so %{buildroot}%{_libdir}/libabsl_time_internal_cctz_libtime_zone.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stime_Slibtest_Uutil.so %{buildroot}%{_libdir}/libabsl_time_libtest_util.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stime_Slibtime.so %{buildroot}%{_libdir}/libabsl_time_libtime.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stypes_Slibbad_Uany_Ucast_Uimpl.so %{buildroot}%{_libdir}/libabsl_types_libbad_any_cast_impl.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stypes_Slibbad_Uoptional_Uaccess.so %{buildroot}%{_libdir}/libabsl_types_libbad_optional_access.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stypes_Slibbad_Uvariant_Uaccess.so %{buildroot}%{_libdir}/libabsl_types_libbad_variant_access.so.%{sover}
install -D -m0755 %{build_folder}/libabsl_Stypes_Sliboptional.so %{buildroot}%{_libdir}/libabsl_types_liboptional.so.%{sover}
# We can't patchelf libraries in the build step, because bazel saves the build
# output in protected read-only directory.
patchelf --set-soname libabsl_base_libbase.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libbase.so.%{sover}
patchelf --set-soname libabsl_base_libdynamic_annotations.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libdynamic_annotations.so.%{sover}
patchelf --set-soname libabsl_base_libexception_safety_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libexception_safety_testing.so.%{sover}
patchelf --set-soname libabsl_base_libmalloc_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libmalloc_internal.so.%{sover}
patchelf --set-soname libabsl_base_libspinlock_wait.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libspinlock_wait.so.%{sover}
patchelf --set-soname libabsl_base_libthrow_delegate.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libthrow_delegate.so.%{sover}
patchelf --set-soname libabsl_container_libhash_generator_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_container_libhash_generator_testing.so.%{sover}
patchelf --set-soname libabsl_container_libraw_hash_set.so.%{sover} %{buildroot}%{_libdir}/libabsl_container_libraw_hash_set.so.%{sover}
patchelf --set-soname libabsl_container_libtest_instance_tracker.so.%{sover} %{buildroot}%{_libdir}/libabsl_container_libtest_instance_tracker.so.%{sover}
patchelf --set-soname libabsl_debugging_libdebugging_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libdebugging_internal.so.%{sover}
patchelf --set-soname libabsl_debugging_libdemangle_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libdemangle_internal.so.%{sover}
patchelf --set-soname libabsl_debugging_libexamine_stack.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libexamine_stack.so.%{sover}
patchelf --set-soname libabsl_debugging_libfailure_signal_handler.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libfailure_signal_handler.so.%{sover}
patchelf --set-soname libabsl_debugging_libleak_check_api_disabled_for_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libleak_check_api_disabled_for_testing.so.%{sover}
patchelf --set-soname libabsl_debugging_libleak_check_api_enabled_for_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libleak_check_api_enabled_for_testing.so.%{sover}
patchelf --set-soname libabsl_debugging_libstacktrace.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libstacktrace.so.%{sover}
patchelf --set-soname libabsl_debugging_libstack_consumption.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libstack_consumption.so.%{sover}
patchelf --set-soname libabsl_debugging_libsymbolize.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libsymbolize.so.%{sover}
patchelf --set-soname libabsl_hash_libcity.so.%{sover} %{buildroot}%{_libdir}/libabsl_hash_libcity.so.%{sover}
patchelf --set-soname libabsl_hash_libhash.so.%{sover} %{buildroot}%{_libdir}/libabsl_hash_libhash.so.%{sover}
patchelf --set-soname libabsl_numeric_libint128.so.%{sover} %{buildroot}%{_libdir}/libabsl_numeric_libint128.so.%{sover}
patchelf --set-soname libabsl_strings_libinternal.so.%{sover} %{buildroot}%{_libdir}/libabsl_strings_libinternal.so.%{sover}
patchelf --set-soname libabsl_strings_libstrings.so.%{sover} %{buildroot}%{_libdir}/libabsl_strings_libstrings.so.%{sover}
patchelf --set-soname libabsl_strings_libstr_format_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_strings_libstr_format_internal.so.%{sover}
patchelf --set-soname libabsl_synchronization_libgraphcycles_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_synchronization_libgraphcycles_internal.so.%{sover}
patchelf --set-soname libabsl_synchronization_libper_thread_sem_test_common.so.%{sover} %{buildroot}%{_libdir}/libabsl_synchronization_libper_thread_sem_test_common.so.%{sover}
patchelf --set-soname libabsl_synchronization_libsynchronization.so.%{sover} %{buildroot}%{_libdir}/libabsl_synchronization_libsynchronization.so.%{sover}
patchelf --set-soname libabsl_time_internal_cctz_libcivil_time.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_internal_cctz_libcivil_time.so.%{sover}
patchelf --set-soname libabsl_time_internal_cctz_libtime_zone.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_internal_cctz_libtime_zone.so.%{sover}
patchelf --set-soname libabsl_time_libtest_util.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_libtest_util.so.%{sover}
patchelf --set-soname libabsl_time_libtime.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_libtime.so.%{sover}
patchelf --set-soname libabsl_types_libbad_any_cast_impl.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_libbad_any_cast_impl.so.%{sover}
patchelf --set-soname libabsl_types_libbad_optional_access.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_libbad_optional_access.so.%{sover}
patchelf --set-soname libabsl_types_libbad_variant_access.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_libbad_variant_access.so.%{sover}
patchelf --set-soname libabsl_types_liboptional.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_liboptional.so.%{sover}
ln -sf libabsl_base_libbase.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libbase.so
ln -sf libabsl_base_libdynamic_annotations.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libdynamic_annotations.so
ln -sf libabsl_base_libexception_safety_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libexception_safety_testing.so
ln -sf libabsl_base_libmalloc_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libmalloc_internal.so
ln -sf libabsl_base_libspinlock_wait.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libspinlock_wait.so
ln -sf libabsl_base_libthrow_delegate.so.%{sover} %{buildroot}%{_libdir}/libabsl_base_libthrow_delegate.so
ln -sf libabsl_container_libhash_generator_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_container_libhash_generator_testing.so
ln -sf libabsl_container_libraw_hash_set.so.%{sover} %{buildroot}%{_libdir}/libabsl_container_libraw_hash_set.so
ln -sf libabsl_container_libtest_instance_tracker.so.%{sover} %{buildroot}%{_libdir}/libabsl_container_libtest_instance_tracker.so
ln -sf libabsl_debugging_libdebugging_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libdebugging_internal.so
ln -sf libabsl_debugging_libdemangle_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libdemangle_internal.so
ln -sf libabsl_debugging_libexamine_stack.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libexamine_stack.so
ln -sf libabsl_debugging_libfailure_signal_handler.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libfailure_signal_handler.so
ln -sf libabsl_debugging_libleak_check_api_disabled_for_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libleak_check_api_disabled_for_testing.so
ln -sf libabsl_debugging_libleak_check_api_enabled_for_testing.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libleak_check_api_enabled_for_testing.so
ln -sf libabsl_debugging_libstacktrace.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libstacktrace.so
ln -sf libabsl_debugging_libstack_consumption.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libstack_consumption.so
ln -sf libabsl_debugging_libsymbolize.so.%{sover} %{buildroot}%{_libdir}/libabsl_debugging_libsymbolize.so
ln -sf libabsl_hash_libcity.so.%{sover} %{buildroot}%{_libdir}/libabsl_hash_libcity.so
ln -sf libabsl_hash_libhash.so.%{sover} %{buildroot}%{_libdir}/libabsl_hash_libhash.so
ln -sf libabsl_numeric_libint128.so.%{sover} %{buildroot}%{_libdir}/libabsl_numeric_libint128.so
ln -sf libabsl_strings_libinternal.so.%{sover} %{buildroot}%{_libdir}/libabsl_strings_libinternal.so
ln -sf libabsl_strings_libstrings.so.%{sover} %{buildroot}%{_libdir}/libabsl_strings_libstrings.so
ln -sf libabsl_strings_libstr_format_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_strings_libstr_format_internal.so
ln -sf libabsl_synchronization_libgraphcycles_internal.so.%{sover} %{buildroot}%{_libdir}/libabsl_synchronization_libgraphcycles_internal.so
ln -sf libabsl_synchronization_libper_thread_sem_test_common.so.%{sover} %{buildroot}%{_libdir}/libabsl_synchronization_libper_thread_sem_test_common.so
ln -sf libabsl_synchronization_libsynchronization.so.%{sover} %{buildroot}%{_libdir}/libabsl_synchronization_libsynchronization.so
ln -sf libabsl_time_internal_cctz_libcivil_time.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_internal_cctz_libcivil_time.so
ln -sf libabsl_time_internal_cctz_libtime_zone.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_internal_cctz_libtime_zone.so
ln -sf libabsl_time_libtest_util.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_libtest_util.so
ln -sf libabsl_time_libtime.so.%{sover} %{buildroot}%{_libdir}/libabsl_time_libtime.so
ln -sf libabsl_types_libbad_any_cast_impl.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_libbad_any_cast_impl.so
ln -sf libabsl_types_libbad_optional_access.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_libbad_optional_access.so
ln -sf libabsl_types_libbad_variant_access.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_libbad_variant_access.so
ln -sf libabsl_types_liboptional.so.%{sover} %{buildroot}%{_libdir}/libabsl_types_liboptional.so
for header in $(find . \( -name "*.h" -o -name "*.inc" \) -printf "%%P\n"); do
    install -D -m0644 $header %{buildroot}%{_includedir}/$header
done

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libabsl_base_libbase.so.%{sover}
%{_libdir}/libabsl_base_libdynamic_annotations.so.%{sover}
%{_libdir}/libabsl_base_libexception_safety_testing.so.%{sover}
%{_libdir}/libabsl_base_libmalloc_internal.so.%{sover}
%{_libdir}/libabsl_base_libspinlock_wait.so.%{sover} 
%{_libdir}/libabsl_base_libthrow_delegate.so.%{sover}
%{_libdir}/libabsl_container_libhash_generator_testing.so.%{sover}
%{_libdir}/libabsl_container_libraw_hash_set.so.%{sover}
%{_libdir}/libabsl_container_libtest_instance_tracker.so.%{sover}
%{_libdir}/libabsl_debugging_libdebugging_internal.so.%{sover}
%{_libdir}/libabsl_debugging_libdemangle_internal.so.%{sover}
%{_libdir}/libabsl_debugging_libexamine_stack.so.%{sover}
%{_libdir}/libabsl_debugging_libfailure_signal_handler.so.%{sover}
%{_libdir}/libabsl_debugging_libleak_check_api_disabled_for_testing.so.%{sover}
%{_libdir}/libabsl_debugging_libleak_check_api_enabled_for_testing.so.%{sover}
%{_libdir}/libabsl_debugging_libstacktrace.so.%{sover}
%{_libdir}/libabsl_debugging_libstack_consumption.so.%{sover}
%{_libdir}/libabsl_debugging_libsymbolize.so.%{sover}
%{_libdir}/libabsl_hash_libcity.so.%{sover}
%{_libdir}/libabsl_hash_libhash.so.%{sover}
%{_libdir}/libabsl_numeric_libint128.so.%{sover}
%{_libdir}/libabsl_strings_libinternal.so.%{sover}
%{_libdir}/libabsl_strings_libstrings.so.%{sover}
%{_libdir}/libabsl_strings_libstr_format_internal.so.%{sover}
%{_libdir}/libabsl_synchronization_libgraphcycles_internal.so.%{sover}
%{_libdir}/libabsl_synchronization_libper_thread_sem_test_common.so.%{sover}
%{_libdir}/libabsl_synchronization_libsynchronization.so.%{sover}
%{_libdir}/libabsl_time_internal_cctz_libcivil_time.so.%{sover}
%{_libdir}/libabsl_time_internal_cctz_libtime_zone.so.%{sover}
%{_libdir}/libabsl_time_libtest_util.so.%{sover}
%{_libdir}/libabsl_time_libtime.so.%{sover}
%{_libdir}/libabsl_types_libbad_any_cast_impl.so.%{sover}
%{_libdir}/libabsl_types_libbad_optional_access.so.%{sover}
%{_libdir}/libabsl_types_libbad_variant_access.so.%{sover}
%{_libdir}/libabsl_types_liboptional.so.%{sover}

%files devel
%{_includedir}/absl
%{_libdir}/libabsl_base_libbase.so
%{_libdir}/libabsl_base_libdynamic_annotations.so
%{_libdir}/libabsl_base_libexception_safety_testing.so
%{_libdir}/libabsl_base_libmalloc_internal.so
%{_libdir}/libabsl_base_libspinlock_wait.so
%{_libdir}/libabsl_base_libthrow_delegate.so
%{_libdir}/libabsl_container_libhash_generator_testing.so
%{_libdir}/libabsl_container_libraw_hash_set.so
%{_libdir}/libabsl_container_libtest_instance_tracker.so
%{_libdir}/libabsl_debugging_libdebugging_internal.so
%{_libdir}/libabsl_debugging_libdemangle_internal.so
%{_libdir}/libabsl_debugging_libexamine_stack.so
%{_libdir}/libabsl_debugging_libfailure_signal_handler.so
%{_libdir}/libabsl_debugging_libleak_check_api_disabled_for_testing.so
%{_libdir}/libabsl_debugging_libleak_check_api_enabled_for_testing.so
%{_libdir}/libabsl_debugging_libstacktrace.so
%{_libdir}/libabsl_debugging_libstack_consumption.so
%{_libdir}/libabsl_debugging_libsymbolize.so
%{_libdir}/libabsl_hash_libcity.so
%{_libdir}/libabsl_hash_libhash.so
%{_libdir}/libabsl_numeric_libint128.so
%{_libdir}/libabsl_strings_libinternal.so
%{_libdir}/libabsl_strings_libstrings.so
%{_libdir}/libabsl_strings_libstr_format_internal.so
%{_libdir}/libabsl_synchronization_libgraphcycles_internal.so
%{_libdir}/libabsl_synchronization_libper_thread_sem_test_common.so
%{_libdir}/libabsl_synchronization_libsynchronization.so
%{_libdir}/libabsl_time_internal_cctz_libcivil_time.so
%{_libdir}/libabsl_time_internal_cctz_libtime_zone.so
%{_libdir}/libabsl_time_libtest_util.so
%{_libdir}/libabsl_time_libtime.so
%{_libdir}/libabsl_types_libbad_any_cast_impl.so
%{_libdir}/libabsl_types_libbad_optional_access.so
%{_libdir}/libabsl_types_libbad_variant_access.so
%{_libdir}/libabsl_types_liboptional.so

%changelog
