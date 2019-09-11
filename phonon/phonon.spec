#
# spec file for package phonon
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


Name:           phonon
Version:        4.10.3
Release:        0
Summary:        Multimedia Platform Abstraction
License:        LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://phonon.kde.org/
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
BuildRequires:  libpulse-devel
BuildRequires:  libqt4-devel
BuildRequires:  xz

%description
Phonon is a cross-platform portable multimedia support abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package devel
Summary:        Phonon Multimedia Platform Abstraction
Group:          Development/Libraries/KDE
Requires:       libphonon4 = %{version}
Requires:       libqt4-devel

%description devel
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package -n libphonon4
Summary:        Phonon Multimedia Platform Abstraction
Group:          System/Libraries
%requires_ge    libqt4-x11
Recommends:     phonon-backend

%description -n libphonon4
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%prep
%setup -q

%build
  %cmake_kde4 -d build -- -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=true
  %make_jobs

%install
  %kde4_makeinstall -C build
  install -d -m 0755 %{buildroot}%{_libdir}/kde4/plugins
  install -d -m 0755 %{buildroot}%{_libdir}/kde4/plugins/phonon_backend
  %fdupes %{buildroot}%{_includedir}

%post   -n libphonon4 -p /sbin/ldconfig
%postun -n libphonon4 -p /sbin/ldconfig

%files -n libphonon4
%license COPYING.LIB
%{_libdir}/libphonon.so.*
%{_libdir}/libphononexperimental.so.*
%dir %{_libdir}/kde4/plugins
%dir %{_libdir}/kde4/plugins/phonon_backend

%files devel
%license COPYING.LIB
%{_datadir}/phonon/
%{_datadir}/qt4/mkspecs/modules/
%{_includedir}/phonon
%{_includedir}/KDE
%{_libdir}/libphonon.so
%{_libdir}/libphononexperimental.so
%{_libdir}/cmake/phonon/
%{_libdir}/pkgconfig/phonon.pc
%{_libdir}/qt4/plugins/designer/libphononwidgets.so
%{_datadir}/dbus-1/interfaces/org.kde.Phonon.AudioOutput.xml

%changelog
