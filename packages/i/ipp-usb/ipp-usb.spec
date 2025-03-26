#
# spec file for package ipp-usb
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


%define         import_path github.com/OpenPrinting/ipp-usb
Name:           ipp-usb
Version:        0.9.30
Release:        0
Summary:        HTTP reverse proxy, backed by IPP-over-USB connection to device
License:        BSD-2-Clause
URL:            https://github.com/OpenPrinting/ipp-usb
Source0:        %{name}-%{version}.tar.zst
Source1:        %{name}.service
BuildRequires:  goipp
BuildRequires:  golang-packaging
BuildRequires:  gzip
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(systemd)

%description
IPP-over-USB allows using the IPP protocol, normally designed for network
printers, to be used with USB printers as well.

%prep
%autosetup
%goprep %{import_path}

%build
go build -buildmode=pie -mod=vendor .

%install
install -d %{buildroot}%{_datadir}/%{name}/quirks
install -Dm0755 %{name} %{buildroot}%{_sbindir}/%{name}
install -Dm0644 systemd-udev/71-%{name}.rules %{buildroot}/%{_prefix}/lib/udev/rules.d/71-%{name}.rules
install -Dm0644 %{name}-quirks/* %{buildroot}%{_datadir}/%{name}/quirks/
install -Dm0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -Dm0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system/%{name}.service
install -d %{buildroot}%{_localstatedir}/log/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%check
#needs a daemon to function

%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}
%{_prefix}/lib/udev/rules.d/71-%{name}.rules
%{_localstatedir}/log/%{name}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/%{name}.conf
%{_prefix}/lib/systemd/system/%{name}.service
%{_datadir}/%{name}

%changelog
