#
# spec file for package forgejo
#
# Copyright (c) 2024 SUSE LLC
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
Version:        9.0.3
Release:        0
Summary:        Self-hostable forge
License:        GPL-3.0-or-later
Group:          Development/Tools/Version Control
URL:            https://forgejo.org
Source0:        https://codeberg.org/%{name}/%{name}/releases/download/v%{version}/%{name}-src-%{version}.tar.gz
#Source1:        https://codeberg.org/%{name}/%{name}/releases/download/v%{version}/%{name}-src-%{version}.tar.gz.asc
#Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xeb114f5e6c0dc2bcdd183550a4b61a2dc5923710#/%{name}.keyring
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
Source99:       get-sources.sh
Patch0:         custom-app.ini.patch
Patch1:         dont-strip.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.23
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
Requires:       (%{name}-apparmor if apparmor-abstractions)
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
Providing Git hosting for your project, friends, company or community? Forgejo (/for'd͡ʒe.jo/ inspired by forĝejo
– the Esperanto word for forge) has you covered with its intuitive interface, light and easy hosting and a lot of builtin functionality.

%prep
%autosetup -p1 -n %{name}-src-%{version}
local-npm-registry %{_sourcedir} install --also=dev

%build
%sysusers_generate_pre %{SOURCE6} %{name} %{name}.conf
export TAGS="bindata timetzdata sqlite sqlite_unlock_notify"
export EXTRA_GOFLAGS="-buildmode=pie -mod=vendor"
%make_build build
go build ${EXTRA_GOFLAGS} -o contrib/environment-to-ini/environment-to-ini contrib/environment-to-ini/environment-to-ini.go

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}/{conf,https,mailer}
install -Dm0755 contrib/environment-to-ini/environment-to-ini %{buildroot}%{_bindir}
ln -s %{name} %{buildroot}%{_bindir}/gitea
install -d %{buildroot}%{_sharedstatedir}/%{name}/{data,https,indexers,queues,repositories}
install -d %{buildroot}%{_sysconfdir}/%{name}
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -D -m 0644 %{_builddir}/%{name}-src-%{version}/custom/conf/app.example.ini %{buildroot}%{_sysconfdir}/%{name}/conf/app.ini
install -D -m 0755 %{_builddir}/%{name}-src-%{version}/gitea %{buildroot}%{_bindir}/%{name}
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/%{name}.conf

%if %{with apparmor}
install -d %{buildroot}%{_sysconfdir}/apparmor.d
install -Dm0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.%{name}
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
%service_add_post %{name}.service

%post firewalld
%firewalld_reload

%if %{with apparmor}
%post apparmor
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.bin.%{name}
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

%check
#as of now, broken
#%%make_build test

%files
%license LICENSE
%doc README.md RELEASE-NOTES.md CONTRIBUTING.md
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
%{_bindir}/gitea
%defattr(0660,root,forgejo,770)
%{_localstatedir}/log/%{name}
%defattr(0660,forgejo,forgejo,750)
%config(noreplace) %{_sysconfdir}/%{name}/conf/app.ini
%{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_sharedstatedir}/%{name}
%{_sysusersdir}/%{name}.conf

%if %{with apparmor}
%files apparmor
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.bin.%{name}
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
