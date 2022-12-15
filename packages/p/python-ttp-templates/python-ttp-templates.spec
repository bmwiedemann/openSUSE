#
# spec file for package python-ttp-templates
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-ttp-templates
Version:        0.3.2
Release:        0
Summary:        Template Text Parser Templates collections
License:        MIT
URL:            https://github.com/dmulyalin/ttp_templates
Source:         https://github.com/dmulyalin/ttp_templates/archive/refs/tags/%{version}.tar.gz#/ttp_templates-%{version}.tar.gz
BuildRequires:  %{python_module netmiko}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ttp}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This repository contains a collection of [TTP](https://github.com/dmulyalin/ttp) templates.

%prep
%autosetup -p1 -n ttp_templates-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cp -r ttp_templates/misc/{N,n}etmiko
pushd test
# not python-yangson package
donttest="test_yang_ietf_interfaces"
%pytest -k "not ($donttest)"
popd

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ttp_templates
%{python_sitelib}/ttp_templates-%{version}*-info

%changelog
