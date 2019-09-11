#
# spec file for package zip
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           zip
Version:        3.0
Release:        0
%define file_version 30
Summary:        File compression program
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
Url:            https://github.com/distropatches/zip/commits/opensuse
Source:         http://downloads.sourceforge.net/project/infozip/Zip%203.x%20%28latest%29/3.0/zip30.tar.gz
Patch2:         zip-3.0-iso8859_2.patch
Patch3:         zip-3.0-add_options_to_help.patch
Patch4:         zip-3.0-nonexec-stack.patch
Patch5:         zip-3.0-optflags.patch
Patch6:         zip-3.0-tempfile.patch
Patch7:         zip-notimestamp.patch
Patch8:         zip-3.0-nomutilation.patch
# PATCH-FIX-UPSTREAM bsc#1068346 kstreitova@suse.com -- fix memory leaks
Patch9:         zip-3.0-fix-memory_leaks.patch
Patch10:        reproducible.patch
Patch11:        zip-3.0-fix-doc.patch
Provides:       crzip = %{version}
Obsoletes:      crzip < %{version}
BuildRequires:  libbz2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Zip is a compression and file packaging utility. It is compatible with
PKZIP(tm) 2.04g (Phil Katz ZIP) for MS-DOS systems.

%prep
%setup -q -n zip%{file_version}
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10 -p1
%patch11 -p1

%build
make %{?_smp_mflags} -f unix/Makefile prefix=/usr CC="gcc %{optflags} -DLARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" generic_gcc

%install
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{_mandir}/man1
make install -f unix/Makefile BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc BUGS CHANGES INSTALL LICENSE README TODO WHATSNEW WHERE
%doc %{_mandir}/man1/zip.1.gz
%doc %{_mandir}/man1/zipcloak.1.gz
%doc %{_mandir}/man1/zipnote.1.gz
%doc %{_mandir}/man1/zipsplit.1.gz
%{_bindir}/zip
%{_bindir}/zipcloak
%{_bindir}/zipnote
%{_bindir}/zipsplit

%changelog
