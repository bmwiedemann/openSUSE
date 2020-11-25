#
# spec file for package systester
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


Name:           systester
Version:        1.5.1
Release:        0
Summary:        Benchmark and system stabilty tool
License:        GPL-2.0-or-later
Group:          System/Benchmark
URL:            http://systester.sourceforge.net
Source:         http://sourceforge.net/projects/systester/files/systester/1.5.0/%{name}-%{version}.tar.gz
Patch0:         systester-qt5.patch
BuildRequires:  gmp-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
ExclusiveArch:  ix86 x86_64

%description
System Stability Tester tries to test the system's stability by
calculating up to 128 millions of Pi digits. It supports multiple
calculation algorithms. For the moment only two have been
implemented. The Quadratic Convergence of Borwein and Gauss-Legendre,
the algorithm SuperPi uses.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%qmake5 systester.pro
%make_build
pushd cli
%make_build all lite
popd

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_docdir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/pixmaps
cp systester %{buildroot}/%{_bindir}
cp Authors Changelog COPYING FAQ.txt %{buildroot}/%{_docdir}/%{name}
cp images/systester.png %{buildroot}/%{_datadir}/pixmaps
cp systester.desktop %{buildroot}/%{_datadir}/applications
pushd cli
cp systester-cli %{buildroot}/%{_bindir}
cp systester-lite %{buildroot}/%{_bindir}
popd
%suse_update_desktop_file  -r %{name} Education Math System Monitor

%files
%license COPYING
%{_bindir}/systester
%{_bindir}/systester-cli
%{_bindir}/systester-lite
%doc %{_docdir}/%{name}
%{_datadir}/applications/systester.desktop
%{_datadir}/pixmaps/systester.png

%changelog
