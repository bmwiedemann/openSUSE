#
# spec file for package python-ctypesgen
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


Name:           python-ctypesgen
Version:        1.1.1
Release:        0
Summary:        Python wrapper generator for ctypes
License:        BSD-2-Clause
URL:            https://github.com/ctypesgen/ctypesgen
Source:         https://files.pythonhosted.org/packages/source/c/ctypesgen/ctypesgen-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{pythons} >= 3.7
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
ctypesgen is a pure-python ctypes wrapper generator. It parses C header files
and creates a wrapper for libraries based on what it finds.

%prep
%autosetup -p1 -n ctypesgen-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ctypesgen
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Create a dir in PWD and set TMPDIR to avoid writing to /tmp
export TMPDIR=`mktemp -d -p ${PWD}`
%pyunittest -v

%post
%python_install_alternative ctypesgen

%postun
%python_uninstall_alternative ctypesgen

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/ctypesgen
%{python_sitelib}/ctypesgen/
%{python_sitelib}/ctypesgen-%{version}*-info/

%changelog
