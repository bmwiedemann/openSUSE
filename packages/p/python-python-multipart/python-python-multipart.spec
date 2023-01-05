#
# spec file for package python-python-multipart
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


Name:           python-python-multipart
Version:        0.0.5
Release:        0
License:        Apache-2.0
Summary:        Python streaming multipart parser
URL:            http://github.com/andrew-d/python-multipart
Source:         https://files.pythonhosted.org/packages/source/p/python-multipart/python-multipart-%{version}.tar.gz
Patch0:         support-pyyaml-6.patch
# https://github.com/andrew-d/python-multipart/commit/8cff1aac7479fbb69087e355f66315b21640bab0
# https://github.com/andrew-d/python-multipart/commit/2c7e95c7236fcecdb5660823936403d1359fdb85
Patch1:         python-python-multipart-no-mock.patch
# https://github.com/andrew-d/python-multipart/commit/c54ad6006bacc77623864ec8e5c96bfd32230e01
Patch2:         python-python-multipart-no-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
A streaming multipart parser for Python.

%prep
%autosetup -p1 -n python-multipart-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/multipart
%{python_sitelib}/python_multipart-%{version}.dist-info

%changelog
