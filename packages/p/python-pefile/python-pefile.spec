#
# spec file for package python-pefile
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
Name:           python-pefile
Version:        2019.4.18
Release:        0
Summary:        A python module to work with PE (pertable executable) files
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/erocarrera/pefile
Source:         https://files.pythonhosted.org/packages/source/p/pefile/pefile-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
# SECTION test requirements
BuildRequires:  %{python_module future}
# /SECTION
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
%setup -q -n pefile-%{version}
sed -i -e '/^#!\//, 1d' pefile.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests not in sdist and have good reason to at time of writing:
# https://github.com/erocarrera/pefile/issues/82#issuecomment-192018385
# https://github.com/erocarrera/pefile/issues/171
# %%check
# %%python_exec setup.py test

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/*

%changelog
