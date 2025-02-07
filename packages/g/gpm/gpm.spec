#
# spec file for package gpm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           gpm
%define lname	libgpm2
Version:        1.20.7
Release:        0
Summary:        Console Mouse Support
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          System/Console
URL:            http://linux.schottelius.org/gpm/

Source0:        http://www.nico.schottelius.org/software/gpm/archives/gpm-%{version}.tar.lzma
Source2:        gpm.service
Source3:        sysconfig.mouse-%{name}
Source4:        README.SUSE
Source5:        baselibs.conf
Source6:        inputattach.c
Source7:        gpl-2.0.txt
Patch0:         gpm-DESTDIR.patch
Patch4:         gpm-syn_conf.patch
Patch6:         gpm-conf.patch
Patch7:         gpm-va_arg.patch
Patch9:         gpm-no_templates_for_new_multiple_mode.patch
Patch10:        gpm-ceil.patch
Patch11:        gpm-Gpm_Open.patch
Patch12:        gpm-daemon_mode.patch
Patch15:        gpm-verbosity.patch
Patch17:        gpm-log.patch
Patch18:        gpm-glibc210.patch
Patch19:        gpm-use_getdtablesize.patch
Patch20:        gpm-int_ptr_casts.patch
Patch21:        gpm-close-fds.patch
Patch23:        gpm-lib-silent.patch
Patch25:        gpm-multilib.patch
Patch26:        gpm-weak-wgetch.patch
#PATCH-FIX-UPSTREAM Pass path to gpm.h
Patch28:        gpm-dependencies.patch
#PATCH-FIX-UPSTREAM Create the symlink libgpm.so
Patch29:        gpm-do_create_symlink.patch
#PATCH-FIX-UPSTREAM Copy the current licence text from gpl-2.0+ to gpm.h
Patch30:        gpm-fix_fsf_addess.patch
#PATCH-FIX-UPSTREAM Fix missing declarations
Patch31:        decls.patch
Patch32:        gpm-fno-common.patch
BuildRequires:  bison
BuildRequires:  libtool
BuildRequires:  lzma
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  systemd-rpm-macros
Requires(pre):  %install_info_prereq
Requires(pre):  /bin/sed
Requires(pre):  %fillup_prereq
%{?systemd_requires}
Provides:       select
%ifarch ppc64
# bug437293
Obsoletes:      gpm-64bit
%endif

%description
The gpm (general purpose mouse) daemon is a mouse server for
applications running on the Linux console. It provides cut and paste
operations. If a gpm-aware program, such as mc (Midnight Commander)
or w3m (a text-based web browser), is active, they will use to gpm to
receive mouse events and do custom handling.

%package -n %lname
Summary:        Console mouse support library
License:        GPL-2.0-or-later
Group:          System/Libraries

%description -n %lname
This package provides a library that handles mouse requests and
delivers them to applications. See the description for the "gpm"
package for more information.

%package devel
Summary:        Development files for gpm (Console Mouse Support)
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Development files for the gpm (general purpose mouse) package.

%prep
%setup -q
%patch -P 0
%patch -P 4
%patch -P 6
%patch -P 7
%patch -P 9
%patch -P 10
%patch -P 11
%patch -P 12
%patch -P 15
%patch -P 17
%patch -P 18
%patch -P 19
%patch -P 20
%patch -P 21
%patch -P 23
%patch -P 25
%patch -P 26
%patch -P 28
%patch -P 29
%patch -P 30
%patch -P 31 -p1
%patch -P 32 -p1
cp %{S:2} %{S:3} %{S:4} .
cp %{S:7} COPYING

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
#export SUSE_ASNEEDED=1
NOCONFIGURE=1 ./autogen.sh
autoreconf -fi
export CFLAGS="%{optflags} -DQUIET_LIBGPM -D_REENTRANT"
%configure --disable-static \
	--sysconfdir=%{_sysconfdir}/gpm
make CC=gcc %{?_smp_mflags}
gcc %{optflags} -o inputattach %{SOURCE6}

%install
make install DESTDIR="%buildroot" ROOT=""
#
# gpm confings
install -d %{buildroot}%{_sysconfdir}/${file/conf\/gpm-/gpm\/}
for file in conf/gpm-* ; do
  install -d %{buildroot}%{_sysconfdir}/${file/conf\/gpm-/gpm\/}
  install -m 644 $file %{buildroot}%{_sysconfdir}/${file/conf\/gpm-/gpm\/}
done
#
# lisp
# an updated version is part of emacs now
#install -d %%{buildroot}/usr/share/emacs/site-lisp
#install contrib/emacs/t-mouse.el* %%{buildroot}/usr/share/emacs/site-lisp
#
# start script
install -m 755 -d %{buildroot}%{_fillupdir}
install -m 755 -d %{buildroot}/%{_unitdir}
install -m 755 -d %{buildroot}/usr/sbin
install -m 755 inputattach %{buildroot}%{_sbindir}
install -m 644 sysconfig.mouse-%{name} %{buildroot}%{_fillupdir}
install -m 644 %{S:2} %{buildroot}/%{_unitdir}/gpm.service
%if 0%{?suse_version} < 1600
ln -sf %{_sbindir}/service %{buildroot}/usr/sbin/rcgpm
%endif
# there were two variables with the same value GPM_PROTOCOL and MOUSETYPE
# in SuLi 8.2. The MOUSETYPE variable better conforms with with other
# variable names MOUSEDEVICE and XMOUSETYPE name scheme, so get rid of
# the obsolete GPM_PROTOCOL variable
if grep "^GPM_PROTOCOL=" %{_sysconfdir}/sysconfig/mouse 1>/dev/null 2>/dev/null ; then
  if grep "^MOUSETYPE=" %{_sysconfdir}/sysconfig/mouse 1>/dev/null 2>/dev/null ; then
    # comment out the obsolete MOUSETYPE variable
    perl -pi -e "s|^(MOUSETYPE=.*)$|\#\$1     \# the variable GPM_PROTOCOL was renamed to MOUSETYPE|" %%{_sysconfdir}/sysconfig/mouse
  fi
  # rename GPM_PROTOCOL to MOUSETYPE
  perl -pi -e "s|^GPM_PROTOCOL=(.*)$|\# the variable GPM_PROTOCOL was renamed to MOUSETYPE\nMOUSETYPE=\$1|" %%{_sysconfdir}/sysconfig/mouse
fi

# Do not package static library
rm -fv %{buildroot}/%{_libdir}/libgpm.a
mkdir -p %{buildroot}/run
touch %{buildroot}/run/gpm.pid

%pre
%service_add_pre gpm.service

%preun
%service_del_preun gpm.service

%post
%{fillup_only gpm}
%service_add_post gpm.service
%{fillup_only -an mouse}
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%service_del_postun gpm.service

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc README README.gpm2 README.SUSE TODO
%doc doc/Announce doc/FAQ doc/README* doc/changelog
%{_infodir}/*
%{_mandir}/*/*
%dir %config %{_sysconfdir}/gpm
%config %{_sysconfdir}/gpm/*
%{_unitdir}/gpm.service
%{_bindir}/*
%{_sbindir}/*
%{_fillupdir}/*
%ghost /run/gpm.pid

%files -n %lname
%defattr(-,root,root)
%_libdir/libgpm.so.2*

%files devel
%defattr(-,root,root)
%{_includedir}/gpm.h
%{_libdir}/libgpm.so

%changelog
