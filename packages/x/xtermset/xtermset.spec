#
# spec file for package xtermset
#
# Copyright (c) 2025 SUSE LLC
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


Name:           xtermset
Version:        0.5.2
Release:        0
Summary:        A program to change the settings of an xterm
License:        GPL-2.0-or-later AND MIT
Group:          System/X11/Terminals
URL:            http://sourceforge.net/projects/clts/
Source:         http://downloads.sourceforge.net/project/clts/xtermset/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.dif
Patch1:         %{name}-%{version}-strcat.patch
Patch2:         %{name}-%{version}-dash.patch
Patch3:         xtermset-automake-1.13.patch
Patch4:         xtermset-gcc15.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Xtermset allows you to change the characteristics of an xterm window
from the command line. Most options have the same names as those that
you would give an xterm at startup.

%prep
%autosetup -p0

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/xtermset
%{_mandir}/man?/*
%{_datadir}/xtermset/

%changelog
