#
# spec file for package hardinfo2
#
# Copyright (c) 2024 SUSE LLC
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


Name:           hardinfo2
Version:        2.1.11
Release:        0
Summary:        A System Information and Benchmark for Linux
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-only
Group:          System/Benchmark
URL:            https://www.hardinfo2.org/
Source0:        https://github.com/hardinfo2/hardinfo2/archive/release-%{version}/%{name}-release-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  openSUSE-release
BuildRequires:  pciutils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(zlib)
Recommends:     Mesa-demo-x
Recommends:     dmidecode
Recommends:     iperf
Recommends:     lsscsi
Recommends:     sensors
Recommends:     sysbench
Recommends:     udisks2
Recommends:     xdg-utils

%description
Hardinfo2 is based on hardinfo.

Hardinfo2 offers System Information and Benchmark for Linux Systems. It is able
to obtain information from both hardware and basic software. It can benchmark
your system and compare to other machines online.

Features include:
 - Report generation (in either HTML or plain text)
 - Online Benchmarking - compare your machine against other machines

%prep
%autosetup -p1 -n %{name}-release-%{version}

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

desktop-file-install --vendor="" \
  --set-generic-name='Hardware Information' \
  --add-category="Settings;HardwareSettings;" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

%fdupes %{buildroot}%{_datadir}

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE LICENSE.1 LICENSE.2
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/hardinfo2.png
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
