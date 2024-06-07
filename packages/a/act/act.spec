#
# spec file for package act
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Orville Q. Song <orville@anislet.dev>
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


%global provider        github
%global provider_tld    com
%global project         nketos
%global repo            act
%global provider_prefix %{provider}.%{provider_tld}/%{project}
%global import_path     %{provider_prefix}/%{repo}
Name:           act
Version:        0.2.63
Release:        0
Summary:        Run your GitHub Actions locally
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/nektos/act
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.16
Requires:       docker
%{go_nostrip}
%{go_provides}

%description
act helps you run your Github Actions locally.

%prep
%setup -q
%setup -q -a1 %{SOURCE1}
sed -i 's_var version = \"v0.2.27-dev\"_var version = "%{version}"_g' main.go

%build
%{goprep} .
mkdir -p vendor/%{provider_prefix}
ln -s . vendor/%{import_path}
%{gobuild} -ldflags "-s -w -X main.Version=v%{version}" .

%install
%{goinstall}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
