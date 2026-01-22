#
# spec file for package wvkbd
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


Name:           wvkbd
Version:        0.19
Release:        0
Summary:        Wayland on-screen keyboard
License:        GPL-3.0-only
URL:            https://github.com/jjsullivan5196/wvkbd
Source:         https://github.com/jjsullivan5196/wvkbd/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cairo-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  pango-devel
BuildRequires:  scdoc
BuildRequires:  wayland-devel

%description
Wayland on-screen keyboard.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license COPYING
%doc README.md
%{_bindir}/wvkbd-mobintl
%{_mandir}/man1/wvkbd.1%{?ext_man}

%changelog
