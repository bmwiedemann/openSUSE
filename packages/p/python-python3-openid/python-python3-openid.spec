#
# spec file for package python-python3-openid
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


# tests are partly broken
%bcond_without     test
%{?sle15allpythons}
Name:           python-python3-openid
Version:        3.2.0
Release:        0
Summary:        OpenID support for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/necaris/python3-openid
Source:         https://files.pythonhosted.org/packages/source/p/python3-openid/python3-openid-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module psycopg2}
%if 0%{?suse_version} > 1500
BuildRequires:  %{python_module mysqlclient}
%endif
%endif
%python_subpackages

%description
This is a set of Python packages to support the use of
the OpenID decentralized identity system in applications.
Includes example code and support for a variety of storage back-ends.

%prep
%setup -q -n python3-openid-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pyunittest openid.test.test_suite
%endif

%files %{python_files}
%license LICENSE
%doc NEWS.md
%{python_sitelib}/openid
%{python_sitelib}/python3[-_]openid-%{version}*-info

%changelog
