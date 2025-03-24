#
# spec file for package forgejo
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


%if 0%{?suse_version} > 1600
%bcond_without selinux
%bcond_without apparmor
%else
%if 0%{?suse_version} == 1600
%bcond_without selinux
%bcond_with apparmor
%else
# Leap & SLE
%bcond_with selinux
%bcond_without apparmor
%endif
%endif
Name:           forgejo
Version:        10.0.3
Release:        0
Summary:        Self-hostable forge
License:        GPL-3.0-or-later
Group:          Development/Tools/Version Control
URL:            https://forgejo.org
Source0:        https://codeberg.org/%{name}/%{name}/releases/download/v%{version}/%{name}-src-%{version}.tar.gz
Source1:        https://codeberg.org/%{name}/%{name}/releases/download/v%{version}/%{name}-src-%{version}.tar.gz.asc
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/EB114F5E6C0DC2BCDD183550A4B61A2DC5923710#/%{name}.keyring
Source3:        package-lock.json
Source4:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
Source5:        %{name}.service
Source6:        %{name}.sysusers
Source7:        %{name}.fc
Source8:        %{name}.if
Source9:        %{name}.te
Source10:       %{name}.apparmor
Source11:       %{name}.firewalld
Source12:       forgejo-abstraction.apparmor
Source13:       forgejo-hooks-abstraction.apparmor
# updated vendored go modules, for fix-CVE-2025-22869.patch
Source14:       vendor.tar.gz
Source98:       README.SUSE
Source99:       get-sources.sh
Patch0:         custom-app.ini.patch
Patch1:         dont-strip.patch
Patch2:         fix-CVE-2025-22869.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.23.6
## node >= 20
%if 0%{?suse_version} == 1500
BuildRequires:  nodejs-devel-default
BuildRequires:  npm-default
%else
BuildRequires:  nodejs-packaging
%endif
BuildRequires:  firewall-macros
BuildRequires:  firewalld
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires:       git-core
Requires:       git-lfs
Recommends:     (%{name}-apparmor if apparmor-abstractions)
Requires:       (%{name}-firewalld if firewalld)
Requires:       (%{name}-selinux if selinux-policy-targeted)
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

%description firewalld
This package adds a firewalld service profile to %{name}

%if %{with apparmor}
%package apparmor
Summary:        Apparmor profile for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description apparmor
This package adds the Apparmor profile to %{name}
%endif

%if %{with selinux}
%package selinux
Summary:        Selinux support for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       selinux-policy-targeted

%description selinux
This package adds SELinux enforcement to %{name}.
%endif

%package environment-to-ini
Summary:        Configuration params via environment variables for %{name}
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
%autosetup -p1 -n %{name}-src-%{version}
tar xf %{SOURCE14} -C %{_builddir}/%{name}-src-%{version}/
local-npm-registry %{_sourcedir} install --also=dev --legacy-peer-deps
cp %{SOURCE98} .

%build
%sysusers_generate_pre %{SOURCE6} %{name} %{name}.conf
export TAGS="bindata timetzdata sqlite sqlite_unlock_notify"
export EXTRA_GOFLAGS="-buildmode=pie -mod=vendor"
%make_build build
go build ${EXTRA_GOFLAGS} -o contrib/environment-to-ini/environment-to-ini contrib/environment-to-ini/environment-to-ini.go

%install
install -d -D \
  %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/{conf,https,mailer}

install -d -m 0750 \
  %{buildroot}%{_sharedstatedir}/%{name}/{data,https,indexers,queues,repositories} \
  %{buildroot}%{_sharedstatedir}/%{name}/data/home/.ssh \
  %{buildroot}%{_sysconfdir}/%{name} \
  %{buildroot}%{_localstatedir}/log/%{name}

install -D -m 0755 contrib/environment-to-ini/environment-to-ini %{buildroot}%{_bindir}
install -D -m 0755 %{_builddir}/%{name}-src-%{version}/gitea     %{buildroot}%{_bindir}/%{name}
ln -s %{name} %{buildroot}%{_bindir}/gitea

install -D -m 0640 %{_builddir}/%{name}-src-%{version}/custom/conf/app.example.ini %{buildroot}%{_sysconfdir}/%{name}/conf/app.ini

install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/%{name}.conf

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

install -Dm0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/apparmor.d/%{name}
install -Dm0644 %{SOURCE12} %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/%{name}
install -Dm0644 %{SOURCE13} %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/%{name}-hooks
%endif

%if %{with selinux}
cd %{_sourcedir}
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
install -Dm0644 %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/%{name}.pp
install -Dm0644 %{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif

#firewalld service file
install -D -m 0644 %{SOURCE11} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
if [ -e %{_datadir}/%{name}/.ssh/authorized_keys ] ; then
  mv %{_datadir}/%{name}/.ssh/authorized_keys %{_sharedstatedir}/%{name}/data/home/.ssh/authorized_keys
fi
%service_add_post %{name}.service

%post firewalld
%firewalld_reload

%if %{with apparmor}
%post apparmor
%apparmor_reload %{_sysconfdir}/apparmor.d/%{name}
%endif

%if %{with selinux}
%post selinux
semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp 2>/dev/null || :

%preun selinux
semodule -r %{name} 2>/dev/null || :
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md RELEASE-NOTES.md CONTRIBUTING.md README.SUSE
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
%{_bindir}/gitea
%{_sysusersdir}/%{name}.conf
%{_datadir}/%{name}
%defattr(0640,root,forgejo,750)
%{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/conf/app.ini
%defattr(0640,forgejo,forgejo,750)
%{_localstatedir}/log/%{name}
%{_sharedstatedir}/%{name}

%if %{with apparmor}
%files apparmor
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/%{name}
%config %{_sysconfdir}/apparmor.d/abstractions/%{name}*
%dir %{_sysconfdir}/apparmor.d/forgejo.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/forgejo.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/forgejo-session-exec.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/forgejo-hooks.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/git.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-pre-receive.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-post-receive.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-proc-receive.d
%dir %{_sysconfdir}/apparmor.d/forgejo.d/hooks-update.d
%endif

%if %{with selinux}
%files selinux
%dir %{_datadir}/selinux/devel/include/distributed
%{_datadir}/selinux/packages/%{name}
%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif

%files firewalld
%{_prefix}/lib/firewalld/services/%{name}.xml

%files environment-to-ini
%{_bindir}/environment-to-ini

%changelog
