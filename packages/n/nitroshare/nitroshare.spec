#
# spec file for package nitroshare
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


%define _version 0.3
Name:           nitroshare
Version:        0.3.4
Release:        0
Summary:        Network file transfer application
License:        MIT
Group:          Productivity/Networking/File-Sharing
URL:            https://nitroshare.net/
Source:         https://launchpad.net/%{name}/%{_version}/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        https://launchpad.net/%{name}/%{_version}/%{version}/+download/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM nitroshare-fix-caja.patch sor.alexei@meowr.ru -- Use a correct Caja GI API version.
Patch0:         %{name}-fix-caja.patch
# PATCH-FIX-OPENSUSE nitroshare-fix-qt-5.11-build.patch -- Fix Qt 5.11+ compatibility.
Patch1:         %{name}-fix-qt-5.11-build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui) >= 5.1
BuildRequires:  pkgconfig(Qt5Network) >= 5.1
BuildRequires:  pkgconfig(Qt5Svg) >= 5.1
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.1

%description
A network file transfer application.
Features:
 * Automatic discovery of devices on the local network.
 * Simple and intuitive user interface.
 * Transfer entire directories.

%package -n caja-extension-%{name}
Summary:        NitroShare integration for Caja
Group:          Productivity/File utilities
Requires:       %{name} = %{version}
Requires:       caja
Supplements:    packageand(caja:%{name})

%description -n caja-extension-%{name}
A network file transfer application.
This package integrates NitroShare into Caja.

%package -n nautilus-extension-%{name}
Summary:        NitroShare integration for Nautilus
Group:          Productivity/File utilities
Requires:       %{name} = %{version}
Requires:       nautilus
Supplements:    packageand(nautilus:%{name})

%description -n nautilus-extension-%{name}
A network file transfer application.
This package integrates NitroShare into Nautilus.

%package -n nemo-extension-%{name}
Summary:        NitroShare integration for Nemo
Group:          Productivity/File utilities
Requires:       %{name} = %{version}
Requires:       nemo
Supplements:    packageand(nemo:%{name})

%description -n nemo-extension-%{name}
A network file transfer application.
This package integrates NitroShare into Nemo.

%package kde
Summary:        NitroShare integration into KDE
Group:          Productivity/File utilities
Requires:       %{name} = %{version}

%description kde
A network file transfer application.
This package integrates NitroShare into the KDE service menu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake
make %{?_smp_mflags} V=1

%install
%cmake_install
%suse_update_desktop_file -r %{name} Network FileTransfer

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%if 0%{?suse_version} >= 1500
%license LICENSE.txt
%else
%doc LICENSE.txt
%endif
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-send
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_mandir}/man?/%{name}.?%{?ext_man}

%files -n caja-extension-%{name}
%{_datadir}/caja-python/

%files -n nautilus-extension-%{name}
%{_datadir}/nautilus-python/

%files -n nemo-extension-%{name}
%{_datadir}/nemo-python/

%files kde
%dir %{_datadir}/kservices5/
%{_datadir}/kservices5/nitroshare_addtoservicemenu.desktop

%changelog
