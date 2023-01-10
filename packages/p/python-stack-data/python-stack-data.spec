#
# spec file for package python-stack-data
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


Name:           python-stack-data
Version:        0.2.0
Release:        0
Summary:        Extract data from python stack frames and tracebacks
License:        MIT
URL:            https://github.com/alexmojaki/stack_data
Source:         https://files.pythonhosted.org/packages/source/s/stack_data/stack_data-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 29-Pygments-2-12.patch gh#alexmojaki/stack_data#29 mcepl@suse.com
# Make the package compatible with Pygments 2.12.
Patch0:         29-Pygments-2-12.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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
# incompatibility with Pygments
%pytest -k 'not test_pygments_example'

%files %{python_files}
%{python_sitelib}/stack_data
%{python_sitelib}/stack_data-%{version}*-info

%changelog
