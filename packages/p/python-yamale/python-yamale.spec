#
# spec file for package python-yamale
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-yamale
Version:        4.0.4
Release:        0
Summary:        A schema and validator for YAML
License:        MIT
URL:            https://github.com/23andMe/Yamale
Source:         https://github.com/23andMe/Yamale/archive/refs/tags/%{version}.tar.gz#/yamale-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml}
# /SECTION
%python_subpackages

%description
A schema and validator for YAML.

%prep
%autosetup -p1 -n Yamale-%{version}

find . -type f -name "*.py" -exec sed -i '/#!\/usr\/bin\/env/d' {} +

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/yamale
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest yamale

%post
%python_install_alternative yamale

%postun
%python_uninstall_alternative yamale

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/yamale
%{python_sitelib}/yamale
%{python_sitelib}/yamale-%{version}*-info/

%changelog
