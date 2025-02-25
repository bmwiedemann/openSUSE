#
# spec file for package python-sphinxcontrib-programoutput
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


%{?sle15_python_module_pythons}
Name:           python-sphinxcontrib-programoutput
Version:        0.18
Release:        0
Summary:        Sphinx extension to include program output
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://sphinxcontrib-programoutput.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib_programoutput/sphinxcontrib_programoutput-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 5.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 5.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Sphinx extension to literally insert the output of arbitrary commands into
documents, helping you to keep your command examples up to date.

%prep
%setup -q -n sphinxcontrib_programoutput-%{version}

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/sphinxcontrib/programoutput/tests/
rm -r %{buildroot}%{$python_sitelib}/sphinxcontrib/__*
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export LANG=en_US.UTF-8
%pyunittest -v src/sphinxcontrib/programoutput/tests/test*.py

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/sphinxcontrib/programoutput/
%{python_sitelib}/sphinxcontrib_programoutput-%{version}*info

%changelog
