#
# spec file for package less
#
# Copyright (c) 2020 SUSE LLC
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


Name:           less
Version:        562
Release:        0
Summary:        Text File Browser and Pager Similar to more
License:        GPL-3.0-or-later OR BSD-2-Clause
Group:          Productivity/Text/Utilities
URL:            http://www.greenwoodsoftware.com/less/
Source:         http://www.greenwoodsoftware.com/less/less-%{version}.tar.gz
Source1:        README.SUSE
Source2:        lessopen.sh
Source3:        lessclose.sh
Source4:        lesskey.src
Source5:        http://www.greenwoodsoftware.com/less/less-%{version}.sig
Source6:        http://www.greenwoodsoftware.com/less/pubkey.asc#/%{name}.keyring
Patch0:         less-429-shell.patch
Patch1:         less-429-save_line_position.patch
Patch2:         less-429-more.patch
BuildRequires:  automake
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
Requires:       file

%description
less is a text file browser and pager similar to more. It allows
backward as well as forward movement within a file. Also, less does not
have to read the entire input file before starting. It is possible to
start an editor at any time from within less.

%prep
%setup -q
%patch0 -p1
%patch1
%patch2
#
# the ./configure script is not writable for the normal user
# rather fix permissions for all files
chmod u+w *
#
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure --with-pic
#
# regenerate help.c because less.hlp was patched
./mkhelp.pl <less.hlp >help.c
#
# build less
%make_build

%install
%make_install
#
# lesskey
install -m 755 -d %{buildroot}/%{_distconfdir}
install -m 644 lesskey.src %{buildroot}/%{_distconfdir}/lesskey
%{buildroot}%{_bindir}/lesskey -o %{buildroot}%{_distconfdir}/lesskey.bin %{buildroot}%{_distconfdir}/lesskey
#
# preprocessor
install -m 755 lessopen.sh lessclose.sh %{buildroot}/%{_bindir}
chmod -x LICENSE COPYING NEWS README.SUSE

%files
%license LICENSE COPYING
%doc NEWS README.SUSE
%{_mandir}/*/*
%{_distconfdir}/*
%{_bindir}/*

%changelog
