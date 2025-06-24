#
# spec file for package cpio
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


Name:           cpio
Version:        2.15
Release:        0
Summary:        A Backup and Archiving Utility
License:        GPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            https://www.gnu.org/software/cpio/cpio.html
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Patch2:         cpio-use_new_ascii_format.patch
Patch4:         cpio-use_sbin_rmt.patch
#PATCH-FIX-UPSTREAM cpio-2.12 cpio-open_nonblock.patch bnc#94449,
#https://savannah.gnu.org/patch/?9263 -- open device with O_NONBLOCK option
Patch5:         cpio-open_nonblock.patch
Patch15:        cpio-eof_tape_handling.patch
# make posibble to have device nodes with major number > 127
# Red Hat Bugzilla #450109
Patch17:        cpio-dev_number.patch
Patch18:        cpio-default_tape_dev.patch
#PATCH-FIX-UPSTREAM cpio-2.10-close_files_after_copy.patch
Patch20:        cpio-close_files_after_copy.patch
Patch21:        cpio-pattern-file-sigsegv.patch
Patch23:        paxutils-rtapelib_mtget.patch
Patch25:        cpio-fix_truncation_check.patch
Patch26:        fix-gcc14.patch
BuildRequires:  autoconf >= 2.71
BuildRequires:  automake
#Requires(post): %{xinstall_info_prereq}
#Requires(preun): %{xinstall_info_prereq}
Suggests:       rmt
Suggests:       %{name}-mt = %{version}

%description
GNU cpio is a program to manage archives of files. Cpio copies files
into or out of a cpio or tar archive. An archive is a file that contains
other files plus information about them, such as their pathname, owner,
time stamps, and access permissions. The archive can be another file on
the disk, a magnetic tape, or a pipe.

%package mt
Summary:        Tape drive control utility
Group:          Productivity/Archiving/Backup
Requires:       %{name} = %{version}
Requires(post): update-alternatives
Provides:       mt
Conflicts:      mt

%description mt
This package includes the 'mt', a local tape drive control program.

%lang_package

%prep
%setup -q
%autopatch -M 20 -p0
%autopatch -m 21 -p1

%build
gettextize -f --no-changelog
autoreconf -fiv
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -fcommon -std=gnu11"
%configure \
  --with-rmt="%{_bindir}/rmt" \
  --enable-mt \
  --disable-silent-rules \
  --program-transform-name='s/^mt$/gnumt/'
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/{usr/bin,bin}
%make_install
%if 0%{?suse_version} < 1550
ln -sf %{_bindir}/cpio %{buildroot}/bin
%endif

%find_lang %{name}

%check
make %{?_smp_mflags} check

%post mt
if [ ! -f %{_bindir}/gnumt ] ; then
   "%{_sbindir}/update-alternatives" --remove mt %{_bindir}/gnumt
fi

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING
%doc NEWS ChangeLog
%if 0%{?suse_version} < 1550
/bin/cpio
%endif
%{_bindir}/cpio
%{_infodir}/cpio.info%{?ext_info}
%{_mandir}/man1/cpio.1%{?ext_man}

%files mt
%ghost %{_bindir}/mt
%{_bindir}/gnumt
%ghost %{_mandir}/man1/mt.1%{ext_man}
%{_mandir}/man1/gnumt.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
