#
# spec file for package python-cbor2
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
Name:           python-cbor2
Version:        4.1.2
Release:        0
Summary:        Pure Python CBOR (de)serializer with extensive tag support
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/agronholm/cbor2
Source:         https://files.pythonhosted.org/packages/source/c/cbor2/cbor2-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 36.2.7}
BuildRequires:  %{python_module setuptools_scm >= 1.7.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pure Python CBOR (de)serializer with extensive tag support

%prep
%setup -q -n cbor2-%{version}
# Remove test dependency on pytest-cov
sed -i 's/--cov//' setup.cfg

%build
export LANG=en_US.UTF8
%python_build

%install
export LANG=en_US.UTF8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
%python_exec -m pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
