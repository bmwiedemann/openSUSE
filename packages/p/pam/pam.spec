#
# spec file for package pam
#
# Copyright (c) 2020 SUSE LLC
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


%if !0%{?usrmerged}
%define libdir /%{_lib}
%define sbindir /sbin
%define pamdir /%{_lib}/security
%else
%define libdir %{_libdir}
%define sbindir %{_sbindir}
# moving this to /usr needs fixing
# several packages short of
# https://github.com/linux-pam/linux-pam/issues/256
%define pamdir %{_libdir}/security
%endif

#
%define enable_selinux 1
%define libpam_so_version 0.85.1
%define libpam_misc_so_version 0.82.1
%define libpamc_so_version 0.82.1
%if ! %{defined _distconfdir}
  %define _distconfdir %{_sysconfdir}
  %define config_noreplace 1
%endif
Name:           pam
#
Version:        1.5.1
Release:        0
Summary:        A Security Tool that Provides Authentication for Applications
License:        GPL-2.0-or-later OR BSD-3-Clause
Group:          System/Libraries
URL:            http://www.linux-pam.org/
Source:         Linux-PAM-%{version}.tar.xz
Source1:        Linux-PAM-%{version}-docs.tar.xz
Source3:        other.pamd
Source4:        common-auth.pamd
Source5:        common-account.pamd
Source6:        common-password.pamd
Source7:        common-session.pamd
Source8:        securetty
Source9:        baselibs.conf
Source10:       unix2_chkpwd.c
Source11:       unix2_chkpwd.8
Source12:       pam-login_defs-check.sh
Patch2:         pam-limit-nproc.patch
Patch4:         pam-hostnames-in-access_conf.patch
Patch5:         pam-xauth_ownership.patch
Patch6:         pam_cracklib-removal.patch
Patch7:         pam_tally2-removal.patch
Patch8:         pam-bsc1177858-dont-free-environment-string.patch
Patch9:         pam-pam_cracklib-add-usersubstr.patch
Patch10:        pam-bsc1181443-make-nofile-unlimited-mean-nr_open.patch
Patch11:        bsc1184358-prevent-LOCAL-from-being-resolved.patch
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  cracklib-devel
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  xz
# this is only needed in the transition phase to make sure modules
# are also loaded from /lib/security as fallback
Patch99:         pam-usrmerge.diff
Requires(post): permissions
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
Recommends:     login_defs-support-for-pam >= 1.3.1
%if 0%{?suse_version} > 1320
BuildRequires:  pkgconfig(libeconf)
%endif
%if %{enable_selinux}
BuildRequires:  libselinux-devel
%endif
Requires:       pam_unix.so
Suggests:       pam_unix
%if 0%{?suse_version} >= 1330
Requires(pre):  group(shadow)
Requires(pre):  user(root)
%endif

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

%package -n pam_unix
Summary:        PAM module for standard UNIX authentication
Group:          System/Libraries
Provides:       pam_unix.so
Conflicts:      pam_unix-nis

%description -n pam_unix
This package contains the pam_unix module, which does the standard
UNIX authentication against the passwd and shadow database. This
module does not contain NIS support.

%package extra
Summary:        PAM module to authenticate against a separate database
Group:          System/Libraries
BuildRequires:  libdb-4_8-devel
BuildRequires:  pam-devel

%description extra
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains useful extra modules eg pam_userdb which is
used to verify a username/password pair against values stored in
a Berkeley DB database.

%package doc
Summary:        Documentation for Pluggable Authentication Modules
Group:          Documentation/HTML
%if 0%{?suse_version} >= 1140
BuildArch:      noarch
%endif

%description doc
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains the documentation.

%package devel
Summary:        Include Files and Libraries for PAM Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       pam = %{version}

%description devel
PAM (Pluggable Authentication Modules) is a system security tool which
allows system administrators to set authentication policy without
having to recompile programs which do authentication.

This package contains header files and static libraries used for
building both PAM-aware applications and modules for use with PAM.

%package deprecated
Summary:        Deprecated PAM Modules
Group:          System/Libraries
Provides:       pam:/%{_lib}/security/pam_cracklib.so
Provides:       pam:/%{_lib}/security/pam_tally2.so

%description deprecated
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

This package contains deprecated extra modules like pam_cracklib and
pam_tally2, which are no longer supported upstream and will be completly
removed with one of the next releases.

%prep
%setup -q -n Linux-PAM-%{version} -b 1
cp -a %{SOURCE12} .
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -R -p1
%patch7 -R -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%if 0%{?usrmerged}
%patch99 -p1
%endif

%build
bash ./pam-login_defs-check.sh
export CFLAGS="%{optflags} -DNDEBUG"
%configure \
	--includedir=%{_includedir}/security \
	--docdir=%{_docdir}/pam \
	--htmldir=%{_docdir}/pam/html \
	--pdfdir=%{_docdir}/pam/pdf \
