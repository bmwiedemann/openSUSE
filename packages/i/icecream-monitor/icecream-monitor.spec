#
# spec file for package icecream-monitor
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           icecream-monitor
Version:        3.4
Release:        0
Summary:        Monitor Program for the icecream Compile Farm
License:        GPL-2.0-or-later
URL:            https://github.com/icecc/icemon
Source0:        icemon-%{version}.tar.xz
Source1:        icemon.1
Patch0:         make-pandoc-optional.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(icecc)
BuildRequires:  pkgconfig(lzo2)

%description
icecream is the next generation distcc. This package provides a monitor
program.

%prep
%autosetup -p1 -n icemon-%{version}

%build
%cmake
%make_jobs

%install
%cmake_install
# manpage pre-generated with pandoc 3.5, which is not in Factory
install -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/icemon.1

%files
%{_bindir}/icemon
%{_datadir}/applications/icemon.desktop
%{_datadir}/icons/hicolor/*/apps/icemon.*
%{_mandir}/man1/icemon.*

%changelog
