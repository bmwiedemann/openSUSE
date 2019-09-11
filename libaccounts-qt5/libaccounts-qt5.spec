#
# spec file for package libaccounts-qt5
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _soname 1
%define _tarbasename libaccounts-qt
%define _version VERSION_1.15-5b272ae218ccdf1f67f4eed92e2cdbe21c56ceb8
Name:           libaccounts-qt5
Version:        1.15
Release:        0
Summary:        Qt library for Single Sign On
License:        LGPL-2.1
Group:          System/Libraries
Url:            https://gitlab.com/accounts-sso/libaccounts-qt
Source:         https://gitlab.com/accounts-sso/%{_tarbasename}/repository/VERSION_%{version}/archive.tar.bz2#/%{_tarbasename}-%{_version}.tar.bz2
Source99:       baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(libaccounts-glib) >= 1.23

%description
This package contains the Qt library for Single Sign On.

%package -n libaccounts-qt5-%{_soname}
Summary:        Qt library for Single Sign On
Group:          System/Libraries

%description -n libaccounts-qt5-%{_soname}
This package contains the Qt library for Single Sign On.

%package devel
Summary:        Development files for libaccounts-qt
Group:          Development/Libraries/C and C++
Requires:       libaccounts-qt5-%{_soname} = %{version}-%{release}

%description devel
This package contains the development files for the accounts-qt library.

%package doc
Summary:        Documentation for libaccounts-qt
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the documentation for the accounts-qt library.

%prep
%setup -q -n %{_tarbasename}-%{_version}

# Fix documentation directory
sed -i '/^documentation.path/ s/doc\//doc\/packages\//' doc/doc.pri

%build
mkdir build
pushd build
%qmake5 \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    ..
%make_jobs
popd

%install
pushd build
%qmake5_install
popd

# remove tests
rm %{buildroot}%{_bindir}/accountstest

%fdupes %{buildroot}%{_docdir}/

%post -n libaccounts-qt5-%{_soname} -p /sbin/ldconfig

%postun -n libaccounts-qt5-%{_soname} -p /sbin/ldconfig

%files -n libaccounts-qt5-%{_soname}
%defattr(-,root,root)
%doc COPYING README.md
%{_libdir}/libaccounts-qt5.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/accounts-qt5/
%{_libdir}/libaccounts-qt5.so
%{_libdir}/pkgconfig/accounts-qt5.pc
%dir %{_libdir}/cmake/
%{_libdir}/cmake/AccountsQt5/

%files doc
%defattr(-,root,root)
%doc %{_docdir}/accounts-qt/

%changelog
