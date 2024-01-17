#
# spec file for package qtmpris
#
# Copyright (c) 2021 SUSE LLC
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

%define sover                1
%define libqt5_includedir    %{_includedir}/qt5
%define libqt5_archdatadir   %{_libdir}/qt5

Name:           qtmpris
Summary:        Qt and QML MPRIS interface and adaptor
Version:        1.0.6
Release:        0
License:        LGPL-2.1+
URL:            https://github.com/sailfishos/qtmpris
Source:         https://github.com/sailfishos/qtmpris/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(dbusextended-qt5)
%if 0%{?suse_version} <= 1500
BuildRequires:  qtdbusextended-devel < 3.1.2
%endif

%description
MPRIS v.2 specification implementation for Qt and QML plugin.

%package -n libmpris-qt5-%{sover}
Summary:        Qtmpris libraries
Group:          System/Libraries

%description -n libmpris-qt5-%{sover}
This package contains the libraries for qtmpris

%package devel
Summary:        Development package for %{name}
Group:          Development/Libraries/Other
Requires:       libmpris-qt5-%{sover} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5
%make_build

%install
%qmake5_install

%post -n libmpris-qt5-%{sover} -p /sbin/ldconfig
%postun -n libmpris-qt5-%{sover} -p /sbin/ldconfig

%files
%doc README.md
%license COPYING
%defattr(-,root,root)
%dir %{_libqt5_archdatadir}/qml/org
%dir %{_libqt5_archdatadir}/qml/org/nemomobile/
%dir %{_libqt5_archdatadir}/qml/org/nemomobile/mpris/
%{_libqt5_archdatadir}/qml/org/nemomobile/mpris/*.so
%{_libqt5_archdatadir}/qml/org/nemomobile/mpris/plugins.qmltypes
%{_libqt5_archdatadir}/qml/org/nemomobile/mpris/qmldir

%files -n libmpris-qt5-%{sover}
%defattr(-,root,root)
%{_libdir}/libmpris-qt5.so.*

%files devel
%defattr(-,root,root)
%doc README.md
%license COPYING
%{libqt5_includedir}/MprisQt/
%{_libdir}/pkgconfig/mpris-qt5.pc
%{_libdir}/libmpris-qt5.so
%{_libqt5_archdatadir}/mkspecs/features/mpris-qt5.prf

%changelog
