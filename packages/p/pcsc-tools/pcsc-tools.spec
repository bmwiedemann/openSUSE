#
# spec file for package pcsc-tools
#
# Copyright (c) 2023 SUSE LLC
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


Name:           pcsc-tools
Version:        1.7.2
Release:        0
Summary:        Smart card tools
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://pcsc-tools.apdu.fr/
Source0:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2
Source1:        https://pcsc-tools.apdu.fr/%{name}-%{version}.tar.bz2.asc
Source2:        pcsc-tools.keyring
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkgconfig
Requires:       perl-pcsc
Requires:       perl(Glib)
Requires:       perl(Gtk3)

%description
These tools are used to test a PC/SC driver, card or reader
or send commands in a friendly environment
(text or graphical user interface).

%prep
%autosetup -p1
sed 's|#!/usr/bin/env perl|#!/usr/bin/perl|g' -i ATR_analysis.in gscriptor scriptor

%build
%configure
%make_build

%install
%make_install

%files
%license LICENCE
%doc Changelog README
%{_bindir}/ATR_analysis
%{_bindir}/gscriptor
%{_bindir}/pcsc_scan
%{_bindir}/scriptor
%{_datadir}/pcsc/
%{_mandir}/man1/*
%{_datadir}/applications/gscriptor.desktop
%{_datadir}/locale/fr/LC_MESSAGES/pcsc-tools.mo
%{_datadir}/locale/ru/LC_MESSAGES/pcsc-tools.mo

%changelog
