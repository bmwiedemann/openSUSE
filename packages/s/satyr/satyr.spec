#
# spec file for package satyr
#
# Copyright (c) 2019-2024 Red Hat, Inc.
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


%define glib_ver 2.43.4

%if 0%{?fedora} || 0%{?rhel} > 7 || 0%{?suse_version} >= 1500
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif
%if 0%{?suse_version}
  %define python3_sphinx python311-Sphinx
  # separate shlib package (openSUSE shlibs packing guidelines)
  %define _libname libsatyr4
%else
  %define python3_sphinx python3-sphinx
  %define _libname %{name}
%endif
Name:           satyr
Version:        0.42
Release:        4%{?dist}
Summary:        Tools to create anonymous, machine-friendly problem reports
License:        GPL-2.0-or-later
URL:            https://github.com/abrt/satyr
Source0:        https://github.com/abrt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  automake
BuildRequires:  binutils-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  glib2-devel
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  rpm-devel
Requires:       glib2-tools%{?_isa} >= %{glib_ver}
%if %{with python3}
BuildRequires:  python3-devel
%endif
%if %{with python3}
BuildRequires:  %{python3_sphinx}
%endif

%description
Satyr is a library that can be used to create and process microreports.
Microreports consist of structured data suitable to be analyzed in a fully
automated manner, though they do not necessarily contain sufficient information
to fix the underlying problem. The reports are designed not to contain any
potentially sensitive data to eliminate the need for review before submission.
Included is a tool that can create microreports and perform some basic
operations on them.

%package -n %{_libname}
Summary:        Tools to create anonymous, machine-friendly problem reports

%description -n %{_libname}
Satyr is a library that can be used to create and process microreports.
Microreports consist of structured data suitable to be analyzed in a fully
automated manner, though they do not necessarily contain sufficient information
to fix the underlying problem. The reports are designed not to contain any
potentially sensitive data to eliminate the need for review before submission.

%package devel
Summary:        Development libraries for %{name}
Requires:       %{_libname}%{?_isa} = %{version}-%{release}

%description devel
Development libraries and headers for %{name}.

%if %{with python3}
%package -n python3-satyr
%{?python_provide:%python_provide python3-satyr}
Summary:        Python 3 bindings for %{name}
Requires:       %{_libname}%{?_isa} = %{version}-%{release}

%description -n python3-satyr
Python 3 bindings for %{name}.
%endif

%prep
%autosetup -p1

# SUSE-specific cleanup
%if 0%{?suse_version}
# Remove the doc file that automatically gets installed somewhere
sed -i '/README.md/d' ./Makefile.am
# Stacktrace test won't work on virtual build machine
sed -i '/core_stacktrace/d' ./tests/Makefile.am
%endif

%build
./autogen.sh
%configure \
%if %{without python3}
        --without-python3 \
%endif
        --disable-static \
        --enable-doxygen-docs

%make_build

%install
%make_install

# Remove all libtool archives (*.la) from modules directory.
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check|| {
    # find and print the logs of failed test
    # do not cat tests/testsuite.log because it contains a lot of bloat
    cat tests/test-suite.log
    find tests/testsuite.dir -name "testsuite.log" -print -exec cat '{}' +
    exit 1
}

%if 0%{?fedora} > 27
# ldconfig is not needed
%else
%if 0%{suse_version}
%ldconfig_scriptlets -n %{_libname}
%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif
%endif

%if 0%{?suse_version}
%files
%doc README.md NEWS
%{_bindir}/satyr
%license COPYING

%files -n %{_libname}
%license COPYING
%{_libdir}/lib*.so.*

%else

%files
%doc README.md NEWS
%license COPYING
%{_bindir}/satyr
%{_mandir}/man1/%{name}.1*
%{_libdir}/lib*.so.*
%endif

%files devel
# The complex pattern below (instead of simlpy *) excludes Makefile{.am,.in}:
%doc apidoc/html/*.{html,png,css,js}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%if 0%{?with_python3}
%files -n python3-satyr
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}/*
%endif

%changelog
