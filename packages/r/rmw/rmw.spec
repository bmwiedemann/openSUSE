#
# spec file for package rmw
#
# Copyright (c) 2021 SUSE LLC
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
Version:        0.7.09
Release:        0
Summary:        Safe-remove utility for the command line
License:        GPL-3.0-or-later
URL:            https://remove-to-waste.info/
Source:         https://github.com/theimpossibleastronaut/rmw/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(ncurses)

%description
rmw (ReMove to Waste) is a safe-remove utility for the command line.
Its goal is to conform to the FreeDesktop.org Trash specification
and therefore be compatible with KDE, GNOME, XFCE, and others.
Desktop integration is optional however, and by default, rmw will
only use a waste folder separated from your desktop trash. One of
its unique features is the ability to purge files from your
Waste/Trash directories after x number of days.

%lang_package

%prep
%setup -q

%build
%configure \
	--docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
rm %{buildroot}%{_docdir}/%{name}/COPYING
%find_lang %{name}

%check
%make_build check

%files
%license COPYING
%{_bindir}/*
%{_docdir}/%{name}
%{_mandir}/man?/*1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
