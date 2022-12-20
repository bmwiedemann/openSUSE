#
# spec file for package screen
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


%if 0%{?suse_version} > 1310
%define rundir /run
%else
%define rundir %{_localstatedir}/run
%endif
Name:           screen
Version:        4.9.0
Release:        0
Summary:        A program to allow multiple screens on a VT100/ANSI Terminal
License:        GPL-3.0-or-later
Group:          System/Console
URL:            https://www.gnu.org/software/screen/
Source:         https://ftp.gnu.org/gnu/screen/%{name}-%{version}.tar.gz
Source1:        screen.conf
Source2:        https://ftp.gnu.org/gnu/screen/%{name}-%{version}.tar.gz.sig
Source3:        https://savannah.gnu.org/people/viewgpg.php?user_id=99366#/%{name}.keyring
Source4:        screen.pam
Patch0:         global_screenrc.patch
Patch6:         libtinfo.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  utempter-devel
Requires:       terminfo-base
Requires(post): permissions
%systemd_ordering

%description
With this program you can take advantage of the multitasking abilities
of your Linux system by opening several sessions over one terminal. The
sessions can also be detached and resumed from another login terminal.

Documentation: man page

%prep
%setup -q
# global_screenrc.patch
%patch0
# libtinfo.diff
%patch6

%build
sh ./autogen.sh

CFLAGS="-DMAXWIN=1000 %{optflags}" %configure --prefix=%{_prefix} --infodir=%{_infodir} \
				--mandir=%{_mandir} \
				--with-socket-dir='(eff_uid ? "%{rundir}/uscreens" : "%{rundir}/screens")' \
				--with-sys-screenrc=%{_sysconfdir}/screenrc \
				--with-pty-group=5 \
				--enable-use-locale \
				--enable-telnet \
				--enable-pam \
				--enable-colors256 \
				--verbose

# update Makefile so that make -j becomes reliable
:> osdef.h	# so that make depend has a chance
:> comm.h	# so that make depend has a chance
%make_build depend	# FIXME: this should be self sufficient.
rm osdef.h	# so that make will use osdef.sh
rm comm.h	# so that make will use comm.sh

%make_build

%install
%make_install
rm -f %{buildroot}%{_bindir}/screen
mv %{buildroot}%{_bindir}/screen-%{version} %{buildroot}%{_bindir}/screen
chmod 755 %{buildroot}%{_bindir}/screen
mkdir -p %{buildroot}%{_sysconfdir}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
%else
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
%endif
mkdir -p %{buildroot}%{_prefix}/lib
mkdir -p %{buildroot}%{_tmpfilesdir}
mkdir -p %{buildroot}%{rundir}/screens
chmod 755 %{buildroot}%{rundir}/screens
mkdir -p %{buildroot}%{rundir}/uscreens
install -m 644 screenrc %{buildroot}%{_sysconfdir}/screenrc
install -m 644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}
%if 0%{?suse_version} > 1500
install -m 644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/screen
%else
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/screen
%endif

%files
%config %{_sysconfdir}/screenrc
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/screen
%else
%config %{_sysconfdir}/pam.d/screen
%endif
%attr(555,root,root) %{_bindir}/screen
%dir %{_datadir}/screen
%{_tmpfilesdir}/screen.conf
%{_datadir}/screen/utf8encodings
%{_infodir}/screen.info*%{ext_info}
%{_mandir}/man1/screen.1%{?ext_man}
%license COPYING

%if 0%{?suse_version} > 1500
%pre
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/screen ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/screen ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%tmpfiles_create %{_tmpfilesdir}/screen.conf

%changelog