%if !0%{?usrmerged}
	--sbindir=/sbin \
	--libdir=/%{_lib} \
%endif
	--enable-isadir=../..%{pamdir} \
	--enable-securedir=%{pamdir} \
	--enable-vendordir=%{_distconfdir} \
	--enable-tally2 --enable-cracklib
make %{?_smp_mflags}
gcc -fwhole-program -fpie -pie -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE %{optflags} -I%{_builddir}/Linux-PAM-%{version}/libpam/include %{SOURCE10} -o %{_builddir}/unix2_chkpwd -L%{_builddir}/Linux-PAM-%{version}/libpam/.libs -lpam

%check
%make_build check

%install
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
mkdir -p %{buildroot}%{_distconfdir}/pam.d
mkdir -p %{buildroot}%{_includedir}/security
mkdir -p %{buildroot}%{pamdir}
mkdir -p %{buildroot}/sbin
mkdir -p -m 755 %{buildroot}%{_libdir}
%make_install
/sbin/ldconfig -n %{buildroot}%{libdir}
# Install documentation
%make_install -C doc
# install securetty
install -m 644 %{SOURCE8} %{buildroot}%{_distconfdir}
%ifarch s390 s390x
for i in ttyS0 ttyS1 hvc0 hvc1 hvc2 hvc3 hvc4 hvc5 hvc6 hvc7 sclp_line0 ttysclp0; do
	echo "$i" >>%{buildroot}/%{_distconfdir}/securetty
done
%endif
# install /etc/security/namespace.d used by pam_namespace.so for namespace.conf iscript
install -d %{buildroot}%{_sysconfdir}/security/namespace.d
# install other.pamd and common-*.pamd
install -m 644 %{SOURCE3} %{buildroot}%{_distconfdir}/pam.d/other
install -m 644 %{SOURCE4} %{buildroot}%{_distconfdir}/pam.d/common-auth
install -m 644 %{SOURCE5} %{buildroot}%{_distconfdir}/pam.d/common-account
install -m 644 %{SOURCE6} %{buildroot}%{_distconfdir}/pam.d/common-password
install -m 644 %{SOURCE7} %{buildroot}%{_distconfdir}/pam.d/common-session
%if !0%{?usrmerged}
rm %{buildroot}/%{_lib}/libpam.so
ln -sf ../../%{_lib}/libpam.so.%{libpam_so_version} %{buildroot}%{_libdir}/libpam.so
rm %{buildroot}/%{_lib}/libpamc.so
ln -sf ../../%{_lib}/libpamc.so.%{libpamc_so_version} %{buildroot}%{_libdir}/libpamc.so
rm %{buildroot}/%{_lib}/libpam_misc.so
ln -sf ../../%{_lib}/libpam_misc.so.%{libpam_misc_so_version} %{buildroot}%{_libdir}/libpam_misc.so
%endif
mkdir -p %{buildroot}%{_prefix}/lib/motd.d
#
# Remove crap
#
find %{buildroot} -type f -name "*.la" -delete -print
for x in pam_unix_auth pam_unix_acct pam_unix_passwd pam_unix_session; do
  ln -f %{buildroot}%{pamdir}/pam_unix.so %{buildroot}%{pamdir}/$x.so
done
#
# Install READMEs of PAM modules
#
DOC=%{buildroot}%{_defaultdocdir}/pam
mkdir -p $DOC/modules
pushd modules
for i in pam_*/README; do
	cp -fpv "$i" "$DOC/modules/README.${i%/*}"
done
popd
# Install unix2_chkpwd
install -m 755 %{_builddir}/unix2_chkpwd %{buildroot}%{sbindir}
install -m 644 %{_sourcedir}/unix2_chkpwd.8 %{buildroot}/%{_mandir}/man8/
# rpm macros
mkdir -p %{buildroot}/usr/lib/rpm/macros.d
echo "%%_pamdir %pamdir" > %{buildroot}%{_prefix}/lib/rpm/macros.d/macros.pam
# Create filelist with translatins
%find_lang Linux-PAM

%verifyscript
%verify_permissions -e %{sbindir}/unix_chkpwd
%verify_permissions -e %{sbindir}/unix2_chkpwd

%post
/sbin/ldconfig
%set_permissions %{sbindir}/unix_chkpwd
%set_permissions %{sbindir}/unix2_chkpwd

%postun -p /sbin/ldconfig
%pre
for i in securetty pam.d/other pam.d/common-account pam.d/common-auth pam.d/common-password pam.d/common-session ; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc.
for i in securetty pam.d/other pam.d/common-account pam.d/common-auth pam.d/common-password pam.d/common-session ; do
  test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done

