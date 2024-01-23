#
# spec file for package python-jsonpath-ng
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


Name:           python-jsonpath-ng
Version:        1.6.1
Release:        0
Summary:        JSONPath for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/h2non/jsonpath-ng
Source:         https://github.com/h2non/jsonpath-ng/archive/refs/tags/v%{version}.tar.gz#/jsonpath-ng-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator
Requires:       python-ply
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ply}
#
BuildRequires:  %{python_module pytest}
BuildRequires:  python3-oslotest
# /SECTION
%python_subpackages

%description
A final implementation of JSONPath for Python that aims to be
standard compliant, including arithmetic and binary comparison
operators and providing clear AST for metaprogramming.

%prep
%setup -q -n jsonpath-ng-%{version}
sed -i '1{/^#!/d}' jsonpath_ng/bin/jsonpath.py
cp tests/test_jsonpath_rw_ext.py /tmp

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jsonpath_ng
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative jsonpath_ng

%postun
%python_uninstall_alternative jsonpath_ng

%check
export PYTHONPATH=${CWD}
%{python_expand cp /tmp/test_jsonpath_rw_ext.py tests/
if [[ ! -d %{buildroot}%{$python_sitelib}/oslotest ]]; then
  rm tests/test_jsonpath_rw_ext.py
fi
$python -m pytest
}

%files %{python_files}
%license LICENSE
%doc README.rst History.md
%python_alternative %{_bindir}/jsonpath_ng
%{python_sitelib}/jsonpath_ng
%{python_sitelib}/jsonpath_ng-%{version}.dist-info

%changelog
