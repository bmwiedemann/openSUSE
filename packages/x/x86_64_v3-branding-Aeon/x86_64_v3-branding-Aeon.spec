#
# spec file for package x86_64_v3-branding-Aeon
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


Name:           x86_64_v3-branding-Aeon
Version:        20240429
Release:        0
Summary:        Aeon configuration for x86_64_v3 support
License:        MIT 
URL:            https://en.opensuse.org/Portal:Aeon
Source:         x86_64_v3-transactional-update.service
BuildRequires:  systemd-rpm-macros
BuildArch:      noarch
Requires:	transactional-update

%description
Aeon configuration for ensuring x86_64_v3 binaries are installed and updated

%prep
cp -a %{SOURCE0} x86_64_v3-transactional-update.service

%build

%install
install -d %{buildroot}%{_unitdir}
install -D -m 644 x86_64_v3-transactional-update.service %{buildroot}%{_unitdir}

%pre
%systemd_pre x86_64_v3-transactional-update.service

%post
%systemd_post x86_64_v3-transactional-update.service

%preun
%systemd_preun x86_64_v3-transactional-update.service

%files
%{_unitdir}/x86_64_v3-transactional-update.service

%changelog

