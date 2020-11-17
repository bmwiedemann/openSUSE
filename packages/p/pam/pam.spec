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
Version:        1.4.0
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
BuildRequires:  audit-devel
BuildRequires:  bison
BuildRequires:  cracklib-devel
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  xz
Requires(post): permissions
# All login.defs variables require support from shadow side.
# Upgrade this symbol version only if new variables appear!
# Verify by shadow-login_defs-check.sh from shadow source package.
Recommends:     login_defs-support-for-pam >= 1.3.1
%if 0%{?suse_version} > 1320
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libnsl)
BuildRequires:  pkgconfig(libtirpc)
%endif
%if %{enable_selinux}
BuildRequires:  libselinux-devel
%endif
%if 0%{?suse_version} >= 1330
Requires(pre):  group(shadow)
Requires(pre):  user(root)
%endif

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

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

%build
bash ./pam-login_defs-check.sh
export CFLAGS="%{optflags} -DNDEBUG"
%configure \
	--sbindir=/sbin \
	--includedir=%{_includedir}/security \
	--docdir=%{_docdir}/pam \
	--htmldir=%{_docdir}/pam/html \
	--pdfdir=%{_docdir}/pam/pdf \
        --libdir=/%{_lib} \
	--enable-isadir=../../%{_lib}/security \
        --enable-securedir=/%{_lib}/security \
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
mkdir -p %{buildroot}/%{_lib}/security
mkdir -p %{buildroot}/sbin
mkdir -p -m 755 %{buildroot}%{_libdir}
%make_install
/sbin/ldconfig -n %{buildroot}/%{_lib}
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
rm %{buildroot}/%{_lib}/libpam.so
ln -sf ../../%{_lib}/libpam.so.%{libpam_so_version} %{buildroot}%{_libdir}/libpam.so
rm %{buildroot}/%{_lib}/libpamc.so
ln -sf ../../%{_lib}/libpamc.so.%{libpamc_so_version} %{buildroot}%{_libdir}/libpamc.so
rm %{buildroot}/%{_lib}/libpam_misc.so
ln -sf ../../%{_lib}/libpam_misc.so.%{libpam_misc_so_version} %{buildroot}%{_libdir}/libpam_misc.so
mkdir -p %{buildroot}%{_prefix}/lib/motd.d
#
# Remove crap
#
find %{buildroot} -type f -name "*.la" -delete -print
for x in pam_unix_auth pam_unix_acct pam_unix_passwd pam_unix_session; do
  ln -f %{buildroot}/%{_lib}/security/pam_unix.so %{buildroot}/%{_lib}/security/$x.so
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
# XXX Remove until whitelisted
rm %{buildroot}/%{_lib}/security/pam_faillock.so
# Install unix2_chkpwd
install -m 755 %{_builddir}/unix2_chkpwd %{buildroot}/sbin/
install -m 644 %{_sourcedir}/unix2_chkpwd.8 %{buildroot}/%{_mandir}/man8/
# Create filelist with translatins
%find_lang Linux-PAM

%verifyscript
%verify_permissions -e /sbin/unix_chkpwd
%verify_permissions -e /sbin/unix2_chkpwd

%post
/sbin/ldconfig
%set_permissions /sbin/unix_chkpwd
%set_permissions /sbin/unix2_chkpwd

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
%{_mandir}/man8/unix2_chkpwd.8%{?ext_man}
%{_mandir}/man8/unix_chkpwd.8%{?ext_man}
%{_mandir}/man8/unix_update.8%{?ext_man}
/%{_lib}/libpam.so.0
/%{_lib}/libpam.so.%{libpam_so_version}
/%{_lib}/libpamc.so.0
/%{_lib}/libpamc.so.%{libpamc_so_version}
/%{_lib}/libpam_misc.so.0
/%{_lib}/libpam_misc.so.%{libpam_misc_so_version}
%dir /%{_lib}/security
/%{_lib}/security/pam_access.so
/%{_lib}/security/pam_debug.so
/%{_lib}/security/pam_deny.so
/%{_lib}/security/pam_echo.so
/%{_lib}/security/pam_env.so
/%{_lib}/security/pam_exec.so
/%{_lib}/security/pam_faildelay.so
#/%{_lib}/security/pam_faillock.so
/%{_lib}/security/pam_filter.so
%dir /%{_lib}/security/pam_filter
/%{_lib}/security//pam_filter/upperLOWER
/%{_lib}/security/pam_ftp.so
/%{_lib}/security/pam_group.so
/%{_lib}/security/pam_issue.so
/%{_lib}/security/pam_keyinit.so
/%{_lib}/security/pam_lastlog.so
/%{_lib}/security/pam_limits.so
/%{_lib}/security/pam_listfile.so
/%{_lib}/security/pam_localuser.so
/%{_lib}/security/pam_loginuid.so
/%{_lib}/security/pam_mail.so
/%{_lib}/security/pam_mkhomedir.so
/%{_lib}/security/pam_motd.so
/%{_lib}/security/pam_namespace.so
/%{_lib}/security/pam_nologin.so
/%{_lib}/security/pam_permit.so
/%{_lib}/security/pam_pwhistory.so
/%{_lib}/security/pam_rhosts.so
/%{_lib}/security/pam_rootok.so
/%{_lib}/security/pam_securetty.so
%if %{enable_selinux}
/%{_lib}/security/pam_selinux.so
/%{_lib}/security/pam_sepermit.so
%endif
/%{_lib}/security/pam_setquota.so
/%{_lib}/security/pam_shells.so
/%{_lib}/security/pam_stress.so
/%{_lib}/security/pam_succeed_if.so
/%{_lib}/security/pam_time.so
/%{_lib}/security/pam_timestamp.so
/%{_lib}/security/pam_tty_audit.so
/%{_lib}/security/pam_umask.so
/%{_lib}/security/pam_unix.so
/%{_lib}/security/pam_unix_acct.so
/%{_lib}/security/pam_unix_auth.so
/%{_lib}/security/pam_unix_passwd.so
/%{_lib}/security/pam_unix_session.so
/%{_lib}/security/pam_usertype.so
/%{_lib}/security/pam_warn.so
/%{_lib}/security/pam_wheel.so
/%{_lib}/security/pam_xauth.so
/sbin/faillock
/sbin/mkhomedir_helper
/sbin/pam_namespace_helper
/sbin/pam_timestamp_check
%verify(not mode) %attr(4755,root,shadow) /sbin/unix_chkpwd
%verify(not mode) %attr(4755,root,shadow) /sbin/unix2_chkpwd
%attr(0700,root,root) /sbin/unix_update
%{_unitdir}/pam_namespace.service

%files extra
%defattr(-,root,root,755)
/%{_lib}/security/pam_userdb.so
%{_mandir}/man8/pam_userdb.8%{?ext_man}

%files deprecated
%defattr(-,root,root,755)
/%{_lib}/security/pam_cracklib.so
/%{_lib}/security/pam_tally2.so
/sbin/pam_tally2
%{_mandir}/man8/pam_cracklib.8%{?ext_man}
%{_mandir}/man8/pam_tally2.8%{?ext_man}

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

%changelog
