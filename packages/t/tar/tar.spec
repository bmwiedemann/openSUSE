#
# spec file for package tar
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


# For correct subpackages docs installation into tar doc directory
%global _docdir_fmt %{name}
Name:           tar
Version:        1.35
Release:        0
Summary:        GNU implementation of ((t)ape (ar)chiver)
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://www.gnu.org/software/tar/
Source0:        https://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.xz.sig
# http://wwwkeys.pgp.net:11371/pks/lookup?op=get&search=0x3602B07F55D0C732
Source2:        %{name}.keyring
Source3:        pax-global-records.tar
Patch0:         %{name}-wildcards.patch
Patch1:         %{name}-backup-spec-fix-paths.patch
Patch2:         paxutils-rtapelib_mtget.patch
# don't print warning about zero blocks
# the patch is used in Fedora and Debian
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=235820
Patch3:         %{name}-ignore_lone_zero_blocks.patch
Patch5:         add_readme-tests.patch
Patch6:         tar-PIE.patch
Patch7:         tests-skip-time01-on-32bit-time_t.patch
Patch11:        tar-fix-extract-unlink.patch
# PATCH-FIX-SUSE danilo.spinella@suse.com bsc#1202436
Patch12:        go-testsuite-test-hang.patch
# PATCH-FIX-UPSTREAM danilo.spinella@suse.com bsc#1202436
Patch13:        bsc1202436.patch
# PATCH-FIX-UPSTREAM danilo.spinella@suse.com bsc#1207753
# tar has a one-byte out-of-bounds read that results in use of
# uninitialized memory for a conditional jump
Patch16:        fix-CVE-2022-48303.patch
Patch17:        add_forgotten-tests.patch
BuildRequires:  automake >= 1.15
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
Recommends:     %{name}-rmt = %{version}
Recommends:     mt
Recommends:     xz
Recommends:     zstd
Provides:       base:/bin/tar

%description
GNU Tar is an archiver program. It is used to create and manipulate files
that are actually collections of many other files; the program provides
users with an organized and systematic method of controlling a large amount
of data. Despite its name, that is an acronym of "tape archiver", GNU Tar
is able to direct its output to any available devices, files or other programs,
it may as well access remote devices or files.

%package backup-scripts
Summary:        Backup scripts
Group:          Productivity/Archiving/Backup
Requires:       %{name} = %{version}
BuildArch:      noarch

%description backup-scripts
Shell scripts for system backup/restore

%package tests
Summary:        Tests for the package
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description tests
Upstream testsuite for the package

%package rmt
Summary:        Remote tape drive control server by GNU
Group:          Productivity/Archiving/Backup
Requires(post): update-alternatives
Provides:       rmt
Conflicts:      rmt

%description rmt
Provides remote access to files and devices for tar, cpio
and similar backup utilities

%package doc
Summary:        Documentation files for GNU tar
Group:          Documentation/Man
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
GNU Tar is an archiver program. It is used to create and manipulate files
that are actually collections of many other files; the program provides
users with an organized and systematic method of controlling a large amount
of data. Despite its name, that is an acronym of "tape archiver", GNU Tar
is able to direct its output to any available devices, files or other programs,
it may as well access remote devices or files.

%lang_package

%prep
%autosetup -p1
cp %{S:3} tests

%build
%define my_cflags -W -Wall -Wpointer-arith -Wstrict-prototypes -Wformat-security -Wno-unused-parameter -fPIE
export CFLAGS="%{optflags} %{my_cflags}"
export RSH=%{_bindir}/ssh
export DEFAULT_ARCHIVE_FORMAT="POSIX"
export DEFAULT_RMT_DIR=%{_bindir}
autoreconf -fi
%configure \
	gl_cv_func_linkat_follow="yes" \
	--enable-backup-scripts \
	--disable-silent-rules \
	--program-transform-name='s/^rmt$/gnurmt/'
%make_build LDFLAGS="-pie"
cd tests
%make_build genfile
mkdir bin
mv genfile bin
cd -

%check
%make_build check || { cat tests/testsuite.log; exit 1; }

%install
%make_install DESTDIR=%{buildroot}
mkdir %{buildroot}/bin
mv %{buildroot}%{_mandir}/man8/gnurmt.8 %{buildroot}%{_mandir}/man1/gnurmt.1
install -D -m 644 scripts/backup-specs %{buildroot}%{_sysconfdir}/backup/backup-specs
# For avoiding file conflicts with dump/restore
mv %{buildroot}%{_sbindir}/restore %{buildroot}%{_sbindir}/restore.sh
rm -f %{buildroot}%{_infodir}/dir
install -D -m 644 -t %{buildroot}%{_docdir}/%{name} README* ABOUT-NLS AUTHORS NEWS THANKS \
							ChangeLog TODO
install -d -m 755 %{buildroot}%{_localstatedir}/lib/tests
cp -r tests %{buildroot}%{_localstatedir}/lib/tests/tar
rm %{buildroot}%{_localstatedir}/lib/tests/tar/*.{c,h,o}
rm %{buildroot}%{_localstatedir}/lib/tests/tar/package.m4
rm %{buildroot}%{_localstatedir}/lib/tests/tar/{atconfig,atlocal,Makefile}*
%if 0%{?suse_version} < 1550
mkdir -p %{buildroot}/bin
ln -s %{_bindir}/%{name} %{buildroot}/bin
%endif
%find_lang %{name}

%post rmt
if [ ! -f %{_bindir}/gnurmt ] ; then
   "%{_sbindir}/update-alternatives" --remove rmt %{_bindir}/gnurmt
fi

%files backup-scripts
%{_sbindir}/backup
%{_sbindir}/restore.sh
%{_libexecdir}/backup.sh
%{_libexecdir}/dump-remind
%dir %{_sysconfdir}/backup
%config(noreplace) %{_sysconfdir}/backup/backup-specs

%files lang -f %{name}.lang

%files tests
%{_localstatedir}/lib/tests
%{_docdir}/%{name}/README-tests

%files rmt
%ghost %{_bindir}/rmt
%{_bindir}/gnurmt
%ghost %{_mandir}/man1/rmt.1%{ext_man}
%{_mandir}/man1/gnurmt.1%{?ext_man}

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README
%{_docdir}/%{name}/ABOUT-NLS
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/THANKS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/TODO
%{_infodir}/%{name}.info*%{?ext_info}

%files
%license COPYING
%if 0%{?suse_version} < 1550
/bin/%{name}
%endif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