%files -f Linux-PAM.lang
%exclude %{_defaultdocdir}/pam
%dir %{_sysconfdir}/pam.d
%dir %{_distconfdir}/pam.d
%dir %{_sysconfdir}/security
%dir %{_sysconfdir}/security/limits.d
%dir %{_prefix}/lib/motd.d
%if %{defined config_noreplace}
%config(noreplace) %{_sysconfdir}/pam.d/other
%config(noreplace) %{_sysconfdir}/pam.d/common-*
%config(noreplace) %{_sysconfdir}/securetty
%else
%{_distconfdir}/pam.d/other
%{_distconfdir}/pam.d/common-*
%{_distconfdir}/securetty
%endif
%config(noreplace) %{_sysconfdir}/environment
%config(noreplace) %{_sysconfdir}/security/access.conf
%config(noreplace) %{_sysconfdir}/security/group.conf
%config(noreplace) %{_sysconfdir}/security/faillock.conf
%config(noreplace) %{_sysconfdir}/security/limits.conf
%config(noreplace) %{_sysconfdir}/security/pam_env.conf
%if %{enable_selinux}
%config(noreplace) %{_sysconfdir}/security/sepermit.conf
%endif
%config(noreplace) %{_sysconfdir}/security/time.conf
%config(noreplace) %{_sysconfdir}/security/namespace.conf
%config(noreplace) %{_sysconfdir}/security/namespace.init
%dir %{_sysconfdir}/security/namespace.d
%doc NEWS
%license COPYING
%{_mandir}/man5/environment.5%{?ext_man}
%{_mandir}/man5/*.conf.5%{?ext_man}
%{_mandir}/man5/pam.d.5%{?ext_man}
%{_mandir}/man8/PAM.8%{?ext_man}
%{_mandir}/man8/faillock.8%{?ext_man}
%{_mandir}/man8/mkhomedir_helper.8%{?ext_man}
%{_mandir}/man8/pam.8%{?ext_man}
%{_mandir}/man8/pam_access.8%{?ext_man}
%{_mandir}/man8/pam_debug.8%{?ext_man}
%{_mandir}/man8/pam_deny.8%{?ext_man}
%{_mandir}/man8/pam_echo.8%{?ext_man}
%{_mandir}/man8/pam_env.8%{?ext_man}
%{_mandir}/man8/pam_exec.8%{?ext_man}
%{_mandir}/man8/pam_faildelay.8%{?ext_man}
%{_mandir}/man8/pam_faillock.8%{?ext_man}
%{_mandir}/man8/pam_filter.8%{?ext_man}
%{_mandir}/man8/pam_ftp.8%{?ext_man}
%{_mandir}/man8/pam_group.8%{?ext_man}
%{_mandir}/man8/pam_issue.8%{?ext_man}
%{_mandir}/man8/pam_keyinit.8%{?ext_man}
%{_mandir}/man8/pam_lastlog.8%{?ext_man}
%{_mandir}/man8/pam_limits.8%{?ext_man}
%{_mandir}/man8/pam_listfile.8%{?ext_man}
%{_mandir}/man8/pam_localuser.8%{?ext_man}
%{_mandir}/man8/pam_loginuid.8%{?ext_man}
%{_mandir}/man8/pam_mail.8%{?ext_man}
%{_mandir}/man8/pam_mkhomedir.8%{?ext_man}
%{_mandir}/man8/pam_motd.8%{?ext_man}
%{_mandir}/man8/pam_namespace.8%{?ext_man}
%{_mandir}/man8/pam_namespace_helper.8%{?ext_man}
%{_mandir}/man8/pam_nologin.8%{?ext_man}
%{_mandir}/man8/pam_permit.8%{?ext_man}
%{_mandir}/man8/pam_pwhistory.8%{?ext_man}
%{_mandir}/man8/pam_rhosts.8%{?ext_man}
%{_mandir}/man8/pam_rootok.8%{?ext_man}
%{_mandir}/man8/pam_securetty.8%{?ext_man}
%{_mandir}/man8/pam_selinux.8%{?ext_man}
%{_mandir}/man8/pam_sepermit.8%{?ext_man}
%{_mandir}/man8/pam_setquota.8%{?ext_man}
%{_mandir}/man8/pam_shells.8%{?ext_man}
%{_mandir}/man8/pam_stress.8%{?ext_man}
%{_mandir}/man8/pam_succeed_if.8%{?ext_man}
%{_mandir}/man8/pam_time.8%{?ext_man}
%{_mandir}/man8/pam_timestamp.8%{?ext_man}
%{_mandir}/man8/pam_timestamp_check.8%{?ext_man}
%{_mandir}/man8/pam_tty_audit.8%{?ext_man}
%{_mandir}/man8/pam_umask.8%{?ext_man}
%{_mandir}/man8/pam_unix.8%{?ext_man}
%{_mandir}/man8/pam_usertype.8%{?ext_man}
%{_mandir}/man8/pam_warn.8%{?ext_man}
%{_mandir}/man8/pam_wheel.8%{?ext_man}
%{_mandir}/man8/pam_xauth.8%{?ext_man}
%{_mandir}/man8/pwhistory_helper.8%{?ext_man}
%{_mandir}/man8/unix2_chkpwd.8%{?ext_man}
%{_mandir}/man8/unix_chkpwd.8%{?ext_man}
%{_mandir}/man8/unix_update.8%{?ext_man}
%{libdir}/libpam.so.0
%{libdir}/libpam.so.%{libpam_so_version}
%{libdir}/libpamc.so.0
%{libdir}/libpamc.so.%{libpamc_so_version}
%{libdir}/libpam_misc.so.0
%{libdir}/libpam_misc.so.%{libpam_misc_so_version}
%dir %{pamdir}
%{pamdir}/pam_access.so
%{pamdir}/pam_debug.so
%{pamdir}/pam_deny.so
%{pamdir}/pam_echo.so
%{pamdir}/pam_env.so
%{pamdir}/pam_exec.so
%{pamdir}/pam_faildelay.so
%{pamdir}/pam_faillock.so
%{pamdir}/pam_filter.so
%dir %{pamdir}/pam_filter
%{pamdir}//pam_filter/upperLOWER
%{pamdir}/pam_ftp.so
%{pamdir}/pam_group.so
%{pamdir}/pam_issue.so
%{pamdir}/pam_keyinit.so
%{pamdir}/pam_lastlog.so
%{pamdir}/pam_limits.so
%{pamdir}/pam_listfile.so
%{pamdir}/pam_localuser.so
%{pamdir}/pam_loginuid.so
%{pamdir}/pam_mail.so
%{pamdir}/pam_mkhomedir.so
%{pamdir}/pam_motd.so
%{pamdir}/pam_namespace.so
%{pamdir}/pam_nologin.so
%{pamdir}/pam_permit.so
%{pamdir}/pam_pwhistory.so
%{pamdir}/pam_rhosts.so
%{pamdir}/pam_rootok.so
%{pamdir}/pam_securetty.so
%if %{enable_selinux}
%{pamdir}/pam_selinux.so
%{pamdir}/pam_sepermit.so
%endif
%{pamdir}/pam_setquota.so
%{pamdir}/pam_shells.so
%{pamdir}/pam_stress.so
%{pamdir}/pam_succeed_if.so
%{pamdir}/pam_time.so
%{pamdir}/pam_timestamp.so
%{pamdir}/pam_tty_audit.so
%{pamdir}/pam_umask.so
%{pamdir}/pam_usertype.so
%{pamdir}/pam_warn.so
%{pamdir}/pam_wheel.so
%{pamdir}/pam_xauth.so
%{sbindir}/faillock
%{sbindir}/mkhomedir_helper
%{sbindir}/pam_namespace_helper
%{sbindir}/pam_timestamp_check
%{sbindir}/pwhistory_helper
%verify(not mode) %attr(4755,root,shadow) %{sbindir}/unix_chkpwd
%verify(not mode) %attr(4755,root,shadow) %{sbindir}/unix2_chkpwd
%attr(0700,root,root) %{sbindir}/unix_update
%{_unitdir}/pam_namespace.service

%files -n pam_unix
%defattr(-,root,root,755)
%{pamdir}/pam_unix.so
%{pamdir}/pam_unix_acct.so
%{pamdir}/pam_unix_auth.so
%{pamdir}/pam_unix_passwd.so
%{pamdir}/pam_unix_session.so

%files extra
%defattr(-,root,root,755)
%{pamdir}/pam_userdb.so
%{_mandir}/man8/pam_userdb.8%{?ext_man}

%files deprecated
%defattr(-,root,root,755)
%{pamdir}/pam_cracklib.so
%{pamdir}/pam_tally2.so
%{sbindir}/pam_tally2

%files doc
%defattr(644,root,root,755)
%dir %{_defaultdocdir}/pam
%doc %{_defaultdocdir}/pam/html
%doc %{_defaultdocdir}/pam/modules
%doc %{_defaultdocdir}/pam/pdf
%doc %{_defaultdocdir}/pam/*.txt

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/security
%{_mandir}/man3/pam*
%{_mandir}/man3/misc_conv.3%{?ext_man}
%{_includedir}/security/*.h
%{_libdir}/libpam.so
%{_libdir}/libpamc.so
%{_libdir}/libpam_misc.so
%{_prefix}/lib/rpm/macros.d/macros.pam

%changelog
