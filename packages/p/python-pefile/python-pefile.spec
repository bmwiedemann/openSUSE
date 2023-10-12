#
# spec file for package python-pefile
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


%{?sle15_python_module_pythons}
Name:           python-pefile
Version:        2023.2.7
Release:        0
Summary:        A python module to work with PE (pertable executable) files
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/erocarrera/pefile
Source:         https://files.pythonhosted.org/packages/source/p/pefile/pefile-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Portable Executable reader module.

All the PE file basic structures are available with their default names as
attributes of the instance returned.

Processed elements such as the import table are made available with lowercase
names, to differentiate them from the upper case basic structure names.

pefile has been tested against many edge cases such as corrupted and malformed
PEs as well as malware, which often attempts to abuse the format way beyond its
standard use. To the best of my knowledge most of the abuse is handled
gracefully.

%prep
%autosetup -p1 -n pefile-%{version}
sed -i -e '/^#!\//, 1d' pefile.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests not in sdist and have good reason to at time of writing:
# https://github.com/erocarrera/pefile/issues/82#issuecomment-192018385
# https://github.com/erocarrera/pefile/issues/171
# %%check
# %%python_exec setup.py test

%files %{python_files}
%doc README
%license LICENSE
%pycache_only %{python_sitelib}/__pycache__/pe*.pyc
%{python_sitelib}/ordlookup
%{python_sitelib}/pefile.py
%{python_sitelib}/peutils.py
%{python_sitelib}/pefile-%{version}*-info

%changelog
