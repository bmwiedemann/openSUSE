#
# spec file for package firejail
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           firetools
Version:        0.9.62
Release:        0
Summary:        GUI for Firajail security sandbox
License:        GPL-2.0
Group:          Productivity/Security
Url:            https://firejail.wordpress.com/
Source0:        https://downloads.sourceforge.net/project/firejail/firetools/firetools-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/project/firejail/firetools/firetools-%{version}.tar.xz.asc
Patch:          firetools-0.9.62-fail_linking.patch
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  automake
BuildRequires:  autoconf
Requires:       firejail >= 0.9.40

%description
Firetools is the graphical user interface of Firejail security sandbox.

%prep
%autosetup -p1

%build
%configure --docdir=%{_docdir}/%{name} --with-qmake=`which qmake-qt5`
make %{?_smp_mflags} VERBOSE=1

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
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
