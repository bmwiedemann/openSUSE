#
# spec file for package htop
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


Name:           htop
Version:        3.2.2
Release:        0
Summary:        An Interactive text-mode Process Viewer for Linux
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://htop.dev
Source0:        https://github.com/htop-dev/htop/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(ncurses)
Recommends:     lsof
Recommends:     strace
%ifnarch        s390 s390x
BuildRequires:  libsensors4-devel
%endif

%description
htop is an interactive text-mode process viewer for Linux. It aims to be a
better 'top' and requires ncurses.

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
  --enable-taskstats \
  --enable-unicode \
  --enable-hwloc \
  --enable-delayacct \
  --enable-capabilities
%make_build

%install
%make_install
%suse_update_desktop_file -i %{name} System Monitor

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1%{?ext_man}
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/htop.svg

%changelog
