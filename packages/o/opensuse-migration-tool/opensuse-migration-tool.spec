#
# spec file for package opensuse-migration-tool
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Marcela Maslanova
# Copyright (c) 2025 Lubos Kocman
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


Name:           opensuse-migration-tool
Version:        20251029.ed0d12d
Release:        0
Summary:        Migration and Upgrade tool for openSUSE
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/openSUSE/opensuse-migration-tool
Source:         opensuse-migration-tool-%{version}.tar.xz
Requires:       bc
Requires:       curl
Requires:       dialog
Requires:       gawk
Requires:       jq
Requires:       sed
BuildArch:      noarch

%description
openSUSE migration and upgrade tool which utilizes get.opensuse.org product API and openSUSE-repos
for a cross-distro migration and upgrade to a new versions of point releases.

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_sbindir}
cp %{name} %{buildroot}/%{_sbindir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp SLES.prod %{buildroot}/%{_datadir}/%{name}/SLES.prod

# Install scripts directory
cp -a scripts %{buildroot}/%{_datadir}/%{name}/

# Dialogrc custom theme
cp dialogrc %{buildroot}%{_datadir}/%{name}/dialogrc

%check

%files
%defattr(644,root,root,755)
%attr(0755, root, root) %{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/scripts
%{_datadir}/%{name}
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/dialogrc
%attr(0755, root, root) %{_datadir}/%{name}/scripts/*
%attr(0644, root, root) %{_datadir}/%{name}/SLES.prod

%license LICENSE
%doc README.md

%changelog
