#
# spec file for package firetools
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


Name:           firetools
Version:        0.9.72
Release:        0
Summary:        GUI for Firajail security sandbox
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://firejailtools.wordpress.com
Source0:        https://downloads.sourceforge.net/project/firejail/firetools/firetools-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/project/firejail/firetools/firetools-%{version}.tar.xz.asc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtbase-devel
Requires:       firejail >= 0.9.64

%description
Firetools is the graphical user interface of Firejail security sandbox.

%prep
%autosetup -p1

%build
%configure --docdir=%{_docdir}/%{name} --with-qmake=`which qmake-qt5`
%make_build VERBOSE=1

%install
%make_install
rm %{buildroot}%{_docdir}/%{name}/COPYING

%files
%doc README RELNOTES
%license COPYING
%{_bindir}/*
%{_prefix}/lib/firetools
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/*

%changelog
