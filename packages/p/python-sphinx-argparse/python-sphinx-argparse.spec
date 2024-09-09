#
# spec file for package python-sphinx-argparse
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-sphinx-argparse
Version:        0.5.2
Release:        0
Summary:        Sphinx extension to document argparse commands and options
License:        MIT
URL:            https://github.com/ashb/sphinx-argparse
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx_argparse-%{version}.tar.gz
BuildRequires:  %{python_module CommonMark}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension that automatically documents argparse commands and options.

%prep
%autosetup -p1 -n sphinx_argparse-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENCE.rst
%{python_sitelib}/sphinxarg
%{python_sitelib}/sphinx_argparse-%{version}.dist-info

%changelog
