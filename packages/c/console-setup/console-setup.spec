#
# spec file for package console-setup
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


Name:           console-setup
Version:        1.134
Release:        0
Summary:        Tools for configuring the console using X Window System key maps
License:        GPL-2.0-or-later AND MIT AND SUSE-Public-Domain
Group:          Applications/System
URL:            http://packages.debian.org/cs/sid/console-setup
Source:         http://ftp.de.debian.org/debian/pool/main/c/%{name}/%{name}_%{version}.tar.xz
# Fixes installing paths to Fedora style
Patch0:         console-setup-1.76-paths.patch
# Fixes FSF address, sent to upstream
Patch1:         console-setup-1.76-fsf-address.patch
# Backport fix from 1.143
Patch2:         console-setup-1.134-perl526.patch
# PATCH-FIX-UPSTREAM in 1.174
Patch3:         console-setup-1.134-reproducible.patch
# Fix Shift-Tab mapping (bsc#1122361)
Patch4:         u_fix-iso-left-tab.patch
# Fix using Caps_Lock where possible (bsc#1202853). Sent upstream.
Patch5:         0001-ckbcomp-Fix-check-for-non-ascii.patch

BuildRequires:  perl
BuildRequires:  perl(encoding)
# require 'xkeyboard-config' to have X Window keyboard descriptions?
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides the console with the same keyboard configuration
scheme that X Window System has. Besides the keyboard, the package configures
also the font on the console.  It includes a rich collection of fonts and
supports several languages that would be otherwise unsupported on the console
(such as Armenian, Georgian, Lao and Thai).

%prep
%setup -q
%patch0 -p1 -b .paths
%patch1 -p1 -b .fsf-address
%patch2 -p1 -b .perl526
%patch3 -p1 -b .reproducible
%patch4 -p1 -b .shift-tab
%patch5 -p1 -b .nonascii

%build
make build-linux

%install
make prefix=$RPM_BUILD_ROOT install-linux
# we don't want another set of keyboard descriptions, we want to use descriptions from
# xkeyboard-config (require it?), so removing it
# or maybe have these from tarball it in optional subpackage?
rm -rf $RPM_BUILD_ROOT/etc/console-setup

%files
%defattr(-,root,root)
%doc README COPYRIGHT CHANGES copyright.fonts copyright.xkb Fonts/copyright
%{_bindir}/ckbcomp
%{_bindir}/setupcon
%config(noreplace) %{_sysconfdir}/default/console-setup
%config(noreplace) %{_sysconfdir}/default/keyboard
%{_datadir}/consolefonts
%{_datadir}/consoletrans
%{_mandir}/*/*

%changelog
