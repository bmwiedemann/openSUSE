#
# spec file for package python-pyelftools
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
Name:           python-pyelftools
Version:        0.25
Release:        0
Summary:        Library for analyzing ELF files and DWARF debugging information
License:        SUSE-Public-Domain
Group:          Development/Languages/Python
URL:            https://github.com/eliben/pyelftools
Source:         https://files.pythonhosted.org/packages/source/p/pyelftools/pyelftools-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
pyelftools is a pure python library for analyzing ELF files and DWARF debugging information

%prep
%setup -q -n pyelftools-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test/run_all_unittests.py
%python_exec test/run_examples_test.py
# May fail due to minor differences in the output of readelf
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#tests
%python_exec test/run_readelf_tests.py || :

%files %{python_files}
%license LICENSE
%doc CHANGES
%python3_only %{_bindir}/readelf.py
%{python_sitelib}/*

%changelog
