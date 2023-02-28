#
# spec file for package pam_wrapper
#
# Copyright (c) 2023 SUSE LLC
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


############################# NOTE ##################################
#
# This is a special library. You are not able to link this library.
# Do NOT create library package or a devel package!
#
############################# NOTE ##################################
%bcond_without python2
Name:           pam_wrapper
Version:        1.1.4
Release:        0
Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
URL:            https://cwrap.org/
Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz.asc
Source2:        %{name}-rpmlintrc
Patch0:         pam_wrapper-fix-cmocka-1.1.6+-support.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libcmocka-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
Recommends:     cmake
Recommends:     pkgconfig
%if %{with python2}
BuildRequires:  pkgconfig(python2)
%endif

%description
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module.

For testing PAM applications, a simple PAM module called pam_matrix is
included. If you plan to test a PAM module, you can use the pamtest library,
which simplifies testing of modules. You can combine it with the cmocka
unit testing framework, or you can use the provided Python bindings to
write tests for your module in Python.

This package does not have a devel package, because this project is for
development/testing.

%package -n libpamtest0
Summary:        A tool to test PAM applications and PAM modules
Requires:       pam_wrapper = %{version}-%{release}

%description -n libpamtest0
If you plan to test a PAM module, you can use this library, which simplifies
testing of modules.

%package -n libpamtest-devel
Summary:        A tool to test PAM applications and PAM modules
Requires:       libpamtest0 = %{version}-%{release}
Requires:       pam_wrapper = %{version}-%{release}
Recommends:     cmake
Recommends:     pkgconfig

%description -n libpamtest-devel
If you plan to develop tests for a PAM module, you can use this library,
which simplifies testing of modules. This subpackage includes the header
files for libpamtest

%package -n libpamtest-devel-doc
Summary:        The libpamtest API documentation

%description -n libpamtest-devel-doc
Documentation for libpamtest development.

%package -n python2-libpamtest
Summary:        A python wrapper for libpamtest
Requires:       libpamtest0 = %{version}-%{release}
Requires:       pam_wrapper = %{version}-%{release}

%description -n python2-libpamtest
If you plan to develop python tests for a PAM module, you can use this
library, which simplifies testing of modules. This subpackage includes
the header files for libpamtest

%package -n python3-libpamtest
Summary:        A python wrapper for libpamtest
Requires:       libpamtest0 = %{version}-%{release}
Requires:       pam_wrapper = %{version}-%{release}

%description -n python3-libpamtest
If you plan to develop python tests for a PAM module, you can use this
library, which simplifies testing of modules. This subpackage includes
the header files for libpamtest

%prep
%autosetup -p1

%build
# CMAKE_SKIP_RPATH:BOOL=OFF is required to run the tests!
%cmake \
  -DUNIT_TESTING=ON \
  -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake_build
%cmake_build doc

%install
%cmake_install

%if %{without python2}
rm -rf %{python2_sitearch}/pypamtest.so
%endif

%check
%ctest

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n libpamtest0 -p /sbin/ldconfig
%postun -n libpamtest0 -p /sbin/ldconfig

%files
%doc AUTHORS README.md CHANGELOG
%license LICENSE
%{_libdir}/libpam_wrapper.so*
%{_libdir}/pkgconfig/pam_wrapper.pc
%dir %{_libdir}/cmake/pam_wrapper
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config-version.cmake
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config.cmake
%dir %{_libdir}/pam_wrapper
%{_libdir}/pam_wrapper/pam_matrix.so
%{_libdir}/pam_wrapper/pam_chatty.so
%{_libdir}/pam_wrapper/pam_get_items.so
%{_libdir}/pam_wrapper/pam_set_items.so
%{_mandir}/man1/pam_wrapper.1%{?ext_man}
%{_mandir}/man8/pam_chatty.8%{?ext_man}
%{_mandir}/man8/pam_matrix.8%{?ext_man}
%{_mandir}/man8/pam_get_items.8%{?ext_man}
%{_mandir}/man8/pam_set_items.8%{?ext_man}

%files -n libpamtest0
%{_libdir}/libpamtest.so.*

%files -n libpamtest-devel
%{_libdir}/libpamtest.so
%{_libdir}/pkgconfig/libpamtest.pc
%dir %{_libdir}/cmake/pamtest
%{_libdir}/cmake/pamtest/pamtest-config-version.cmake
%{_libdir}/cmake/pamtest/pamtest-config-relwithdebinfo.cmake
%{_libdir}/cmake/pamtest/pamtest-config.cmake
%{_includedir}/libpamtest.h

%files -n libpamtest-devel-doc
%doc build/doc/html

%if %{with python2}
%files -n python2-libpamtest
%{python2_sitearch}/pypamtest.so
%endif

%files -n python3-libpamtest
%{python3_sitearch}/pypamtest.so

%changelog
