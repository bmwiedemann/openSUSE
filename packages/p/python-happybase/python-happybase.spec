#
# spec file for package python-happybase
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


Name:           python-happybase
Version:        1.2.0
Release:        0
Summary:        A Python library to interact with Apache HBase
License:        MIT
URL:            https://github.com/wbolster/happybase
Source:         https://github.com/wbolster/happybase/archive/%{version}.tar.gz
# https://github.com/python-happybase/happybase/pull/238
Patch0:         use_pytest.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module thriftpy2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-six
Requires:       python-thriftpy2 >= 0.4
BuildArch:      noarch
%python_subpackages

%description
HappyBase is a Python library to interact with Apache HBase.

%package -n python-happybase-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module happybase-doc = %{version}}

%description -n python-happybase-doc
HappyBase is a Python library to interact with Apache HBase.

This package contains the documentation.

%prep
%autosetup -p1 -n happybase-%{version}

%build
%pyproject_wheel
sphinx-build -b html doc docs/build/html

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm -r docs/build/html/.[a-z]*

%check
# the api tests need running thrift server
%pytest tests/test_util.py

%files %{python_files}
%license LICENSE.rst
%doc NEWS.rst README.rst TODO.rst
%{python_sitelib}/happybase
%{python_sitelib}/happybase-%{version}.dist-info

%files -n python-happybase-doc
%license LICENSE.rst
%doc docs/build/html

%changelog
