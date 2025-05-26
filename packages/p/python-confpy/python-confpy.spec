#
# spec file for package python-confpy
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


Name:           python-confpy
Version:        0.11.0
Release:        0
Summary:        Config file parsing and option management
License:        MIT
URL:            https://github.com/kevinconway/confpy
Source:         https://files.pythonhosted.org/packages/source/c/confpy/confpy-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Jinja2
BuildArch:      noarch
%python_subpackages

%description
Config file parsing and option management.

%prep
%setup -q -n confpy-%{version}
find . -name '*.pyc' -delete

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/confpy-generate
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative confpy-generate

%postun
%python_uninstall_alternative confpy-generate

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/confpy-generate
%{python_sitelib}/confpy
%{python_sitelib}/confpy-%{version}*-info

%changelog
