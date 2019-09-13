#
# spec file for package cdrdao
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           cdrdao
Version:        1.2.3
Release:        0
Summary:        Tool to write CD-Rs in Disk-At-Once Mode
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Record
Url:            http://cdrdao.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE cdrdao-build.patch
Patch0:         cdrdao-build.patch
# PATCH-FIX-OPENSUSE cdrdao-1.2.2-scan.patch bnc#144861 nadvornik@suse.cz -- Do not scan old ATAPI interface
Patch1:         cdrdao-1.2.2-scan.patch
# PATCH-FIX-OPENSUSE cdrdao-fixes.patch bnc#424635 nadvornik@suse.cz -- Fix cdrdao segfault
Patch2:         cdrdao-fixes.patch
# PATCH-FIX-OPENSUSE cdrdao-1.2.3-stat.patch asterios.dramis@gmail.com -- Missing includes causes failure build (patch taken from Fedora)
Patch3:         cdrdao-1.2.3-stat.patch
# PATCH-FIX-UPSTREAM cdrdao-gcc6-fixes.patch dimstar@opensuse.org -- Fix errors seen by GCC6.
Patch4:         cdrdao-gcc6-fixes.patch
BuildRequires:  gcc-c++
BuildRequires:  lame
BuildRequires:  libao-devel
BuildRequires:  libsigc++2-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(mad)
# For autoreconf
BuildRequires:  automake
BuildRequires:  gconf2-devel
Obsoletes:      gcdmaster <= 1.2.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CDRDAO creates CD-Rs in disk-at-once (DAO) mode driven by a description
file called a TOC file. In DAO mode, it is possible to create
non-standard track pregaps that have lengths other than 2 seconds and
contain nonzero audio data. This is useful for dividing live recordings
into tracks where 2 second gaps would be irritating.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1
%patch4 -p1

%build
autoreconf -fvi
%configure \
 --without-scglib
make %{?_smp_mflags} VERBOSE=1

%install
%make_install

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING CREDITS ChangeLog README README.PlexDAE cdrdao.lsm
%doc contrib/wav2dao/wav2dao.pl
%{_bindir}/cdrdao
%{_bindir}/cue2toc
%{_bindir}/toc2cddb
%{_bindir}/toc2cue
%{_datadir}/cdrdao/
%doc %{_mandir}/man1/cue2toc.1%{ext_man}
%doc %{_mandir}/man1/cdrdao.1%{ext_man}
%doc %{_mandir}/man1/toc2cddb.1%{ext_man}
%doc %{_mandir}/man1/toc2cue.1%{ext_man}

%changelog
