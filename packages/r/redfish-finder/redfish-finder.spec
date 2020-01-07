#
# spec file for package redfish-finder
#
# Copyright (c) 2019 SUSE LLC
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


Name:           redfish-finder
Version:        0.4
Release:        0
Summary:        Utility for parsing smbios information and configuring canonical bmc access
License:        GPL-2.0-only
Group:          System/Management
URL:            https://github.com/nhorman/redfish-finder
Source0:        redfish-finder-0.4.tar.gz
Patch0:         python_path.patch
BuildRequires:  python3
Requires:       NetworkManager
Requires:       dmidecode
Requires:       python3
BuildArch:      noarch

%description
Scans Smbios information for type 42 management controller information, and uses
that to configure the appropriate network interface so that the bmc is
canonically accessible via the hostname redfish-localhost

%prep
%setup -q
%patch0 -p1


%build
#noop here
%pre
%service_add_pre redfish-finder.service

%install
install -D -p -m 0755 redfish-finder %{buildroot}/%{_bindir}/redfish-finder
install -D -p -m 0644 redfish-finder.1 %{buildroot}/%{_mandir}/man1/redfish-finder.1
install -D -p -m 0644 ./redfish-finder.service %{buildroot}/%{_unitdir}/redfish-finder.service
mkdir %{buildroot}/%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rc%{name}

%post
%service_add_post redfish-finder.service

%preun
%systemd_preun redfish-finder.service

%postun
%systemd_postun_with_restart redfish-finder.service

%files
%license COPYING
%doc README.md
%{_bindir}/redfish-finder
%{_sbindir}/rcredfish-finder
%{_mandir}/man1/redfish-finder.1%{?ext_man}
%{_unitdir}/redfish-finder.service

%changelog
