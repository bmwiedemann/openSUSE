#
# spec file for package purge-kernels-service
#
# Copyright (c) 2020 SUSE LLC
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


Name:           purge-kernels-service
Version:        0
Release:        0
Summary:        The service for removing old kernels when multiversion is enabled
License:        MIT
Source:         purge-kernels.service
Conflicts:      dracut < 049+git118
Provides:       dracut:/usr/lib/systemd/system/purge-kernels.service
Requires:       zypper(purge-kernels)
BuildRequires:  systemd-rpm-macros
BuildArch:      noarch

%description
This service runs zypper purge-kernels on boot after a kernel package was installed.

%prep

%build

%install
install -m 644 -D -t %{buildroot}/%{_unitdir}/ %{SOURCE0}

%pre
%service_add_pre purge-kernels.service
%post
%service_add_post purge-kernels.service
%preun
%service_del_preun purge-kernels.service
%postun
%service_del_postun purge-kernels.service

%files
%{_unitdir}/purge-kernels.service

%changelog
