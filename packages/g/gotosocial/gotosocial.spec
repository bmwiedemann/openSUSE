#
# spec file for package gotosocial
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
Name:           gotosocial
Version:        0.18.0
Release:        0
Summary:        An ActivityPub social network server, written in Golang
License:        AGPL-3.0-only
Url:            https://docs.gotosocial.org/en/latest/
Source0:        https://github.com/superseriousbusiness/%{name}/releases/download/v%{version}/%{name}-%{version}-source-code.tar.gz#/%{name}-%{version}.tar.gz
# Generated with ./vendor_yarn.sh %{version}
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        vendor_yarn.sh
Source3:        gotosocial.sysusers
Patch0:         default-settings.patch
BuildRequires:  golang(API) = 1.23
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig(systemd)
BuildRequires:  apparmor-profiles
BuildRequires:  apparmor-rpm-macros
BuildRequires:  nodejs >= 16
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  rsync
BuildRequires:  yarn
%{?systemd_ordering}
%sysusers_requires
ExclusiveArch:  x86_64 aarch64

%description
With GoToSocial, you can keep in touch with your friends, post, read, and share
images and articles. All without being tracked or advertised to!

%prep
%autosetup -p1 -a1 -c -n %{name}-%{version}

%build
GO_BUILDTAGS="${GO_BUILDTAGS-} netgo osusergo static_build kvformat timetzdata"
GO_LDFLAGS="${GO_LDFLAGS-} -s -w -extldflags '-static' -X 'main.Version=%{version}'"
GO_GCFLAGS=${GO_GCFLAGS-}
CGO_ENABLED=0
go build -trimpath -mod=vendor -buildmode=pie \
         -tags "${GO_BUILDTAGS}" \
         -ldflags="${GO_LDFLAGS}" \
         -gcflags="${GO_GCFLAGS}" \
         ./cmd/gotosocial

export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn --offline --cwd ./web/source install
yarn --offline --cwd ./web/source ts-patch install
yarn --offline --cwd ./web/source build

%sysusers_generate_pre %{SOURCE3} %{name}

%install
install -D -m 0755 gotosocial %{buildroot}%{_sbindir}/gotosocial

install -D -m 0750 -d %{buildroot}/var/lib/%{name}/{,.cache/} %{buildroot}/etc/%{name}/
install -D -m 0755 -d %{buildroot}%{_datadir}/%{name}/ %{buildroot}%{_docdir}/%{name}/

install -D -m 0644 example/gotosocial.service   %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 example/apparmor/gotosocial  %{buildroot}/etc/apparmor.d/gotosocial
install -D -m 0644 %{SOURCE3}                   %{buildroot}%{_sysusersdir}/%{name}.conf
install    -m 0640 example/config.yaml          %{buildroot}/etc/%{name}/config.yaml
rsync -qa --chmod=u=rwX,go=rX   web/template    %{buildroot}/etc/%{name}/
rsync -qa --chmod=u=rwX,go=rX   web/assets      %{buildroot}%{_datadir}/%{name}/
rsync -qa --exclude=**/.cache   docs            %{buildroot}%{_docdir}/%{name}/

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%apparmor_reload /etc/apparmor.d/%{name}

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc *.md
%license LICENSE
%{_sbindir}/gotosocial
%{_unitdir}/%{name}.service
%config /etc/apparmor.d/gotosocial
%{_sysusersdir}/%{name}.conf
%dir                %attr(-,%{name},%{name})  /var/lib/%{name}/{,.cache/}
%config(noreplace)  %attr(-,root,%{name})     /etc/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/assets
%{_docdir}/%{name}

%changelog
