#
# spec file for package distribution-gpg-keys
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Nicolas FORMICHELLA <stigpro@outlook.fr>
# Copyright (c) 2022 Neal Gompa <ngompa13@gmail.com>.
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           distribution-gpg-keys
Version:        1.115
Release:        0
Summary:        GPG keys of various Linux distributions
Group:          System/Packages
License:        CC0-1.0
URL:            https://github.com/rpm-software-management/distribution-gpg-keys
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch

%description
GPG keys used by various Linux distributions to sign packages.

%prep
%autosetup -p1

%build
#nothing to do here

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/

# We don't want to package COPR GPG keys
rm -rf %{buildroot}%{_datadir}/%{name}/copr

%fdupes %{buildroot}/%{_prefix}

%files
%license LICENSE
%doc README.md SOURCES.md
%{_datadir}/%{name}/

%changelog
