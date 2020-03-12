#
# spec file for package python-partd
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-partd
Version:        1.1.0
Release:        0
Summary:        Appendable key-value storage
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mrocklin/partd/
Source:         https://files.pythonhosted.org/packages/source/p/partd/partd-%{version}.tar.gz
BuildRequires:  %{python_module locket}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toolz}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-locket
Requires:       python-toolz
Recommends:     python-blosc
Recommends:     python-msgpack-python
Recommends:     python-numpy >= 1.9.0
Recommends:     python-pandas
Recommends:     python-pyzmq
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Key-value byte store with appendable values

Partd stores key-value pairs.
Values are raw bytes.
We append on old values.

Partd excels at shuffling operations.

%prep
%setup -q -n partd-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
