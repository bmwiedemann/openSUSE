#
# spec file for package syncthing
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


Name:           syncthing
Version:        1.30.0
Release:        0
Summary:        Continuous File Synchronisation
License:        MPL-2.0
Group:          Productivity/Networking/File-Sharing
URL:            https://syncthing.net/
Source:         https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz
# signature can not be validated at the moment, see changelog entry from "Jan 16 11:32:55 UTC 2025" and https://github.com/syncthing/syncthing/issues/9902
#Source1:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{name}-relaysrv-user.conf
Patch0:         harden_strelaysrv.service.patch
Patch1:         harden_syncthing@.service.patch
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  update-desktop-files
BuildRequires:  golang(API) >= 1.14
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}

%description
Syncthing is an application that synchronises files across multiple
devices. This means the creation, modification or deletion of files
on one machine will automatically be replicated to other devices.

%package relaysrv
Summary:        Relay server for syncthing
Group:          Productivity/Networking/File-Sharing
Requires(pre):  pwdutils
%{?systemd_ordering}
%sysusers_requires

%description relaysrv
Syncthing requires relay servers for NAT traversal. This package
contains the necessary files for setting up a relay server, either
joined to the syncthing relay pool or private.

%prep
%autosetup -n %{name} -p1

%build
# move source archive which is extracted as "syncthing" to be "src/github.com/syncthing/syncthing"
pushd ..
install -d "src/github.com/syncthing/"
mv %{name} "src/github.com/syncthing/"%{name}
mkdir syncthing
cd "$PWD/src/github.com/syncthing/"%{name}

# set build environment, in particular use "-mod=vendor" to use the Go modules from the source archive's vendor dir
export BUILD_USER=abuild BUILD_HOST=openSUSE
export CGO_CPPFLAGS="${CPPFLAGS}" CGO_CFLAGS="${CFLAGS}" CGO_CXXFLAGS="${CXXFLAGS}" CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-trimpath -mod=vendor"

# build and install syncthing without automatic updates
go run build.go -no-upgrade -version v%{version} install
# build and install strelaysrv without automatic updates
go run build.go -no-upgrade -version v%{version} install strelaysrv
popd

%sysusers_generate_pre %{SOURCE3} %{name}-strelaysrv %{name}-strelaysrv-user.conf

%install
st_dir=$PWD
cd ../src/github.com/syncthing/%{name}
mv LICENSE AUTHORS CONDUCT.md CONTRIBUTING.md README.md "$st_dir"
install -Dpm 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 bin/strelaysrv %{buildroot}%{_bindir}/strelaysrv
install -dm 0750 %{buildroot}/%{_localstatedir}/lib/syncthing-relaysrv
install -Dpm 0644 cmd/strelaysrv/etc/linux-systemd/strelaysrv.service \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i '/Service\]/a EnvironmentFile=-\/etc\/default/strelaysrv'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i 's,^ExecStart=.*,ExecStart=/usr/bin/strelaysrv $OPTIONS,'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i 's,EnvironmentFile=/etc/default/syncthing-relaysrv,EnvironmentFile=-/etc/default/syncthing-relaysrv,'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i 's/^User=.*/User=strelaysrv/'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i 's/^Group=.*/Group=strelaysrv/'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i 's,^ReadWritePaths=.*,ReadWritePaths=/var/lib/syncthing-relaysrv,'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
install -Dpm 0644 etc/linux-systemd/system/%{name}@.service        \
  %{buildroot}%{_unitdir}/%{name}@.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
install -Dpm 0644 etc/linux-systemd/user/%{name}.service           \
  %{buildroot}%{_userunitdir}/%{name}.service
%endif
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}-relaysrv.conf

%suse_update_desktop_file -i "syncthing-ui"

%pre

%pre relaysrv -f %{name}-strelaysrv.pre
%service_add_pre strelaysrv.service

%post
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%systemd_user_post %{name}.service
%endif

%post relaysrv
%service_add_post strelaysrv.service

%preun
%service_del_preun %{name}@.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%systemd_user_preun %{name}.service
%endif

%preun relaysrv
%service_del_preun strelaysrv.service

%postun
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%systemd_user_postun %{name}.service
%endif

%postun relaysrv
%service_del_postun strelaysrv.service

%files
%license LICENSE
%doc AUTHORS CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_datadir}/applications/syncthing-ui.desktop
%{_unitdir}/%{name}@.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%{_userunitdir}/%{name}.service
%endif

%files relaysrv
%license LICENSE
%{_bindir}/strelaysrv
%{_unitdir}/strelaysrv.service
%dir %attr(750,strelaysrv,strelaysrv) %{_localstatedir}/lib/syncthing-relaysrv
%{_sysusersdir}/%{name}-relaysrv.conf

%changelog
