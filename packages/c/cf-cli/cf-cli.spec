#
# spec file for package cf-cli
#
# Copyright (c) 2025 SUSE LLC and contributors
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


# Define just "test" as a package in _multibuild file to distinguish test
# instructions here
%if "@BUILD_FLAVOR@" == ""
%define _test 0
%define name_ext %nil
%else
%define _test 1
%define name_ext -test
%endif

%global provider        code.cloudfoundry
%global provider_tld    org
%global project         ""
%global repo            cli
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define         short_name cf-cli
Name:           %{short_name}%{?name_ext}
Version:        8.16.0+git.0.4b92b73e4
Release:        0
Summary:        Cloud Foundry command line client
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/cloudfoundry/cli
Source:         cli-%{version}.tar.gz
Source1:        README
Source2:        vendor.tar.gz
%if 0%{?_test}
BuildRequires:  %{short_name} = %{version}
%else
BuildRequires:  go
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.25
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif

%description
This is the official command line client for Cloud Foundry.

%prep
%if 0%{?_test}
# workaround to prevent post/install failing assuming this file for whatever
# reason
touch %{_sourcedir}/%{short_name}
%else
%autosetup -n cli-%{version} -a2
cp %{SOURCE1} ./
%endif

%build
%if 0%{?_test}
cf --help
%else
# show correct version instead of 0.0.0
grep -rl "0.0.0-unknown-version" ./ | xargs sed -i 's/0.0.0-unknown-version/%{version}/g'
%goprep %{import_path}
%gobuild

%check
echo 'Test if cf can be executed'
../go/bin/cli --version
%endif

%install
%if 0%{?_test}
# disable debug packages in package test to prevent error about missing files
%define debug_package %{nil}
%else
mkdir -p %{buildroot}/%{_bindir}
cp ../go/bin/cli %{buildroot}/%{_bindir}/cf
cp %{SOURCE1} ./
%endif

%files
%if 0%{?_test}
%defattr(-,root,root,-)
%else
%defattr(-,root,root,-)
%{_bindir}/cf
%license LICENSE
%doc NOTICE README
%endif

%changelog
