#
# spec file for package python-configobj
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
Name:           python-configobj
Version:        5.0.9
Release:        0
Summary:        Config file reading, writing and validation
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/DiffSK/configobj
# No tests in PyPI sdist
Source:         https://github.com/DiffSK/configobj/archive/refs/tags/v%{version}.tar.gz#/configobj-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
ConfigObj is a simple but powerful config file reader and writer: an ini
file round tripper. Its main feature is that it is very easy to use, with a
straightforward programmer's interface and a simple syntax for config files.
It has lots of other features though:

 * Nested sections (subsections), to any level
 * List values
 * Multiple line values
 * Full Unicode support
 * String interpolation (substitution)
 * Integrated with a powerful validation system
   - including automatic type checking/conversion
   - and allowing default values
   - repeated sections
 * All comments in the file are preserved
 * The order of keys/sections is preserved
 * Powerful ``unrepr`` mode for storing/retrieving Python data-types

%prep
%autosetup -p1 -n configobj-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/configobj
%{python_sitelib}/validate
%{python_sitelib}/configobj-%{version}.dist-info

%changelog
