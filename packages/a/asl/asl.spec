#
# spec file for package asl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           asl
Version:        1.42_bld144
Release:        0
Summary:        Macro Assembler AS
License:        GPL-2.0-or-later
Group:          Development/Languages/Other
Url:            http://john.ccac.rwth-aachen.de:8000/as/
Source:         http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current-142-bld115.tar.bz2
Patch0:         asl-buildfixes.patch
Patch2:         asl-ppc64.patch
BuildRequires:  gcc-c++
Obsoletes:      %{name}-doc

%description
AS is a portable macro cross-assembler for a variety of microprocessors
and controllers. Although it is mainly targeted at embedded processors
and single-board computers, you also find CPU families that are used in
workstations and PCs in the target list.

%prep
%setup -q -n asl-current
%patch0 -p1
%patch2 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing"

%check
make %{?_smp_mflags} test

%install
%make_install PREFIX=%{buildroot}

%files
%license COPYING
%doc README TODO
%{_bindir}/asl
%{_bindir}/alink
%{_bindir}/p2bin
%{_bindir}/p2hex
%{_bindir}/pbind
%{_bindir}/plist
%dir %{_includedir}/asl
%{_includedir}/asl/80c50x.inc
%{_includedir}/asl/80c552.inc
%{_includedir}/asl/bitfuncs.inc
%{_includedir}/asl/ctype.inc
%{_includedir}/asl/h8_3048.inc
%{_includedir}/asl/reg166.inc
%{_includedir}/asl/reg251.inc
%{_includedir}/asl/reg29k.inc
%{_includedir}/asl/reg53x.inc
%{_includedir}/asl/reg683xx.inc
%{_includedir}/asl/reg7000.inc
%{_includedir}/asl/reg78k0.inc
%{_includedir}/asl/reg96.inc
%{_includedir}/asl/regace.inc
%{_includedir}/asl/regavr.inc
%{_includedir}/asl/regcop8.inc
%{_includedir}/asl/reggp32.inc
%{_includedir}/asl/reghc08jb.inc
%{_includedir}/asl/reghc08q.inc
%{_includedir}/asl/reghc12.inc
%{_includedir}/asl/regm16c.inc
%{_includedir}/asl/regmsp.inc
%{_includedir}/asl/regst9.inc
%{_includedir}/asl/regz380.inc
%{_includedir}/asl/stddef04.inc
%{_includedir}/asl/stddef16.inc
%{_includedir}/asl/stddef17.inc
%{_includedir}/asl/stddef18.inc
%{_includedir}/asl/stddef2x.inc
%{_includedir}/asl/stddef37.inc
%{_includedir}/asl/stddef3x.inc
%{_includedir}/asl/stddef47.inc
%{_includedir}/asl/stddef51.inc
%{_includedir}/asl/stddef56k.inc
%{_includedir}/asl/stddef5x.inc
%{_includedir}/asl/stddef60.inc
%{_includedir}/asl/stddef62.inc
%{_includedir}/asl/stddef75.inc
%{_includedir}/asl/stddef87.inc
%{_includedir}/asl/stddef90.inc
%{_includedir}/asl/stddef96.inc
%{_includedir}/asl/stddefxa.inc
%{_includedir}/asl/stddefz8.inc
%{_includedir}/asl/reg6303.inc
%{_includedir}/asl/reg78310.inc
%{_includedir}/asl/stddef4x.inc
%dir %{_libexecdir}/asl
%{_libexecdir}/asl/as.msg
%{_libexecdir}/asl/alink.msg
%{_libexecdir}/asl/cmdarg.msg
%{_libexecdir}/asl/ioerrs.msg
%{_libexecdir}/asl/p2bin.msg
%{_libexecdir}/asl/p2hex.msg
%{_libexecdir}/asl/pbind.msg
%{_libexecdir}/asl/plist.msg
%{_libexecdir}/asl/tools.msg
%{_mandir}/man1/asl.1%{?ext_man}
%{_mandir}/man1/p2bin.1%{?ext_man}
%{_mandir}/man1/p2hex.1%{?ext_man}
%{_mandir}/man1/pbind.1%{?ext_man}
%{_mandir}/man1/plist.1%{?ext_man}
%{_mandir}/man1/alink.1%{?ext_man}

%changelog
