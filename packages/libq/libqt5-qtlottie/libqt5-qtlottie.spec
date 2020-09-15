#
# spec file for package libqt5-qtlottie
#
# Copyright (c) 2020 SUSE LLC
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


Name:           libqt5-qtlottie
Version:        5.15.1
Release:        0
Summary:        Qt 5 Quick Lottie Addon
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
URL:            https://www.qt.io
%define base_name libqt5
%define real_version 5.15.1
%define so_version 5.15.1
%define tar_version qtlottie-everywhere-src-5.15.1
Source:         https://download.qt.io/official_releases/qt/5.15/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml) >= %{version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{version}
%requires_ge    libQt5Gui5

%description
This package provides a QML module for Qt 5 which allows playing of BodyMovin
files from QML.

%package -n libQt5Bodymovin5
Summary:        Qt 5 BodyMovin Library
Group:          System/Libraries

%description -n libQt5Bodymovin5
Qt is a set of libraries for developing applications.

This package includes a library for reading BodyMovin animation files.

%package -n libQt5Bodymovin-devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       libQt5Bodymovin5 = %{version}

%description -n libQt5Bodymovin-devel
You need this package if you want to compile programs with the Qt BodyMovin
library.

%package -n libQt5Bodymovin-private-headers-devel
Summary:        Headers for the unstable API of the Qt5 BodyMovin library
Group:          Development/Libraries/X11
Requires:       libQt5Bodymovin-devel = %{version}

%description -n libQt5Bodymovin-private-headers-devel
You need this package if you want to compile programs against the unstable API
of the Qt5 BodyMovin library.

%prep
%autosetup -n %{tar_version}

%build
%qmake5
%make_jobs

%install
%qmake5_install
find %{buildroot}/%{_libqt5_libdir} -type f -name '*la' -print -exec perl -pi -e 's,-L%{_builddir}/\S+,,g' {} +
find %{buildroot}/%{_libqt5_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} + -exec sed -i -e "s,^moc_location=.*,moc_location=%{_lib}qt5_bindir/moc," -e "s,uic_location=.*,uic_location=%{_lib}qt5_bindir/uic," {} +
find %{buildroot}/%{_libqt5_libdir} -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} +

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%post -n libQt5Bodymovin5 -p /sbin/ldconfig
%postun -n libQt5Bodymovin5 -p /sbin/ldconfig

%files -n libQt5Bodymovin5
%license LICENSE.*
%{_libqt5_libdir}/libQt5Bodymovin.so.*

%files
%license LICENSE.*
%dir %{_libqt5_archdatadir}/qml/Qt/
%dir %{_libqt5_archdatadir}/qml/Qt/labs/
%dir %{_libqt5_archdatadir}/qml/Qt/labs/lottieqt/
%{_libqt5_archdatadir}/qml/Qt/labs/lottieqt/liblottieqtplugin.so
%{_libqt5_archdatadir}/qml/Qt/labs/lottieqt/plugins.qmltypes
%{_libqt5_archdatadir}/qml/Qt/labs/lottieqt/qmldir

# The entire library is private for now, so not all files are present.
%files -n libQt5Bodymovin-devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtBodymovin/%%{so_version}
%{_libqt5_includedir}/QtBodymovin
%{_libqt5_libdir}/cmake/Qt5Bodymovin
%{_libqt5_libdir}/libQt5Bodymovin.prl
%{_libqt5_libdir}/libQt5Bodymovin.so
#%%{_libqt5_libdir}/pkgconfig/Qt5Bodymovin.pc
#%%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_bodymovin.pri

%files -n libQt5Bodymovin-private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/QtBodymovin/%{so_version}
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_bodymovin_private.pri

%changelog
