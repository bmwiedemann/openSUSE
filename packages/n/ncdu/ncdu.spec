#
# spec file for package ncdu
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


Name:           ncdu
Version:        1.20
Release:        0
Summary:        NCurses Disk Usage
License:        MIT
URL:            https://dev.yorhel.nl/ncdu/
Source0:        https://dev.yorhel.nl/download/%{name}-%{version}.tar.gz
Source1:        https://dev.yorhel.nl/download/%{name}-%{version}.tar.gz.asc
Source2:        https://yorhel.nl/key.asc#/%{name}.keyring
BuildRequires:  pkgconfig(ncurses)

%description
ncdu (NCurses Disk Usage) is a curses-based version of
the well-known 'du', and provides a fast way to see what
directories are using your disk space.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
