#
# spec file for package pcsc-tools
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.6.1
Release:        0
Summary:        Smart card tools
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Management
URL:            http://ludovic.rousseau.free.fr/softwares/pcsc-tools/
Source0:        http://ludovic.rousseau.free.fr/softwares/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://ludovic.rousseau.free.fr/softwares/%{name}/%{name}-%{version}.tar.bz2.asc
Source2:        pcsc-tools.keyring
Source3:        https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Source4:        https://www.gnu.org/licenses/gpl-3.0.txt
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
%setup -q
cp -v %{SOURCE3} %{SOURCE4} .
sed 's|#!/usr/bin/env perl|#!/usr/bin/perl|g' -i ATR_analysis gscriptor scriptor

%build
%configure
%make_build

%install
%make_install

%files
%license gpl*.txt
%doc Changelog README
%{_bindir}/ATR_analysis
%{_bindir}/gscriptor
%{_bindir}/pcsc_scan
%{_bindir}/scriptor
%{_datadir}/pcsc/
%{_mandir}/man1/*

%changelog
