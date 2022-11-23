#
# spec file for package sudo
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


Name:           sudo
Version:        1.9.12p1
Release:        0
Summary:        Execute some commands as root
License:        ISC
Group:          System/Base
URL:            https://www.sudo.ws/
Source0:        https://www.sudo.ws/dist/%{name}-%{version}.tar.gz
Source1:        https://www.sudo.ws/dist/%{name}-%{version}.tar.gz.sig
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
BuildRequires:  libopenssl-devel
BuildRequires:  libselinux-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires(pre):  coreutils
Requires(pre):  permissions
Recommends:     sudo-plugin-python

%description
Sudo is a command that allows users to execute some commands as root.
The %{_sysconfdir}/sudoers file (edited with 'visudo') specifies which users have
access to sudo and which commands they can run. Sudo logs all its
activities to syslogd, so the system administrator can keep an eye on
things. Sudo asks for the password for initializing a check period of a
given time N (where N is defined at installation and is set to 5
minutes by default).

%package plugin-python
Summary:        Plugin API for python
Group:          System/Base
Requires:       %{name} = %{version}

%description plugin-python
This package contains the sudo plugin which allows to write sudo plugins
in python. The API closely follows the C sudo plugin API described by
sudo_plugin(5).

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
%autosetup -p1

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
    --enable-openssl \
    --with-sendmail=%{_sbindir}/sendmail \
    --with-sudoers-mode=0440 \
    --with-env-editor \
    --without-secure-path \
    --with-passprompt="[sudo] password for %%p: " \
    --with-rundir=%{_localstatedir}/lib/sudo \
    --with-sssd
%if 0%{?sle_version} < 150000
# the SLES12 way
%make_build
%else
# -B required to make every build give the same result - maybe from bad build deps in Makefiles?
%make_build -B
%endif

%install
%make_install install_uid=`id -u` install_gid=`id -g`
%if %{defined _distconfdir}
install -d -m 755 %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE3} %{buildroot}%{_pam_vendordir}/sudo
install -m 644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/sudo-i
%else
install -d -m 755 %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/sudo
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/sudo-i
%endif
rm -f %{buildroot}%{_bindir}/sudoedit
ln -sf %{_bindir}/sudo %{buildroot}%{_bindir}/sudoedit
install -d -m 755 %{buildroot}%{_sysconfdir}/openldap/schema
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

install -d %{buildroot}%{_licensedir}/%{name}
rm -fv %{buildroot}%{_docdir}/%{name}/LICENSE.md

%if %{defined _distconfdir}
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
%license LICENSE.md
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
%{_mandir}/man8/sudo_sendlog.8%{?ext_man}

%config(noreplace) %attr(0440,root,root) %{_sysconfdir}/sudoers
%attr(0750,root,root) %dir %{_sysconfdir}/sudoers.d
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sudo.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sudo_logsrvd.conf
%if %{defined _distconfdir}
%{_pam_vendordir}/sudo
%{_pam_vendordir}/sudo-i
%else
%config(noreplace) %{_sysconfdir}/pam.d/sudo
%config(noreplace) %{_sysconfdir}/pam.d/sudo-i
%endif
%attr(4755,root,root) %{_bindir}/sudo
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
%{_libexecdir}/%{name}/%{name}/sudo_intercept.so
%{_libexecdir}/%{name}/libsudo_util.so.*
%attr(0711,root,root) %dir %ghost %{_localstatedir}/lib/%{name}
%attr(0700,root,root) %dir %ghost %{_localstatedir}/lib/%{name}/ts
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/sudo.conf

%files plugin-python
%{_mandir}/man5/sudo_plugin_python.5%{?ext_man}
%{_libexecdir}/%{name}/%{name}/python_plugin.so

%files devel
%doc plugins/sample/sample_plugin.c
%{_includedir}/sudo_plugin.h
%{_mandir}/man5/sudo_plugin.5%{?ext_man}
%attr(0644,root,root) %{_libexecdir}/%{name}/libsudo_util.so
%{_libexecdir}/%{name}/sudo/*.la
%{_libexecdir}/%{name}/*.la

%files test
%{_localstatedir}/lib/tests

%changelog
