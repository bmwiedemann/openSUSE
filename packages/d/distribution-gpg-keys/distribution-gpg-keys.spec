#
# spec file for package distribution-gpg-keys
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2021 Nicolas FORMICHELLA <stigpro@outlook.fr>
# Copyright (c) 2022 Neal Gompa <ngompa13@gmail.com>.
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


# Release versions are part of the git tag
%global origrel 1

Name:           distribution-gpg-keys
Version:        1.79
Release:        0
Summary:        GPG keys of various Linux distributions
Group:          System/Packages
License:        CC0-1.0
URL:            https://github.com/xsuchy/distribution-gpg-keys
Source0:        %{url}/archive/%{name}-%{version}-%{origrel}.tar.gz
BuildArch:      noarch

%description
GPG keys used by various Linux distributions to sign packages.

%prep
%setup -q -n %{name}-%{name}-%{version}-%{origrel}

%build
#nothing to do here

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/
cp -a keys/* %{buildroot}%{_datadir}/%{name}/

# We don't want to package COPR GPG keys
rm -rf %{buildroot}%{_datadir}/%{name}/copr

%files
%license LICENSE
%doc README.md SOURCES.md
%{_datadir}/%{name}/

%changelog
