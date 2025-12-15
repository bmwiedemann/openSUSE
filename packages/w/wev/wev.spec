#
# spec file for package wev
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           wev
Version:        1.1.0
Release:        0
Summary:        Wayland event viewer
License:        MIT
URL:            https://git.sr.ht/~sircmpwn/wev
Source0:        https://git.sr.ht/~sircmpwn/wev/archive/%{version}.tar.gz
BuildRequires:  libxkbcommon-devel
BuildRequires:  scdoc
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

%description
This is a tool for debugging events on a Wayland window, analagous to
the X11 tool xev.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README.md
%{_bindir}/wev
%{_mandir}/man1/wev.*

%changelog
