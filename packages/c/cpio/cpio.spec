#
# spec file for package cpio
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.12
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
Patch24:        cpio-check_for_symlinks.patch
Patch25:        cpio-fix_truncation_check.patch
Patch26:        cpio-2.12-util.c_no_return_in_nonvoid_fnc.patch
Patch27:        cpio-2.12-out_of_bounds_write.patch
BuildRequires:  autoconf
BuildRequires:  automake
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Recommends:     %{name}-lang = %{version}
Recommends:     %{name}-mt = %{version}
Recommends:     rmt

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
Requires(postun): update-alternatives
Provides:       mt

%description mt
This package includes the 'mt', a local tape drive control program.

%lang_package

%prep
%setup -q
%patch2
%patch4
%patch5
%patch15
%patch17
%patch18
%patch20
%patch21 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1

%build
gettextize -f --no-changelog
autoreconf -fiv
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
%configure \
  --with-rmt="%{_bindir}/rmt" \
  --enable-mt \
  --disable-silent-rules \
  --program-transform-name='s/^mt$/gnumt/'
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/{usr/bin,bin}
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/mt %{buildroot}%{_bindir}/mt
ln -sf %{_sysconfdir}/alternatives/mt.1%{ext_man} %{buildroot}%{_mandir}/man1/mt.1%{ext_man}
#UsrMerge
ln -sf %{_bindir}/cpio %{buildroot}/bin
#EndUsrMerge

%find_lang %{name}

%check
make %{?_smp_mflags} check

%post mt
%{_sbindir}/update-alternatives --force \
    --install %{_bindir}/mt mt %{_bindir}/gnumt 10 \
    --slave %{_mandir}/man1/mt.1%{ext_man} mt.1%{ext_man} %{_mandir}/man1/gnumt.1%{ext_man}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%postun mt
if [ ! -f %{_bindir}/gnumt ] ; then
   "%{_sbindir}/update-alternatives" --remove mt %{_bindir}/gnumt
fi

%files
%license COPYING
%doc NEWS ChangeLog
#UsrMerge
/bin/cpio
#EndUsrMerge
%{_bindir}/cpio
%{_infodir}/cpio.info%{?ext_info}
%{_mandir}/man1/cpio.1%{?ext_man}

%files mt
%ghost %{_bindir}/mt
%{_bindir}/gnumt
%ghost %{_mandir}/man1/mt.1%{ext_man}
%{_mandir}/man1/gnumt.1%{?ext_man}
%ghost %{_sysconfdir}/alternatives/mt
%ghost %{_sysconfdir}/alternatives/mt.1%{ext_man}

%files lang -f %{name}.lang

%changelog
