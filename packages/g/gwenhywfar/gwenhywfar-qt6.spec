#
# spec file for package gwenhywfar-qt6
#
# Copyright (c) 2025 SUSE LLC
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


%define libversion 79
%define devversion 5
%define devrelease 5.14
# Beta does not mean "before release" but a release that is considered as beta:
%define _version %{version}
%define _name gwenhywfar
%define releasenumber 630
%define checksumreleasenumber 629
%bcond_without configure
Name:           gwenhywfar-qt6
Version:        5.14.1
Release:        0
Summary:        Multiplatform helper library for other libraries
License:        LGPL-2.1-or-later
URL:            https://www.aquamaniac.de/rdm/projects/gwenhywfar
Source:         https://www.aquamaniac.de/rdm/attachments/download/%{releasenumber}/%{_name}-%{_version}.tar.gz
Source1:        https://www.aquamaniac.de/rdm/attachments/download/%{checksumreleasenumber}/%{_name}-%{_version}.tar.gz.asc
Source2:        gwenhywfar.keyring
BuildRequires:  fdupes
%if 0%{?suse_version} < 1600
BuildRequires:  gcc13
BuildRequires:  gcc13-PIE
%endif
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(gnutls) >= 2.9.8
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(libgcrypt) >= 1.2.0
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(openssl)
%if %{with configure}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

%description
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes some
often needed functions (for example, handling and parsing of
configuration files, reading and writingof XML files, and interprocess
communication).

%package -n libgwengui-qt6-%{libversion}
Summary:        Qt6 UI backend for the gwenhywfar multi-platform helper library

%description -n libgwengui-qt6-%{libversion}
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (for example, for handling and parsing of
configuration files, reading and writing of XML files, and interprocess
communication).

This package provides the Qt6 implementation of the generic UI toolkit.

%package devel
Summary:        Header files for the Gwenhywfar multi-platform helper library
Requires:       glibc-devel
Requires:       gwenhywfar-devel = %{version}
Requires:       libgwengui-qt6-%{libversion} = %{version}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Widgets)

%description devel
Gwenhywfar is a base library used to provide OS abstraction functions
for Linux, FreeBSD, OpenBSD, NetBSD, and Windows. It also includes
some often needed functions (e.g. for handling and parsing of
configuration files, reading/writing of XML files, interprocess
communication etc).

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{_version}

%build
%if 0%{?suse_version} < 1600
export CC=gcc-13 CXX=g++-13
%endif

export PATH=%{_qt6_bindir}:$PATH

%if %{with configure}
autoreconf -ifv -I /usr/share/gettext/m4
%endif

# with-guis=qt5 will build with Qt 6
%configure\
  --enable-release\
  --disable-static \
  --with-guis="qt5" \
  --with-plugins-ct= \
  --with-plugins-cfgmgr= \
  --with-plugins-dbio=

%make_jobs

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

# Cleanup, we only want Qt 6 related files
rm -r %{buildroot}%{_bindir}
rm -r %{buildroot}%{_datadir}
# Headers are identical for both Qt 5 and 6 and we can't have 'Conflicts'
rm -r %{buildroot}%{_includedir}
rm -r %{buildroot}%{_libdir}/cmake/{gwengui-cpp,gwenhywfar}*
rm %{buildroot}%{_libdir}/{libgwengui-cpp,libgwenhywfar}.*
rm %{buildroot}%{_libdir}/pkgconfig/gwenhywfar.pc

%fdupes %{buildroot}%{_libdir}/cmake

%ldconfig_scriptlets -n libgwengui-qt6-%{libversion}

%files -n libgwengui-qt6-%{libversion}
%license COPYING
%{_libdir}/libgwengui-qt6.so.*

%files devel
%{_libdir}/libgwengui-qt6.so
%{_libdir}/pkgconfig/gwengui-qt6.pc
%dir %{_libdir}/cmake
%{_libdir}/cmake/gwengui-qt6-%{devrelease}

%changelog
