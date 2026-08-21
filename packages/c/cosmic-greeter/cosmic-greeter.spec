#
# spec file for package cosmic-greeter
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         appid com.system76.CosmicGreeter
Name:           cosmic-greeter
Version:        1.6.0
Release:        0
Summary:        COSMIC greeter for greetd
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-greeter
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        %{name}.service
Source3:        %{name}-daemon.service
Source4:        %{name}.sysusers
Patch0:         change-imageformat.patch
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  git-core
BuildRequires:  greetd
BuildRequires:  just
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  sysuser-tools
BuildRequires:  wallpaper-branding-openSUSE
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
Recommends:     fprintd-pam
Recommends:     xinit
Requires:       bash
Requires:       cosmic-comp
Requires:       greetd >= 0.10
Requires:       mozilla-fira-fonts
%systemd_requires
%sysusers_requires

%description
libcosmic greeter for greetd, which can be run inside cosmic-comp

%prep
%autosetup -p1 -a1
cp %{_datadir}/wallpapers/openSUSEdefault/contents/images/default-dark.png res/background.png

%build
%sysusers_generate_pre %{SOURCE4} %{name} %{name}.conf
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
install -d %{buildroot}%{_sharedstatedir}/%{name}
install -D -m 0644 %{name}.toml %{buildroot}%{_sysconfdir}/greetd/%{name}.toml
chmod 0644 %{buildroot}%{_datadir}/dbus-1/system.d/%{appid}.conf
chmod -x %{buildroot}%{_datadir}/dbus-1/system.d/%{appid}.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}-daemon.service
rm -f %{buildroot}%{_sysusersdir}/%{name}.conf

# workaround for getting the right pam permissions
install -d %{buildroot}%{_prefix}/lib/pam.d
ln -s %{_prefix}/lib/pam.d/greetd %{buildroot}%{_prefix}/lib/pam.d/%{name}

%pre -f %{name}.pre
%service_add_pre %{name}.service %{name}-daemon.service

%post
%service_add_post %{name}.service %{name}-daemon.service
%tmpfiles_create %{_prefix}/lib/tmpfiles.d/%{name}.conf

%preun
%service_del_preun %{name}.service %{name}-daemon.service

%postun
%service_del_postun %{name}.service %{name}-daemon.service

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/greetd/%{name}.toml
%{_bindir}/%{name}
%{_bindir}/%{name}-daemon
%{_bindir}/%{name}-start
%{_datadir}/dbus-1/system.d/%{appid}.conf
%{_prefix}/lib/pam.d/%{name}
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}-daemon.service
%{_unitdir}/%{name}.service

%changelog
