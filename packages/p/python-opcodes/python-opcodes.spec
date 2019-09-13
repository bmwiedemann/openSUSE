#
# spec file for package python-opcodes
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
Name:           python-opcodes
Version:        0.3.14
Release:        0
Summary:        Database of Processor Instructions/Opcodes
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/Maratyszcza/Opcodes
Source:         https://files.pythonhosted.org/packages/source/o/opcodes/opcodes-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module nose}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand %{_bindir}/nosetests-%{$python_bin_suffix} 

%files %{python_files}
%doc readme.rst
%license license.rst 
%{python_sitelib}/*

%changelog
