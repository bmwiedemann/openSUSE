#
# spec file for package spectator
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


Name:           spectator
Version:        0.6+git74.9ef0de5
Release:        0
Summary:        System tray that downloads and display info about the Turris router
License:        GPL-3.0+
Group:          Productivity/Networking/Other
Url:            https://gitlab.labs.nic.cz/turris/spectator
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qttranslations
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
Requires:       openssl

%description
Spectator, systray tool to display various informations about the
Turris router from CZ.nic

%package     -n libturris-spectator0
Summary:        System tray that downloads and display info about the Turris router
Group:          System/Libraries

%description -n libturris-spectator0
Spectator, systray tool to display various informations about the
Turris router from CZ.nic

%package     -n libturris-spectator-devel
Summary:        Development files for libturris-spectator
Group:          Development/Libraries/C and C++
Requires:       libturris-spectator0 = %{version}

%description -n libturris-spectator-devel
The libturris-spectator-devel package contains libraries and header files for
developing applications that use libturris-spectator.

%prep
%setup -q
# old function fails with Qt 5.10
sed -e 's/lessThan(/versionAtLeast(/' -e 's/QT_VERSION/QT_VERSION_STR/' \
    -i spectator.pro
# set proper destination path
sed -e '/^target.path/s/lib/$${LIBDIR}/' -i library/library.pro

%build
%qmake5 PREFIX="%{_prefix}" LIBDIR="%{_lib}"
%make_jobs

%install
%{qmake5_install}

%post -n libturris-spectator0 -p /sbin/ldconfig

%postun -n libturris-spectator0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc CHANGELOG README.rst COPYING
%{_bindir}/turris-spectator
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%files -n libturris-spectator0
%defattr(-,root,root)
%{_libdir}/libturris-spectator.so.*

%files -n libturris-spectator-devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/libturris-spectator.so

%changelog
