#
# spec file for package htop
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


Name:           htop
Version:        2.2.0
Release:        0
Summary:        An Interactive text-mode Process Viewer for Linux
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://hisham.hm/htop
Source0:        https://hisham.hm/htop/releases/%{version}/%{name}-%{version}.tar.gz
Source1:        https://hisham.hm/htop/releases/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch0:         htop-desktop-file-fix-thoenig-01.patch
# PATCH-FIX-OPENSUSE htop-script-python3.patch
Patch1:         htop-script-python3.patch
# PATCH-FIX-UPSTREAM This broke with commit db05ba61065f64b59d0014518be0786b5439e54c -- allow args for specific options
Patch2:         htop-2.2.0-fix-option-string.patch
# PATCH-FIX-UPSTREAM Make sure the auto-regenerated headers (after scripts/MakeHeader.py) actually compile
Patch3:         htop-2.2.0-fix-linux-process-ordering.patch
# PATCH-FIX-OPENSUSE htop-2.2.0-gcc10.patch https://github.com/hishamhm/htop/pull/981
Patch4:         htop-2.2.0-gcc10.patch
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  python3-base
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(ncurses)
Recommends:     lsof
Recommends:     strace

%description
htop is an interactive text-mode process viewer for Linux. It aims to be a
better 'top' and requires ncurses.

%prep
%autosetup -p1

%build
%configure \
  --enable-taskstats \
  --enable-unicode \
  --enable-linux-affinity \
  --enable-taskstats \
  --enable-delayacct \
  --enable-cgroup
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

%changelog
