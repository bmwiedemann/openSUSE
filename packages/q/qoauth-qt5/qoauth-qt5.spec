#
# spec file for package qoauth-qt5
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           qoauth-qt5
Version:        2.0.0
Release:        0
Summary:        Library for interaction with OAuth-powered network services
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/ayoy/qoauth
Source:         qoauth-%{version}.tar.gz
# PATCH-FIX-OPENSUSE qoauth-qt5-rpmoptflags.patch crrodriguez@opensuse.org
Patch0:         qoauth-qt5-rpmoptflags.patch
# PATCH-FIX-OPENSUSE qoauth-qt5-ppc64-libdir.patch uweigand@de.ibm.com
Patch2:         qoauth-qt5-ppc64-libdir.patch
# PATCH-FIX-OPENSUSE pcfile.patch wbauer@tmo.at -- Adjust the pkgconfig file to Qt5.
Patch3:         pcfile.patch
# PATCH-FIX-OPENSUSE qoauth-qt5-fix-includedir.patch sor.alexei@meowr.ru -- Fix the include directory.
Patch4:         qoauth-qt5-fix-includedir.patch
BuildRequires:  libqca-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)

%description
QOAuth supports interaction with OAuth-powered network services,
in the style of Qt libraries.

%package -n libqoauth2
Summary:        Library for interaction with OAuth-powered network services
Group:          System/Libraries

%description -n libqoauth2
QOAuth supports interaction with OAuth-powered network services,
in the style of Qt libraries.

%package devel
Summary:        Development files for QOAuth
Group:          Development/Libraries/C and C++
Requires:       libqoauth2 = %{version}
Conflicts:      qoauth-devel

%description devel
QOAuth supports interaction with OAuth-powered network services,
in the style of Qt libraries.

This package contains files for developing applications using QOAuth.

%prep
%setup -q -n qoauth-%{version}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%qmake5
make %{?_smp_mflags} V=1

%install
%qmake5_install

%post -n libqoauth2 -p /sbin/ldconfig

%postun -n libqoauth2 -p /sbin/ldconfig

%files -n libqoauth2
%defattr(-,root,root)
%license LICENSE
%{_libdir}/libqoauth.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/QtOAuth
%{_libdir}/libqoauth.so
%{_libdir}/libqoauth.prl
%{_libdir}/pkgconfig/qoauth.pc
%dir %{_libdir}/qt5/
%dir %{_libdir}/qt5/mkspecs/
%dir %{_libdir}/qt5/mkspecs/features/
%{_libdir}/qt5/mkspecs/features/oauth.prf

%changelog
