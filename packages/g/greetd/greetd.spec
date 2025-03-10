#
# spec file for package greetd
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


%if 0%{?suse_version} >= 1550
  %define _pam_confdir %{_pam_vendordir}
  %define _config_norepl %nil
%else
  %define _pam_confdir %{_sysconfdir}/pam.d
  %define _config_norepl %config(noreplace)
%endif

Name:           greetd
Version:        0.10.3
Release:        0
Summary:        Minimal and flexible login manager daemon
License:        GPL-3.0-only
Group:          System/X11/Displaymanagers
URL:            https://git.sr.ht/~kennylevinsen/greetd
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source3:        greetd.pam
Source99:       greetd.rpmlintrc
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  make
BuildRequires:  pam-devel
# Required for man pages
BuildRequires:  scdoc
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
Requires:       pam
# requires branding
# NOTE: unversioned branding is required to avoid issues like bsc#1205950
Requires:       %{name}-branding

%description
greetd is a login manager daemon. greetd on its own does not have any user interface,
but instead offloads that to greeters, which are arbitrary applications that implement the greetd IPC protocol.

%package agreety
Summary:        A text-based greeter for greetd
Group:          System/X11/Displaymanagers
Requires:       %{name} = %{version}

%description agreety
agreety is a very simple text-based greeter, with an appearance similar to agetty and login.

%package        fakegreet
Group:          Development/Tools/Other
Summary:        Test utility for greeter development

%description    fakegreet
fakegreet is a test utility that allows launching greeters without greetd daemon.

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/X11/Displaymanagers
Requires:       %{name} = %{version}
Requires:       %{name}-agreety = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: /etc/greetd/config.toml contains upstream config

%description branding-upstream
This package provides the upstream look and feel for greetd.

%prep
%autosetup -a1

%build
%{cargo_build}
%make_build -C man

%install

install -D -p -m 0755 target/release/%{name}   %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 target/release/agreety   %{buildroot}%{_bindir}/agreety
install -D -p -m 0755 target/release/fakegreet %{buildroot}%{_bindir}/fakegreet

%make_install PREFIX=%{_prefix} -C man

# Provide a working default shell for the stock greetd config
# https://github.com/openSUSE/openSUSEway/issues/37
sed -i -e "s|\$SHELL|bash|" config.toml
install -D -p -m 0644 config.toml %{buildroot}/%{_sysconfdir}/%{name}/config.toml

install -D -m 0644 %{name}.service %{buildroot}/%{_unitdir}/%{name}.service

install -D -m 0644 %{SOURCE3} %{buildroot}/%{_pam_confdir}/greetd

install -d %{buildroot}%{_localstatedir}/cache/greetd
install -d %{buildroot}%{_sharedstatedir}/greetd
install -d %{buildroot}/run/greetd

%check
%{cargo_test}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun_without_restart %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%_config_norepl %{_pam_confdir}/greetd
%ghost %attr(711,root,greeter) %dir /run/greetd/
%attr(750,greeter,greeter) %dir %{_sharedstatedir}/greetd
%ghost %dir %{_localstatedir}/cache/greetd/
%{_mandir}/man1/greetd.1*
%{_mandir}/man5/greetd.5*
%{_mandir}/man7/greetd-ipc.7*

%files agreety
%license LICENSE
%{_bindir}/agreety
%{_mandir}/man1/agreety.1*

%files fakegreet
%license LICENSE
%{_bindir}/fakegreet

%files branding-upstream
%license LICENSE
%dir %{_sysconfdir}/%{name}
%attr(644,greeter,greeter) %config(noreplace) %{_sysconfdir}/%{name}/config.toml

%changelog
