#
# spec file for package xbench
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _xorg7libs %{_lib}
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %{_mandir}
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb %{_datadir}/X11/xkb
%define _xorg7_termcap %{_libexecdir}/X11/etc
%define _xorg7_serverincl %{_includedir}/xorg
%define _xorg7_fonts %{_datadir}/fonts
%define _xorg7_prefix /usr
Name:           xbench
Version:        0.2
Release:        0
Summary:        Benchmark for X11
License:        SUSE-Public-Domain
Group:          System/Benchmark
Url:            http://ftp.x.org/contrib/utilities/
Source:         http://ftp.x.org/contrib/utilities/%{name}-%{version}-src.tar.gz
Patch0:         xbench-%{version}.patch
Patch1:         xbench-%{version}-ia64.patch
Patch2:         xbench-%{version}-nonvoid.patch
Patch3:         xbench-%{version}-gets.patch
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A benchmark for X11.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
xmkmf -a
make %{?_smp_mflags} CCOPTIONS="%{optflags}"

%install
make "DESTDIR=%{buildroot}" install
make "DESTDIR=%{buildroot}" install.man
install -d %{buildroot}%{_defaultdocdir}/xbench
install -d %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/xbench/results
install -d %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/xbench/scripts
install -m 644 AUTHOR CHANGES IAFA-PACKAGE README xbench.doc Makefile script.run \
    %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/xbench
install -m 644 results/* %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/xbench/results
install -m 644 scripts/* %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/xbench/scripts
chmod a+x %{buildroot}%{_prefix}/%{_xorg7libshare}/X11/xbench/scripts/insSep.sh
cd %{buildroot}%{_defaultdocdir}/xbench; ln -sf ../../../../%{_xorg7libshare}/X11/xbench benchmarks

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/xbench
%doc %{_xorg7_mandir}/man1/xbench.1x*
%{_prefix}/%{_xorg7bin}/xbench
%{_prefix}/%{_xorg7libshare}/X11/xbench

%changelog
