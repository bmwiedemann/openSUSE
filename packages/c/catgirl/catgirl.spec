#
# spec file for package catgirl
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           catgirl
Version:        2.2a
Release:        0
Summary:        IRC client
License:        GPL-3.0-or-later
URL:            https://git.causal.agency/catgirl/about/
Source:         https://git.causal.agency/catgirl/snapshot/%{name}-%{version}.tar.gz
BuildRequires:  ctags
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libtls)
# libtls is implemented by both libressl and libretls
BuildRequires:  libretls-devel
BuildRequires:  pkgconfig(ncursesw)

%description
catgirl is an ncurses based terminal IRC client. It supports the most common
IRC functions. It is configured from text files or the command line only and
enforces TLS secured connections.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE
%{_bindir}/catgirl
%{_mandir}/man1/catgirl.1%{?ext_man}

%changelog
