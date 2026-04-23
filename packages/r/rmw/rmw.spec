#
# spec file for package rmw
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           rmw
Version:        0.9.5
Release:        0
Summary:        Safe-remove utility for the command line
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://theimpossibleastronaut.github.io/rmw-website
Source:         https://github.com/theimpossibleastronaut/rmw/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(canfigger)
BuildRequires:  pkgconfig(ncurses)

%description
rmw (ReMove to Waste) is a safe-remove utility for the command line. It
can move and restore files to and from directories specified in a
configuration file, and can also be integrated with your regular
desktop trash folder (if your desktop environment uses the
FreeDesktop.org Trash specification). One of the unique features of rmw
is the ability to purge items from your waste (or trash) directories
after x number of days.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Ddocdir=%{_docdir}/%{name} \
	--buildtype=release \
	-Dstrip=true \
    -Db_sanitize=none
%meson_build

%install
%meson_install

%check
%meson_test

rm %{buildroot}%{_docdir}/%{name}/COPYING
%find_lang %{name}

%files lang -f %{name}.lang

%files
%{_bindir}/rmw
%{_docdir}/%{name}
%{_mandir}/man?/*1%{?ext_man}

%license COPYING

%changelog
