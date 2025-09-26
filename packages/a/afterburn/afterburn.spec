#
# spec file for package afterburn
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


%global rustflags -Clink-arg=-Wl,-z,relro,-z,now

%global dracutmodulesdir %(pkg-config --variable=dracutmodulesdir dracut || echo '/usr/lib/dracut/modules.d')

Name:           afterburn
Version:        5.9.0.git21.a73f509
Release:        0
Summary:        A cloud provider agent
License:        Apache-2.0
URL:            https://coreos.github.io/afterburn/
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Patch0:         0001-Fix-authorized-keys-location-for-OpenSUSE.patch
Patch1:         0002-Set-the-default-user-to-suse.patch
Patch2:         0003-On-OpenSUSE-do-not-add-to-kernel-command-line.patch


BuildRequires:  cargo
BuildRequires:  rust >= 1.84.1
BuildRequires:  pkgconfig(openssl)

%description
Afterburn is a one-shot agent for cloud-like platforms which interacts with provider-specific metadata endpoints.

%package dracut
Summary:        Dracut modules for afterburn
BuildRequires:  pkgconfig(dracut)
Requires:       %{name} = %{?epoch:}%{version}-%{release}
Requires:       dracut
BuildArch:      noarch

%description dracut
Dracut module that enables afterburn and corresponding services
to run in the initramfs on boot.

%prep
%autosetup -p1 -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config
# Remove exec bits to prevent an issue in fedora shebang checking
find vendor -type f -name \*.rs -exec chmod -x '{}' +

%build
export RUSTFLAGS="%{rustflags}"
cargo build --offline --release

%check
export RUSTFLAGS="%{rustflags}"
cargo test --offline --release

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/cmdline.d

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 %{_builddir}/%{name}-%{version}/systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -m 0644 %{_builddir}/%{name}-%{version}/systemd/%{name}-checkin.service %{buildroot}%{_unitdir}/%{name}-checkin.service
install -m 0644 %{_builddir}/%{name}-%{version}/systemd/%{name}-firstboot-checkin.service %{buildroot}%{_unitdir}/%{name}-firstboot-checkin.service
install -m 0644 %{_builddir}/%{name}-%{version}/systemd/%{name}-sshkeys.target %{buildroot}%{_unitdir}/%{name}-sshkeys.target
sed -e 's,@DEFAULT_INSTANCE@,'suse',' < systemd/%{name}-sshkeys@.service.in > systemd/%{name}-sshkeys@.service.tmp
mv systemd/%{name}-sshkeys@.service.tmp systemd/%{name}-sshkeys@.service
install -m 0644 %{_builddir}/%{name}-%{version}/systemd/%{name}-sshkeys@.service %{buildroot}%{_unitdir}/%{name}-sshkeys@.service
mkdir -p %{buildroot}%{dracutmodulesdir}
cp -a dracut/* %{buildroot}%{dracutmodulesdir}
rm %{buildroot}%{dracutmodulesdir}/30afterburn/afterburn-network-kargs.service

%pre
%service_add_pre %{name}.service %{name}-checkin.service %{name}-firstboot-checkin.service %{name}-sshkeys@.service %{name}-sshkeys.target

%post
%service_add_post %{name}.service %{name}-checkin.service %{name}-firstboot-checkin.service %{name}-sshkeys@.service %{name}-sshkeys.target

%preun
%service_del_preun %{name}.service %{name}-checkin.service %{name}-firstboot-checkin.service %{name}-sshkeys@.service %{name}-sshkeys.target

%postun
%service_del_postun %{name}.service %{name}-checkin.service %{name}-firstboot-checkin.service %{name}-sshkeys@.service %{name}-sshkeys.target

%files
%license LICENSE
%doc README.md
%{_bindir}/afterburn
%{_unitdir}/afterburn.service
%{_unitdir}/afterburn-checkin.service
%{_unitdir}/afterburn-firstboot-checkin.service
%{_unitdir}/afterburn-sshkeys@.service
%{_unitdir}/%{name}-sshkeys.target

%files dracut
%dir %{_sysconfdir}/cmdline.d
%{dracutmodulesdir}/30afterburn/

%changelog
