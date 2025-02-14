#
# spec file for package paralleloverhead
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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


%define realname ParallelOverhead
Name:           paralleloverhead
Version:        1.1.3
Release:        0
Summary:        An endless runner game
License:        CC0-1.0 AND MIT
Group:          Amusements/Games/Action/Arcade
URL:            https://huitsi.net/ParallelOverhead/
#Git-Clone:     https://codeberg.org/Huitsi/ParallelOverhead.git
Source:         https://codeberg.org/Huitsi/ParallelOverhead/releases/download/%{version}/%{realname}-%{version}-source_with_built_assets.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl2)

%description
Parallel Overhead is a colorful endless runner game where you take control of
the ships Truth and Beauty on a groundbreaking trip through hyperspace. A
stable hyperspace tunnel has finally been achieved with the two ships
supporting it on opposite walls of the tunnel. Well, almost stable...
It's up to you to keep the ships from falling through the cracks!

%prep
%autosetup -n %{realname}-%{version}-source_with_built_assets/

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install prefix=%{_prefix} bindir=%{_bindir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/parallel_overhead
%{_datadir}/games/parallel_overhead/
%{_datadir}/icons/hicolor/48x48/apps/net.huitsi.ParallelOverhead.png
%{_datadir}/icons/hicolor/scalable/apps/net.huitsi.ParallelOverhead.svg
%{_mandir}/man6/parallel_overhead.6%{?ext_man}
%{_datadir}/applications/net.huitsi.ParallelOverhead.desktop
%{_datadir}/metainfo/net.huitsi.ParallelOverhead.metainfo.xml

%changelog
