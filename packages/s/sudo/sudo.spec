#
# spec file for package sudo
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


%if ! %{defined _distconfdir}
%define _distconfdir %{_sysconfdir}
%else
%define use_usretc 1
%endif
Name:           sudo
Version:        1.9.0rc4
Release:        0
Summary:        Execute some commands as root
License:        ISC
Group:          System/Base
URL:            https://www.sudo.ws/
Source0:        https://www.sudo.ws/dist/beta/%{name}-%{version}.tar.gz
Source1:        https://www.sudo.ws/dist/beta/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        sudo.pamd
Source4:        sudo-i.pamd
Source5:        README.SUSE
Source6:        fate_313276_test.sh
Source7:        README_313276.test
# PATCH-OPENSUSE: the "SUSE" branding of the default sudo config
Patch0:         sudo-sudoers.patch
BuildRequires:  audit-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  groff
BuildRequires:  libselinux-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires(pre):  coreutils
Requires(pre):  permissions

%description
Sudo is a command that allows users to execute some commands as root.
The %{_sysconfdir}/sudoers file (edited with 'visudo') specifies which users have
access to sudo and which commands they can run. Sudo logs all its
activities to syslogd, so the system administrator can keep an eye on
things. Sudo asks for the password for initializing a check period of a
given time N (where N is defined at installation and is set to 5
minutes by default).

%package devel
Summary:        Header files needed for sudo plugin development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
These header files are needed for building of sudo plugins.

%package test
Summary:        Tests for the package
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description test
Tests for fate#313276

%prep
%setup -q
%patch0 -p1

%build
%ifarch s390 s390x %{sparc}
F_PIE=-fPIE
%else
F_PIE=-fpie
%endif
export CFLAGS="%{optflags} -Wall $F_PIE -DLDAP_DEPRECATED"
export LDFLAGS="-pie"
%configure \
    --libexecdir=%{_libexecdir}/sudo \
    --docdir=%{_docdir}/%{name} \
    --with-noexec=%{_libexecdir}/sudo/sudo_noexec.so \
    --enable-tmpfiles.d=%{_tmpfilesdir} \
    --with-pam \
    --with-pam-login \
    --with-ldap \
    --with-selinux \
    --with-linux-audit \
    --with-logfac=auth \
    --with-all-insults \
    --with-ignore-dot \
    --with-tty-tickets \
    --enable-shell-sets-home \
    --enable-warnings \
    --enable-python \
    --with-sendmail=%{_sbindir}/sendmail \
    --with-sudoers-mode=0440 \
    --with-env-editor \
    --without-secure-path \
    --with-passprompt="[sudo] password for %%p: " \
    --with-rundir=%{_localstatedir}/lib/sudo \
    --with-sssd
# -B required to make every build give the same result - maybe from bad build deps in Makefiles?
%make_build -B

%install
%make_install install_uid=`id -u` install_gid=`id -g`
install -d -m 755 %{buildroot}%{_distconfdir}/pam.d
install -m 644 %{SOURCE3} %{buildroot}%{_distconfdir}/pam.d/sudo
install -m 644 %{SOURCE4} %{buildroot}%{_distconfdir}/pam.d/sudo-i
rm -f %{buildroot}%{_bindir}/sudoedit
ln -sf %{_bindir}/sudo %{buildroot}%{_bindir}/sudoedit
install -d -m 755 %{buildroot}%{_sysconfdir}/openldap/schema
install -m 644 doc/schema.OpenLDAP %{buildroot}%{_sysconfdir}/openldap/schema/sudo.schema
install -m 644 %{SOURCE5} %{buildroot}%{_docdir}/%{name}/
rm -f %{buildroot}%{_docdir}/%{name}/sample.pam
rm -f %{buildroot}%{_docdir}/%{name}/sample.syslog.conf
rm -f %{buildroot}%{_docdir}/%{name}/schema.OpenLDAP
rm -f %{buildroot}%{_sysconfdir}/sudoers.dist

%find_lang %{name}
%find_lang sudoers
cat sudoers.lang >> %{name}.lang
# tests
install -d -m 755 %{buildroot}%{_localstatedir}/lib/tests/sudo
install -m 755 %{SOURCE6} %{buildroot}%{_localstatedir}/lib/tests/sudo
install -m 755 %{SOURCE7} %{buildroot}%{_localstatedir}/lib/tests/sudo
install -d %{buildroot}%{_docdir}/%{name}-test
install -m 644 %{buildroot}%{_docdir}/%{name}/LICENSE %{buildroot}%{_docdir}/%{name}-test/LICENSE
rm -fv %{buildroot}%{_docdir}/%{name}/LICENSE

