#
# spec file for package tar
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


# For correct subpackages docs installation into tar doc directory
%global _docdir_fmt %{name}
Name:           tar
Version:        1.32
Release:        0
Summary:        GNU implementation of ((t)ape (ar)chiver)
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
Url:            https://www.gnu.org/software/tar/
Source0:        https://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.bz2
Source1:        https://ftp.gnu.org/gnu/tar/%{name}-%{version}.tar.bz2.sig
# http://wwwkeys.pgp.net:11371/pks/lookup?op=get&search=0x3602B07F55D0C732
Source2:        %{name}.keyring
Patch0:         %{name}-wildcards.patch
Patch1:         %{name}-backup-spec-fix-paths.patch
Patch2:         paxutils-rtapelib_mtget.patch
# don't print warning about zero blocks
# the patch is used in Fedora and Debian
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=235820
Patch3:         %{name}-ignore_lone_zero_blocks.patch
# The next patch is disabled because it causes a regression:
#https://bugzilla.opensuse.org/show_bug.cgi?id=918487
Patch4:         %{name}-recursive--files-from.patch
Patch5:         add_readme-tests.patch
BuildRequires:  automake
BuildRequires:  libacl-devel
BuildRequires:  libselinux-devel
Requires(pre):  info
Recommends:     %{name}-lang = %{version}
Recommends:     %{name}-rmt = %{version}
Recommends:     mt
Recommends:     xz
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
Requires(postun): update-alternatives
Provides:       rmt

%description rmt
Provides remote access to files and devices for tar, cpio
and similar backup utilities

%package doc
Summary:        Documentation files for GNU tar
Group:          Documentation/Man
Requires:       %{name} = %{version}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1

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
make %{?_smp_mflags} LDFLAGS="-pie"
cd tests
make %{?_smp_mflags} genfile
mkdir bin
mv genfile bin
cd -

%check
%if !0%{?qemu_user_space_build:1}
# Checks disabled in qemu because of races happening when we emulate
# multi-threaded programs
make %{?_smp_mflags} check
%endif

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
# Alternatives system
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/rmt %{buildroot}%{_bindir}/rmt
ln -sf %{_sysconfdir}/alternatives/rmt.1%{ext_man} %{buildroot}%{_mandir}/man1/rmt.1%{ext_man}
#UsrMerge
mkdir -p %{buildroot}/bin
ln -s %{_bindir}/%{name} %{buildroot}/bin
#EndUsrMerge
%find_lang %{name}

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%post rmt
%{_sbindir}/update-alternatives --force \
    --install %{_bindir}/rmt rmt %{_bindir}/gnurmt 10 \
    --slave %{_mandir}/man1/rmt.1%{ext_man} rmt.1%{ext_man} %{_mandir}/man1/gnurmt.1%{ext_man}

%preun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%postun rmt
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
%ghost %{_sysconfdir}/alternatives/rmt
%ghost %{_sysconfdir}/alternatives/rmt.1%{ext_man}

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/README
%{_docdir}/%{name}/ABOUT-NLS
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/THANKS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/TODO
%{_infodir}/%{name}.info*

%files
%license COPYING
#UsrMerge
/bin/%{name}
#EndUsrMerge
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
