#
# spec file for package asl
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


Name:           asl
Version:        1.42_bld232
Release:        0
Summary:        Macro Assembler AS
License:        GPL-2.0-only OR GPL-3.0-only
URL:            http://john.ccac.rwth-aachen.de:8000/as/
Source:         http://john.ccac.rwth-aachen.de:8000/ftp/as/source/c_version/asl-current-142-bld173.tar.bz2
Patch0:         asl-buildfixes.patch
BuildRequires:  gcc-c++
Obsoletes:      %{name}-doc

%description
AS is a portable macro cross-assembler for a variety of microprocessors
and controllers. Although it is mainly targeted at embedded processors
and single-board computers, you also find CPU families that are used in
workstations and PCs in the target list.

%prep
%autosetup -p1 -n asl-current

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing"

%check
make %{?_smp_mflags} test

%install
%make_install INSTROOT=%{buildroot}

%files
%license COPYING
%doc README TODO
%dir %{_prefix}/lib/asl
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
%{_prefix}/lib/asl/alink.msg
%{_prefix}/lib/asl/as.msg
%{_prefix}/lib/asl/cmdarg.msg
%{_prefix}/lib/asl/ioerrs.msg
%{_prefix}/lib/asl/p2bin.msg
%{_prefix}/lib/asl/p2hex.msg
%{_prefix}/lib/asl/pbind.msg
%{_prefix}/lib/asl/plist.msg
%{_prefix}/lib/asl/tools.msg

%changelog
