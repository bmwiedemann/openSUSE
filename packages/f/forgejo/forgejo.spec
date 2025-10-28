#
# spec file for package forgejo
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} >= 1600
%bcond_without selinux
%bcond_without apparmor
%else
# Leap & SLE 15.X
%bcond_with selinux
%bcond_without apparmor
%endif
Name:           forgejo
Version:        13.0.2
Release:        0
Summary:        Self-hostable forge
License:        GPL-3.0-or-later
Group:          Development/Tools/Version Control
URL:            https://forgejo.org
Source0:        https://codeberg.org/forgejo/forgejo/releases/download/v%{version}/forgejo-src-%{version}.tar.gz
Source1:        https://codeberg.org/forgejo/forgejo/releases/download/v%{version}/forgejo-src-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/EB114F5E6C0DC2BCDD183550A4B61A2DC5923710#/forgejo.keyring
Source3:        package-lock.json
Source4:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
Source5:        forgejo.service
Source6:        forgejo.sysusers
Source7:        forgejo.fc
Source8:        forgejo.if
Source9:        forgejo.te
Source10:       forgejo.apparmor
Source11:       forgejo.firewalld
Source12:       forgejo-abstraction.apparmor
Source13:       forgejo-hooks-abstraction.apparmor
Source99:       README.SUSE
Patch0:         custom-app.ini.patch
Patch1:         fix-CVE-2025-58190.patch
Patch2:         fix-CVE-2025-47911.patch
BuildRequires:  golang(API) >= 1.25
## node >= 20
%if 0%{?suse_version} == 1500
BuildRequires:  nodejs-devel-default
BuildRequires:  npm-default
%else
BuildRequires:  nodejs-packaging
%endif
BuildRequires:  fdupes
BuildRequires:  firewall-macros
BuildRequires:  firewalld
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires:       git-core
Requires:       git-lfs
Requires:       (forgejo-apparmor if apparmor-abstractions)
Requires:       (forgejo-firewalld if firewalld)
Requires:       (forgejo-selinux if selinux-policy-targeted)
Conflicts:      forgejo-longterm
%if %{with apparmor}
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
BuildRequires:  libapparmor-devel
%endif
%if %{with selinux}
BuildRequires:  checkpolicy
BuildRequires:  selinux-policy-devel
%endif
%{systemd_requires}
%{sysusers_requires}

%package firewalld
Summary:        Firewalld profile for %{name}
BuildArch:      noarch
Conflicts:      forgejo-longterm-firewalld

%description firewalld
This package adds a firewalld service profile to %{name}

%if %{with apparmor}
%package apparmor
Summary:        Apparmor profile for %{name}
BuildArch:      noarch
Conflicts:      forgejo-longterm-apparmor
Requires:       %{name} = %{version}-%{release}

%description apparmor
This package adds the Apparmor profile to %{name}
%endif

%if %{with selinux}
%package selinux
Summary:        Selinux support for %{name}
BuildArch:      noarch
Conflicts:      forgejo-longterm-selinux
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-targeted

%description selinux
This package adds SELinux enforcement to %{name}.
%endif

%package environment-to-ini
Summary:        Configuration params via environment variables for %{name}
Conflicts:      forgejo-longterm-environment-to-ini
Requires:       %{name} = %{version}-%{release}

%description environment-to-ini
OCI Container users can change arbitrary configuration
via environment variables with this tool

Forgejo needs to use an ini file for configuration because the running
environment that starts the OCI container may not be the same as that used
by the hooks. An ini file also gives a good default and means that
users do not have to completely provide a full environment.

