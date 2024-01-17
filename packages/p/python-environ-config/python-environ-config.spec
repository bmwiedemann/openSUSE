#
# spec file for package python-environ-config
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


Name:           python-environ-config
Version:        23.2.0
Release:        0
Summary:        Boilerplate-free configuration with env variables
License:        MIT
URL:            https://github.com/hynek/environ_config
Source:         https://files.pythonhosted.org/packages/source/e/environ-config/environ_config-%{version}.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17.4.0
Conflicts:      python-django-environ
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 17.4.0}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module urllib3 < 2}
# /SECTION
%python_subpackages

%description
Boilerplate-free configuration with env variables.

%prep
%setup -q -n environ_config-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/environ
%{python_sitelib}/environ_config-%{version}.dist-info

%changelog
