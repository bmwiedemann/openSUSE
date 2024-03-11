#
# spec file for package libaccounts-qt
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
ExclusiveArch: do_not_build
%endif
%if "%{flavor}" == "qt6"
%define qt_major_ver 6
%define qt6 1
%endif
%if "%{flavor}" == "qt5"
%define qt_major_ver 5
%define qt5 1
%endif
%define soversion 1
%define rname libaccounts-qt
Name:           libaccounts-qt%{?qt_major_ver}
Version:        1.16git.20231124T162152~18557f7
Release:        0
Summary:        Qt library for Single Sign On
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/libaccounts-qt
Source:         %{rname}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt%{qt_major_ver}Core)
BuildRequires:  pkgconfig(Qt%{qt_major_ver}Test)
BuildRequires:  pkgconfig(Qt%{qt_major_ver}Xml)
BuildRequires:  pkgconfig(libaccounts-glib) >= 1.23

%description
This package contains the Qt library for Single Sign On.

%package -n libaccounts-qt%{qt_major_ver}-%{soversion}
Summary:        Qt library for Single Sign On

%description -n libaccounts-qt%{qt_major_ver}-%{soversion}
This package contains the Qt library for Single Sign On.

%package devel
Summary:        Development files for libaccounts-qt%{qt_major_ver}
Requires:       libaccounts-qt%{qt_major_ver}-%{soversion} = %{version}-%{release}

%description devel
This package contains the development files for the accounts-qt%{qt_major_ver} library.

# Only install the doc once
%if 0%{?qt6}
%package doc
Summary:        Documentation for libaccounts-qt
BuildArch:      noarch

%description doc
This package contains the documentation for the accounts-qt library.
%endif

%prep
%autosetup -p1 -n %{rname}-%{version}

# Fix documentation directory
sed -i '/^documentation.path/ s/doc\//doc\/packages\//' doc/doc.pri

%build
%if 0%{?qt6}
%qmake6 \
%else
%qmake5 \
%endif
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \

%make_jobs

%install
%if 0%{?qt6}
%qmake6_install
%else
%qmake5_install
%endif

# remove tests
rm %{buildroot}%{_bindir}/accountstest

%if 0%{?qt6}
%fdupes %{buildroot}%{_docdir}
%else
rm -r %{buildroot}%{_docdir}
%endif

%ldconfig_scriptlets -n libaccounts-qt%{qt_major_ver}-%{soversion}

%files -n libaccounts-qt%{qt_major_ver}-%{soversion}
%license COPYING
%doc README.md
%{_libdir}/libaccounts-qt%{qt_major_ver}.so.*

%files devel
%{_includedir}/accounts-qt%{qt_major_ver}/
%{_libdir}/libaccounts-qt%{qt_major_ver}.so
%{_libdir}/pkgconfig/accounts-qt%{qt_major_ver}.pc
%{_libdir}/cmake/AccountsQt%{qt_major_ver}/

%if 0%{?qt6}
%files doc
%doc %{_docdir}/accounts-qt/
%endif

%changelog
