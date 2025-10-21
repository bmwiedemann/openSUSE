#
# spec file for package ebook2cwgui
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


Name:           ebook2cwgui
Version:        0.1.2
Release:        0
Summary:        GUI for ebook2cw
License:        GPL-2.0-or-later
URL:            https://fkurz.net/ham/ebook2cw.html#gui
Source:         https://fkurz.net/ham/ebook2cw/%{name}-%{version}.tar.gz
# Taken from Debian
Patch0:         wx3.0-compat.patch
BuildRequires:  c++_compiler
BuildRequires:  wxWidgets-devel
Requires:       ebook2cw

%description
A graphical user interface (GUI) for ebook2cw. The GUI uses the same
configuration file as ebook2cw, called ebook2cw.conf.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install \
	DESTDIR=%{buildroot}%{_prefix} \
	%{nil}

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/ebook2cwgui
%{_mandir}/man1/ebook2cwgui.1%{?ext_man}

%changelog
