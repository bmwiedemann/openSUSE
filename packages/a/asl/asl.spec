#
# spec file for package asl
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define rev 310
Name:           asl
Version:        1.42_bld%{rev}
Release:        0
Summary:        Macro Assembler AS
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://john.ccac.rwth-aachen.de:8000/as/
# Upstream serves source tarballs only from the non-standard port
# http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current-142-bld%%{rev}.tar.bz2
# which the OBS source validator cannot reach (factory-auto's download
# check fails on that host:port), so the tarball is tracked in the
# package and Source carries no URL.
Source:         asl-current-142-bld%{rev}.tar.bz2
Source2:        Makefile.def
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  texlive-german
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-makeindex

%description
AS is a portable macro cross-assembler for a variety of microprocessors
and controllers. Although it is mainly targeted at embedded processors
and single-board computers, you also find CPU families that are used in
workstations and PCs in the target list.

%prep
%autosetup -p1 -n asl-current
cp %{SOURCE2} .

%build
%make_build CFLAGS="%{optflags}"

%check
%make_build test

%install
%make_install INSTROOT=%{buildroot}%{_prefix} DOCDIR=share/doc/packages/asl MANDIR=share/man
# COPYING is shipped via %%license; drop the duplicate copy from the doc dir
rm %{buildroot}%{_defaultdocdir}/%{name}/COPYING

%files
%license COPYING
%{_defaultdocdir}/*
%{_bindir}/alink
%{_bindir}/asl
%{_bindir}/p2bin
%{_bindir}/p2hex
%{_bindir}/pbind
%{_bindir}/plist
%{_includedir}/asl/
%{_mandir}/man1/alink.1%{?ext_man}
%{_mandir}/man1/asl.1%{?ext_man}
%{_mandir}/man1/p2bin.1%{?ext_man}
%{_mandir}/man1/p2hex.1%{?ext_man}
%{_mandir}/man1/pbind.1%{?ext_man}
%{_mandir}/man1/plist.1%{?ext_man}

%changelog
