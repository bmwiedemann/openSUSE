#
# spec file for package python-dynaconf
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-dynaconf
Version:        2.1.1
Release:        0
Summary:        The dynamic configurator for your Python Project
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rochacbruno/dynaconf
Source:         https://github.com/rochacbruno/dynaconf/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.6.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-click
Requires:       python-configobj
Requires:       python-python-box
Requires:       python-python-dotenv
Requires:       python-setuptools
Requires:       python-toml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 0.12}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-box}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module toml}
# /SECTION
%python_subpackages

%description
The dynamic configurator for your Python Project

%prep
%setup -q -n dynaconf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python3_only %{_bindir}/dynaconf
%{python_sitelib}/*

%changelog
