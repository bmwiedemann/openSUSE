#
# spec file for package python-stack-data
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
Name:           python-stack-data
Version:        0.6.3
Release:        0
Summary:        Extract data from python stack frames and tracebacks
License:        MIT
URL:            https://github.com/alexmojaki/stack_data
Source:         https://files.pythonhosted.org/packages/source/s/stack_data/stack_data-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# PATCH-FIX-UPSTREAM https://github.com/alexmojaki/stack_data/pull/58 Modify test_executing_style_defs to work with Pygments 2.19
Patch0:         pygments.patch
Requires:       python-asttokens
Requires:       python-executing
Requires:       python-pure-eval
Suggests:       python-littleutils
Suggests:       python-pygments
Suggests:       python-pytest
Suggests:       python-typeguard
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module asttokens}
BuildRequires:  %{python_module executing}
BuildRequires:  %{python_module littleutils}
BuildRequires:  %{python_module pure-eval}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typeguard}
# /SECTION
%python_subpackages

%description
Extract data from python stack frames and tracebacks for informative displays

%prep
%autosetup -p1 -n stack_data-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# incompatibility with even older Pygments
%pytest -k 'not ((test_core and test_pygments_example) or (test_serializer and test_example))'

%files %{python_files}
%{python_sitelib}/stack_data
%{python_sitelib}/stack_data-%{version}*-info

%changelog
