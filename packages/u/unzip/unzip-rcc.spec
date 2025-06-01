#
# spec file for package unzip-rcc
#
# Copyright (c) 2025 SUSE LLC
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


%define _name unzip
%define fileversion 60

%bcond_without rcc
%if %{with rcc}
BuildRequires:  librcc-devel
Suggests:       librcc0
Provides:       %{_name} = %{version}
Conflicts:      %{_name}
%else
Conflicts:      %{_name}-rcc
%endif
# NOTE: unzip.spec is the major file, if you want to update unzip-rcc.spec
# call pre_checkin.sh after editing unzip.spec

Name:           unzip-rcc
Version:        6.00
Release:        0
Summary:        A program to unpack compressed files
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
URL:            http://www.info-zip.org/
Source:         http://sourceforge.net/projects/infozip/files/UnZip%%206.x%%20%%28latest%%29/UnZip%%206.0/%{_name}%{fileversion}.tar.gz
Source1:        pre_checkin.sh
Patch0:         unzip.dif
Patch1:         unzip-iso8859_2.patch
Patch3:         unzip-optflags.patch
Patch4:         unzip-5.52-filename_too_long.patch
Patch5:         unzip-no_file_name_translation.patch
Patch8:         unzip-open_missing_mode.patch
Patch10:        unzip-5.52-use_librcc.patch
Patch11:        unzip-no-build-date.patch
Patch12:        unzip-dont_call_isprint.patch
Patch13:        Fix-CVE-2014-8139-unzip.patch
# http://pkgs.fedoraproject.org/cgit/rpms/unzip.git/plain/unzip-6.0-cve-2014-8139.patch
Patch14:        Fix-CVE-2014-8140-and-CVE-2014-8141.patch
Patch15:        CVE-2015-7696.patch
Patch16:        CVE-2015-7697.patch
Patch17:        CVE-2016-9844.patch
Patch18:        CVE-2014-9913.patch
Patch19:        CVE-2018-1000035.patch
Patch20:        Fix-CVE-2014-9636-unzip-buffer-overflow.patch
Patch21:        unzip60-total_disks_zero.patch
Patch22:        unzip60-cfactorstr_overflow.patch
Patch23:        unzip-initialize-the-symlink-flag.patch
# PATCH-FIX-UPSTREAM danilo.spinella@suse.com CVE-2022-0530 bsc#1196177
Patch24:        CVE-2022-0530.patch
# PATCH-FIX-UPSTREAM danilo.spinella@suse.com CVE-2022-0529 bsc#1196180
Patch25:        CVE-2022-0529.patch
Patch26:        unzip-time-decl.patch
Requires(post): update-alternatives
Recommends:     %{_name}-doc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
UnZip is an extraction utility for archives compressed in .zip format
(known as "zip files").  Although highly compatible both with PKWARE's
PKZIP(tm) and PKUNZIP utilities for MS-DOS and with Info-ZIP's own Zip
program, our primary objectives have been portability and non-MS-DOS
functionality. This version can also extract encrypted archives.

%package doc
Summary:        Documentation files for unzip
Group:          Productivity/Archiving/Compression
BuildArch:      noarch
%if %{with rcc}
Conflicts:      %{_name}-doc
%else
Conflicts:      %{_name}-rcc-doc
%endif

%description doc
UnZip is an extraction utility for archives compressed in .zip format
(known as "zip files").  Although highly compatible both with PKWARE's
PKZIP(tm) and PKUNZIP utilities for MS-DOS and with Info-ZIP's own Zip
program, our primary objectives have been portability and non-MS-DOS
functionality. This version can also extract encrypted archives.

%prep
%setup -q -n %{_name}%{fileversion}
%patch -P 0
%patch -P 1
%patch -P 3
%patch -P 4
%patch -P 5
%patch -P 8
%if %{with rcc}
%patch -P 10
%endif
%patch -P 11
%patch -P 12
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p0
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1
%patch -P 25 -p1
%patch -P 26 -p1

%build
export RPM_OPT_FLAGS="%{optflags} \
-D_GNU_SOURCE -DRCC_LAZY -DWILD_STOP_AT_DIR \
-DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT \
-DUNICODE_WCHAR -DUTF8_MAYBE_NATIVE -DNO_LCHMOD \
-DDATE_FORMAT=DF_YMD -I. -fstack-protector -fno-strict-aliasing -fPIE"

make %{?_smp_mflags}  -f unix/Makefile LF2="-ldl -pie" linux_noasm

%check
make %{?_smp_mflags} -f unix/Makefile check

%install
mkdir -p %{buildroot}%{_bindir}
# unzip funzip unzipsfx
for i in unzip funzip unzipsfx;	do
	install $i "%{buildroot}%{_bindir}/$i"
done

# zipinfo is just a symlink to unzip
ln -s unzip %{buildroot}%{_bindir}/zipinfo

# zipgrep comes from elsewhere in the build environment
install unix/zipgrep "%{buildroot}%{_bindir}/zipgrep"

# as both unzip and unzip-rcc now conflict, we provide the man
# packages through both packages
mkdir -p %{buildroot}%{_mandir}/man1
for i in man/*.1; do
 install -m 644 $i %{buildroot}%{_mandir}/man1/
done

%post
# remove old alternatives from when we were using update-alternatives
# zipinfo was never provided as an alternative
for bin in unzip funzip unzipsfx zipgrep; do
  %{_sbindir}/update-alternatives --remove $bin "%{_bindir}/$bin"-plain
  %{_sbindir}/update-alternatives --remove $bin "%{_bindir}/$bin"-rcc
done

%files
%defattr(-,root,root)
%{_bindir}/unzip
%{_bindir}/funzip
%{_bindir}/unzipsfx
%{_bindir}/zipinfo
%{_bindir}/zipgrep

%files doc
%defattr(-,root,root)
%{_mandir}/man1/*
%doc BUGS Contents History.* LICENSE README ToDo WHERE
%doc *.txt proginfo

%changelog
