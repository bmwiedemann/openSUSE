#
# spec file for package pam_wrapper
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


############################# NOTE ##################################
#
# This is a special library. You are not able to link this library.
# Do NOT create library package or a devel package!
#
############################# NOTE ##################################

Name:           pam_wrapper
Version:        1.0.7
Release:        0

Summary:        A tool to test PAM applications and PAM modules
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            http://cwrap.org/

Source0:        https://ftp.samba.org/pub/cwrap/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libcmocka-devel
BuildRequires:  pam-devel
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)

Recommends:     pkg-config
Recommends:     cmake

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
Group:          Development/Libraries/C and C++
Requires:       pam_wrapper = %{version}-%{release}

%description -n libpamtest0
If you plan to test a PAM module, you can use this library, which simplifies
testing of modules.

%package -n libpamtest-devel
Summary:        A tool to test PAM applications and PAM modules
Group:          Development/Libraries/C and C++
Requires:       libpamtest0 = %{version}-%{release}
Requires:       pam_wrapper = %{version}-%{release}

Recommends:     pkg-config
Recommends:     cmake

%description -n libpamtest-devel
If you plan to develop tests for a PAM module, you can use this library,
which simplifies testing of modules. This subpackage includes the header
files for libpamtest

%package -n libpamtest-devel-doc
Summary:        The libpamtest API documentation
Group:          Development/Libraries/C and C++

%description -n libpamtest-devel-doc
Documentation for libpamtest development.

%package -n python2-libpamtest
Summary:        A python wrapper for libpamtest
Group:          Development/Libraries/C and C++
Requires:       libpamtest0 = %{version}-%{release}
Requires:       pam_wrapper = %{version}-%{release}

%description -n python2-libpamtest
If you plan to develop python tests for a PAM module, you can use this
library, which simplifies testing of modules. This subpackage includes
the header files for libpamtest

%package -n python3-libpamtest
Summary:        A python wrapper for libpamtest
Group:          Development/Libraries/C and C++
Requires:       libpamtest0 = %{version}-%{release}
Requires:       pam_wrapper = %{version}-%{release}

%description -n python3-libpamtest
If you plan to develop python tests for a PAM module, you can use this
library, which simplifies testing of modules. This subpackage includes
the header files for libpamtest

%prep
%setup -q

%build
# CMAKE_SKIP_RPATH:BOOL=OFF is required to run the tests!
%cmake \
  -DUNIT_TESTING=ON \
  -DCMAKE_SKIP_RPATH:BOOL=OFF

make %{?_smp_mflags} VERBOSE=1
make %{?_smp_mflags} doc

%install
%cmake_install

%check
%ctest

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n libpamtest0 -p /sbin/ldconfig

%postun -n libpamtest0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%license LICENSE
%{_libdir}/libpam_wrapper.so*
%{_libdir}/pkgconfig/pam_wrapper.pc
%dir %{_libdir}/cmake/pam_wrapper
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config-version.cmake
%{_libdir}/cmake/pam_wrapper/pam_wrapper-config.cmake
%dir %{_libdir}/pam_wrapper
%{_libdir}/pam_wrapper/pam_matrix.so
%{_libdir}/pam_wrapper/pam_get_items.so
%{_libdir}/pam_wrapper/pam_set_items.so
%{_mandir}/man1/pam_wrapper.1*
%{_mandir}/man8/pam_matrix.8*
%{_mandir}/man8/pam_get_items.8*
%{_mandir}/man8/pam_set_items.8*

%files -n libpamtest0
%defattr(-,root,root,-)
%{_libdir}/libpamtest.so.*

%files -n libpamtest-devel
%defattr(-,root,root,-)
%{_libdir}/libpamtest.so
%{_libdir}/pkgconfig/libpamtest.pc
%dir %{_libdir}/cmake/libpamtest
%{_libdir}/cmake/libpamtest/libpamtest-config-version.cmake
%{_libdir}/cmake/libpamtest/libpamtest-config.cmake
%{_includedir}/libpamtest.h

%files -n libpamtest-devel-doc
%defattr(-,root,root)
%doc build/doc/html

%files -n python2-libpamtest
%{python2_sitearch}/pypamtest.so

%files -n python3-libpamtest
%{python3_sitearch}/pypamtest.so

%changelog
