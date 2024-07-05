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
Version:        7.0.5
Release:        0
Summary:        Self-hostable forge
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://forgejo.org
Source0:        https://codeberg.org/%{name}/%{name}/releases/download/v%{version}/%{name}-src-%{version}.tar.gz
Source1:        https://codeberg.org/%{name}/%{name}/releases/download/v%{version}/%{name}-src-%{version}.tar.gz.asc
Source2:        http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xeb114f5e6c0dc2bcdd183550a4b61a2dc5923710#/%{name}.keyring
Source3:        package-lock.json
Source4:        node_modules.spec.inc
%include        %{_sourcedir}/node_modules.spec.inc
Source5:        %{name}.service
Source6:        %{name}.sysusers
Source7:        apparmor-usr.bin.%{name}
Source8:        %{name}.fc
Source9:        %{name}.if
Source10:       %{name}.sh
Source11:       %{name}.te
Source99:       get-sources.sh
Patch0:         custom-app.ini.patch
BuildRequires:  golang-packaging
BuildRequires:  golang(API) = 1.22
## node >= 20
%if 0%{?suse_version} == 1500
BuildRequires:  nodejs-devel-default
BuildRequires:  npm-default
%else
BuildRequires:  nodejs-packaging
%endif
BuildRequires:  local-npm-registry
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
Requires:       git-core
Requires:       git-lfs
Requires:       (%{name}-apparmor if apparmor-abstractions)
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

%description
Providing Git hosting for your project, friends, company or community? Forgejo (/for'd͡ʒe.jo/ inspired by forĝejo
– the Esperanto word for forge) has you covered with its intuitive interface, light and easy hosting and a lot of builtin functionality.

%prep
%autosetup -p1 -n %{name}-src-%{version}
local-npm-registry %{_sourcedir} install --also=dev

%build
%sysusers_generate_pre %{SOURCE6} %{name} %{name}.conf
export EXTRA_GOFLAGS="-buildmode=pie -mod=vendor"
export TAGS="bindata timetzdata sqlite sqlite_unlock_notify"
%make_build build

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}/{conf,https,mailer}
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
install -Dm0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.%{name}
%endif

%if %{with selinux}
cd %{_sourcedir}
make -f %{_datadir}/selinux/devel/Makefile %{name}.pp
install -Dm0644 %{name}.pp %{buildroot}%{_datadir}/selinux/packages/%{name}/%{name}.pp
install -Dm0644 %{name}.if %{buildroot}%{_datadir}/selinux/devel/include/distributed/%{name}.if
%endif

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

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

%changelog
