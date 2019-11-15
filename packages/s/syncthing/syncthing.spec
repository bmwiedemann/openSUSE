#
# spec file for package syncthing
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.3.1
Release:        0
Summary:        Continuous File Synchronisation
License:        MPL-2.0
Group:          Productivity/Networking/File-Sharing
Url:            https://syncthing.net/
Source:         https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-source-v%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  go >= 1.8
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
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

%description relaysrv
Syncthing requires relay servers for NAT traversal. This package
contains the necessary files for setting up a relay server, either
joined to the syncthing relay pool or private.

%prep
%setup -q -n %{name}

%build
export BUILD_USER=abuild
export BUILD_HOST=openSUSE
mkdir -p build/src/ build/vendor/
export GOPATH="$PWD/build:$PWD/build/vendor"

mkdir -p build/src/github.com/%{name}/%{name}
ls | sed '/^build$/d' | xargs cp -at build/src/github.com/%{name}/%{name}
cp -a vendor build/vendor/src

pushd build/src/github.com/%{name}/%{name}/
go run build.go -version v%{version} install all
popd

%install
install -Dpm 0755 build/src/github.com/%{name}/%{name}/bin/%{name} \
  %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 build/src/github.com/%{name}/%{name}/bin/stcli \
  %{buildroot}%{_bindir}/stcli
install -Dpm 0755 build/src/github.com/%{name}/%{name}/bin/strelaysrv \
  %{buildroot}%{_bindir}/strelaysrv
install -dm 0750 %{buildroot}/%{_localstatedir}/lib/strelaysrv
install -Dpm 0644 cmd/strelaysrv/etc/linux-systemd/strelaysrv.service \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i '/Service\]/a EnvironmentFile=-\/etc\/default/strelaysrv'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
sed -i 's,^ExecStart=.*,ExecStart=/usr/bin/strelaysrv $OPTIONS,'    \
  %{buildroot}%{_unitdir}/strelaysrv.service
install -Dpm 0644 etc/linux-systemd/system/%{name}@.service        \
  %{buildroot}%{_unitdir}/%{name}@.service
install -Dpm 0644 etc/linux-systemd/system/%{name}-resume.service  \
  %{buildroot}%{_unitdir}/%{name}-resume.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
install -Dpm 0644 etc/linux-systemd/user/%{name}.service           \
  %{buildroot}%{_userunitdir}/%{name}.service
%endif

%pre
%service_add_pre %{name}-resume.service

%pre relaysrv
%service_add_pre strelaysrv.service
getent group strelaysrv >/dev/null || /usr/sbin/groupadd -r strelaysrv
getent passwd strelaysrv >/dev/null || \
	/usr/sbin/useradd -g strelaysrv -s /bin/false -r \
	-c "User for syncthing relay server" -d /var/lib/strelaysrv strelaysrv

%post
%service_add_post %{name}-resume.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%systemd_user_post %{name}.service
%endif

%post relaysrv
%service_add_post strelaysrv.service

%preun
%service_del_preun %{name}@.service %{name}-resume.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%systemd_user_preun %{name}.service
%endif

%preun relaysrv
%service_del_preun strelaysrv.service

%postun
%service_del_postun %{name}-resume.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%systemd_user_postun %{name}.service
%endif

%postun relaysrv
%service_del_postun strelaysrv.service

%files
%license LICENSE
%doc AUTHORS CONDUCT.md CONTRIBUTING.md README.md
%{_bindir}/%{name}
%{_bindir}/stcli
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}-resume.service
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} > 120300
%{_userunitdir}/%{name}.service
%endif

%files relaysrv
%{_bindir}/strelaysrv
%{_unitdir}/strelaysrv.service
%dir %attr(750,strelaysrv,strelaysrv) %{_localstatedir}/lib/strelaysrv

%changelog
