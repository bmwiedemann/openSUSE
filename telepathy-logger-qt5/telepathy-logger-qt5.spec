#
# spec file for package telepathy-logger-qt5
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#
%define SOVERSION 5
Name:           telepathy-logger-qt5
Version:        17.08.0
Release:        0
Summary:        Qt Wrapper around TpLogger client library
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/KDE/telepathy-logger-qt
Source0:        telepathy-logger-qt-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  python-xml
BuildRequires:  telepathy-logger-devel >= 0.8.0
BuildRequires:  telepathy-qt5-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(telepathy-farstream)
BuildRequires:  pkgconfig(telepathy-glib)
Requires:       telepathy-logger >= 0.8.0
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
Telepathy-logger-qt5 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package devel
Summary:        Qt Wrapper around TpLogger client library
Group:          Development/Libraries/KDE
Requires:       libtelepathy-logger-qt%{SOVERSION} = %{version}
Requires:       telepathy-glib-devel
Requires:       telepathy-logger-devel >= 0.8.0
Conflicts:      telepathy-logger-qt4-devel

%description devel
Telepathy-logger-qt5 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%package -n libtelepathy-logger-qt%{SOVERSION}
Summary:        Qt Wrapper around TpLogger client library
Group:          Productivity/Networking/Instant Messenger

%description -n libtelepathy-logger-qt%{SOVERSION}
Telepathy-logger-qt5 is a Qt Wrapper around the TpLogger client library.
It is needed by KDE Telepathy in order to log the chat activity.

%prep
%setup -q -n telepathy-logger-qt-%{version}

%build
  %cmake_kf5 -d build -- -DPYTHON_EXECUTABLE=%{_bindir}/python2
  %make_jobs

%install
  %make_install -C build
  %fdupes -s %{buildroot}

%post -n libtelepathy-logger-qt%{SOVERSION} -p /sbin/ldconfig
%postun -n libtelepathy-logger-qt%{SOVERSION} -p /sbin/ldconfig

%files -n libtelepathy-logger-qt%{SOVERSION}
%license COPYING
%doc AUTHORS ChangeLog HACKING TODO
%{_kf5_libdir}/libtelepathy-logger-qt.so.*

%files devel
%{_kf5_libdir}/libtelepathy-logger-qt.so
%{_kf5_cmakedir}/TelepathyLoggerQt/
%{_includedir}/TelepathyLoggerQt/

%changelog
