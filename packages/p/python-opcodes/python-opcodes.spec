#
# spec file for package python-opcodes
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
Name:           python-opcodes
Version:        0.3.14
Release:        0
Summary:        Database of Processor Instructions/Opcodes
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Maratyszcza/Opcodes
Source:         https://files.pythonhosted.org/packages/source/o/opcodes/opcodes-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
The goal of this project is to document instruction sets in a format convenient
for tools development. An instruction set is represented by three files:

- An XML file that describes instructions
- An XSD file that describes the structure of the XML file
- A Python module that reads the XML file and represents it as a set of Python
  objects

This project is a spin-off from <https://github.com/Maratyszcza/PeachPy

%prep
%setup -q -n opcodes-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc readme.rst
%license license.rst
%{python_sitelib}/opcodes
%{python_sitelib}/opcodes-%{version}.dist-info

%changelog
