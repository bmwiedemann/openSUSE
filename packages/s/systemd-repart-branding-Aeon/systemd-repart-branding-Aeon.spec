#
# spec file for package systemd-repart-branding-Aeon
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


Name:           systemd-repart-branding-Aeon
Version:        20240404
Release:        0
Summary:        Aeon configuration for systemd-repart
License:        MIT
URL:            https://en.opensuse.org/Portal:Aeon
Source:         50-root.conf
Source1:        00-esp.conf
Source2:        LICENSE
BuildArch:      noarch
Provides:       systemd-repart-branding
Conflicts:      systemd-repart-branding

%description
Aeon configuration for systemd-repart

%prep
cp -a %{SOURCE0} 50-root.conf
cp -a %{SOURCE1} 00-esp.conf
cp -a %{SOURCE2} LICENSE

%build

%install
install -d %{buildroot}%{_prefix}/lib/repart.d
install -D -m 644 50-root.conf %{buildroot}%{_prefix}/lib/repart.d/
install -D -m 644 00-esp.conf %{buildroot}%{_prefix}/lib/repart.d/

%files
%license LICENSE
%dir %{_prefix}/lib/repart.d
%{_prefix}/lib/repart.d/50-root.conf
%{_prefix}/lib/repart.d/00-esp.conf

%changelog