%if %{defined use_usretc}
%pre
# move outdated pam.d/*.rpmsave files away
for i in sudo sudo-i ; do
    test -f %{_sysconfdir}/pam.d/${i}.rpmsave && mv -v %{_sysconfdir}/pam.d/${i}.rpmsave %{_sysconfdir}/pam.d/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc.
for i in  sudo sudo-i ; do
  test -f %{_sysconfdir}/pam.d/${i}.rpmsave && mv -v %{_sysconfdir}/pam.d/${i}.rpmsave %{_sysconfdir}/pam.d/${i} ||:
done
%endif

%post
chmod 0440 %{_sysconfdir}/sudoers
%if 0%{?suse_version} <= 1130
%run_permissions
%else
%set_permissions %{_bindir}/sudo
%endif
%tmpfiles_create %{_tmpfilesdir}/sudo.conf

%verifyscript
%verify_permissions -e %{_bindir}/sudo

%files -f %{name}.lang
%license doc/LICENSE
%doc %{_docdir}/%{name}
%{_mandir}/man1/cvtsudoers.1%{?ext_man}
%{_mandir}/man5/sudoers.5%{?ext_man}
%{_mandir}/man5/sudo.conf.5%{?ext_man}
%{_mandir}/man5/sudoers.ldap.5%{?ext_man}
%{_mandir}/man5/sudoers_timestamp.5%{?ext_man}
%{_mandir}/man8/sudo.8%{?ext_man}
%{_mandir}/man8/sudoedit.8%{?ext_man}
%{_mandir}/man8/sudoreplay.8%{?ext_man}
%{_mandir}/man8/visudo.8%{?ext_man}
%{_mandir}/man5/sudo_logsrv.proto.5%{?ext_man}
%{_mandir}/man5/sudo_logsrvd.conf.5%{?ext_man}
%{_mandir}/man8/sudo_logsrvd.8%{?ext_man}
%{_mandir}/man8/sudo_plugin_python.8%{?ext_man}
%{_mandir}/man8/sudo_sendlog.8%{?ext_man}

%config(noreplace) %attr(0440,root,root) %{_sysconfdir}/sudoers
%dir %{_sysconfdir}/sudoers.d
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sudo.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sudo_logsrvd.conf
%if %{defined use_usretc}
%{_distconfdir}/pam.d/sudo
%{_distconfdir}/pam.d/sudo-i
%else
%config(noreplace) %{_sysconfdir}/pam.d/sudo
%config(noreplace) %{_sysconfdir}/pam.d/sudo-i
%endif
%attr(4755,root,root) %{_bindir}/sudo
%dir %{_sysconfdir}/openldap
%dir %{_sysconfdir}/openldap/schema
%attr(0444,root,root) %config %{_sysconfdir}/openldap/schema/sudo.schema
%{_bindir}/sudoedit
%{_bindir}/sudoreplay
%{_bindir}/cvtsudoers
%{_sbindir}/visudo
%{_sbindir}/sudo_logsrvd
%{_sbindir}/sudo_sendlog
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/sesh
%{_libexecdir}/%{name}/sudo_noexec.so
%dir %{_libexecdir}/%{name}/%{name}
%{_libexecdir}/%{name}/%{name}/sudoers.so
%{_libexecdir}/%{name}/%{name}/group_file.so
%{_libexecdir}/%{name}/%{name}/system_group.so
%{_libexecdir}/%{name}/%{name}/audit_json.so
%{_libexecdir}/%{name}/%{name}/sample_approval.so
%{_libexecdir}/%{name}/%{name}/python_plugin.so
%{_libexecdir}/%{name}/libsudo_util.so.*
%attr(0711,root,root) %dir %ghost %{_localstatedir}/lib/%{name}
%attr(0700,root,root) %dir %ghost %{_localstatedir}/lib/%{name}/ts
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/sudo.conf

%files devel
%doc plugins/sample/sample_plugin.c
%{_includedir}/sudo_plugin.h
%{_mandir}/man8/sudo_plugin.8%{?ext_man}
%attr(0644,root,root) %{_libexecdir}/%{name}/libsudo_util.so
%{_libexecdir}/%{name}/sudo/*.la
%{_libexecdir}/%{name}/*.la

%files test
%{_localstatedir}/lib/tests
%{_docdir}/%{name}-test/

%changelog
