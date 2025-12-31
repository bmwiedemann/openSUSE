#
# spec file for package wayclip
#
# Copyright (c) 2022 SUSE LLC
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


Name:           wayclip
Version:        0.5+git.1754102356.a0826e7
Release:        0
Summary:        Wayland clipboard utility
License:        ISC
URL:            https://sr.ht/~noocsharp/wayclip
Source0:        wayclip-%{version}.tar.xz
BuildRequires:  pkgconf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(wayland-client)

%description
wayclip is a pair of command-line utilities: waycopy
and waypaste, which allow access to the Wayland
clipboard. Specifically, wayclip is a wlr-data-control protocol
client.

%prep
%autosetup -p1 -n wayclip-%{version}

%build
export CFLAGS="%{optflags} $(pkgconf --cflags wayland-client)"
export LDLAGS="%{optflags} $(pkgconf --libs wayland-client)"
%make_build CC=gcc PREFIX="%{_prefix}"

%install
%make_install CC=gcc PREFIX="%{_prefix}"

%files
%license LICENSE
%doc README.md
%{_bindir}/waycopy
%{_bindir}/waypaste
%{_mandir}/man1/waycopy.1%{?ext_man}
%{_mandir}/man1/waypaste.1%{?ext_man}

%changelog