%description
Providing Git hosting for your project, friends, company or community? Forgejo
(/for'd͡ʒe.jo/ inspired by forĝejo – the Esperanto word for forge) has you
covered with its intuitive interface, light and easy hosting and a lot of
builtin functionality.

%prep
%autosetup -p1 -n forgejo-src-%{version}
local-npm-registry %{_sourcedir} install --include=dev --legacy-peer-deps
cp %{SOURCE99} .

%build
%sysusers_generate_pre %{SOURCE6} forgejo forgejo.conf
export TAGS="timetzdata sqlite sqlite_unlock_notify"
export EXTRA_GOFLAGS="-buildmode=pie -mod=vendor"
STRIP=0 %make_build build
go build ${EXTRA_GOFLAGS} -o contrib/environment-to-ini/environment-to-ini contrib/environment-to-ini/environment-to-ini.go

%install
install -d -D \
  %{buildroot}%{_bindir} %{buildroot}%{_datadir}/forgejo/{conf,https,mailer}

cp -r options %{buildroot}%{_datadir}/forgejo/
cp -r public %{buildroot}%{_datadir}/forgejo/
cp -r templates %{buildroot}%{_datadir}/forgejo/

install -d -m 0750 \
  %{buildroot}%{_sharedstatedir}/forgejo/{data,https,indexers,queues,repositories} \
  %{buildroot}%{_sharedstatedir}/forgejo/data/home/.ssh \
  %{buildroot}%{_sysconfdir}/forgejo \
  %{buildroot}%{_localstatedir}/log/forgejo

install -D -m 0755 contrib/environment-to-ini/environment-to-ini %{buildroot}%{_bindir}
install -D -m 0755 %{_builddir}/forgejo-src-%{version}/gitea     %{buildroot}%{_bindir}/forgejo
ln -s forgejo %{buildroot}%{_bindir}/gitea

install -D -m 0640 %{_builddir}/forgejo-src-%{version}/custom/conf/app.example.ini %{buildroot}%{_sysconfdir}/forgejo/conf/app.ini

install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/forgejo.service
install -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/forgejo.conf

%if %{with apparmor}
install -D -d \
  %{buildroot}%{_sysconfdir}/apparmor.d/abstractions \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/forgejo-session-exec.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/forgejo-hooks.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/git.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/hooks-pre-receive.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/hooks-post-receive.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/hooks-proc-receive.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/hooks-update.d \
  %{buildroot}%{_sysconfdir}/apparmor.d/forgejo.d/forgejo.d

install -Dm0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/apparmor.d/forgejo
install -Dm0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/forgejo
install -Dm0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/forgejo-hooks
%endif

%if %{with selinux}
cd %{_sourcedir}
make -f %{_datadir}/selinux/devel/Makefile forgejo.pp
install -Dm0644 forgejo.pp %{buildroot}%{_datadir}/selinux/packages/forgejo/forgejo.pp
install -Dm0644 forgejo.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/forgejo.if
%endif

#firewalld service file
install -D -m 0644 %{SOURCE11} %{buildroot}%{_prefix}/lib/firewalld/services/forgejo.xml

%fdupes %{buildroot}

%pre -f forgejo.pre
%service_add_pre forgejo.service

%post
if [ -e %{_datadir}/forgejo/.ssh/authorized_keys ] ; then
  mv %{_datadir}/forgejo/.ssh/authorized_keys %{_sharedstatedir}/forgejo/data/home/.ssh/authorized_keys
fi
%service_add_post forgejo.service

%post firewalld
%firewalld_reload

%if %{with apparmor}
%post apparmor
%apparmor_reload %{_sysconfdir}/apparmor.d/forgejo
%endif

%if %{with selinux}
%post selinux
semodule -i %{_datadir}/selinux/packages/forgejo/forgejo.pp 2>/dev/null || :

%preun selinux
semodule -r forgejo 2>/dev/null || :
%endif

%preun
%service_del_preun forgejo.service

%postun
%service_del_postun forgejo.service

%files
%license LICENSE
%doc README.md RELEASE-NOTES.md CONTRIBUTING.md README.SUSE
%{_bindir}/forgejo
%{_bindir}/gitea
%{_datadir}/forgejo
%{_sysusersdir}/forgejo.conf
%{_unitdir}/forgejo.service
%defattr(0640,root,forgejo,750)
%config(noreplace) %{_sysconfdir}/forgejo/conf/app.ini
%dir %{_sysconfdir}/forgejo
%dir %{_sysconfdir}/forgejo/conf
%defattr(0640,forgejo,forgejo,750)
%{_localstatedir}/log/forgejo
%{_sharedstatedir}/forgejo

%if %{with apparmor}
%files apparmor
%config %{_sysconfdir}/apparmor.d/abstractions/forgejo*
%config %{_sysconfdir}/apparmor.d/forgejo
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/forgejo-hooks.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/forgejo-session-exec.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/forgejo.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/git.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-post-receive.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-pre-receive.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-proc-receive.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-update.d
%endif

%if %{with selinux}
%files selinux
%dir %{_datadir}/selinux/devel/include/distributed
%{_datadir}/selinux/devel/include/distributed/forgejo.if
%{_datadir}/selinux/packages/forgejo
%endif

%files firewalld
%{_prefix}/lib/firewalld/services/forgejo.xml

%files environment-to-ini
%{_bindir}/environment-to-ini

%changelog
