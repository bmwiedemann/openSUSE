#
# spec file for package debugedit
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


Name:           debugedit
Version:        5.0
Release:        0
Summary:        Debuginfo extraction
License:        GPL-3.0-or-later
Group:          System/Packages
#Git-Clone:     https://sourceware.org/git/debugedit.git
URL:            https://www.sourceware.org/debugedit
Source0:        https://sourceware.org/ftp/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://sourceware.org/ftp/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch0:         finddebuginfo.patch
Patch1:         finddebuginfo-absolute-links.patch
Patch2:         debugsubpkg.patch
Patch3:         debuglink.patch
Patch4:         debuginfo-mono.patch
Patch5:         remove-bad-shift.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  help2man
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
# /usr/bin/gdb-add-index is optional
Suggests:       gdb
Requires:       binutils
Requires:       coreutils
Requires:       dwz
Requires:       elfutils
Requires:       findutils
Requires:       gawk
Requires:       grep
Requires:       sed
Requires:       xz

%description
debugedit provides programs and scripts for creating debuginfo and source file distributions,
collect build-ids and rewrite source paths in DWARF data for debugging, tracing and profiling.

%prep
%autosetup -p0

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}/usr/lib/rpm
mv %{buildroot}%{_bindir}/{find-debuginfo,sepdebugcrcfix} %{buildroot}/usr/lib/rpm
ln -s ../../bin/debugedit %{buildroot}/usr/lib/rpm

%files
%license COPYING3
%doc README
%{_bindir}/debugedit
/usr/lib/rpm/debugedit
/usr/lib/rpm/find-debuginfo
/usr/lib/rpm/sepdebugcrcfix
%{_mandir}/man1/debugedit.1%{?ext_man}
%{_mandir}/man1/find-debuginfo.1%{?ext_man}
%{_mandir}/man1/sepdebugcrcfix.1%{?ext_man}

%changelog
