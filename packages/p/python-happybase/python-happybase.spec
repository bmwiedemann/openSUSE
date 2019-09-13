#
# spec file for package python-happybase
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-happybase
Version:        1.1.0
Release:        0
Summary:        A Python library to interact with Apache HBase
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/wbolster/happybase
Source:         https://files.pythonhosted.org/packages/source/h/happybase/happybase-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module thriftpy}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-six
Requires:       python-thriftpy >= 0.3.8
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
%setup -q -n happybase-%{version}

%build
%python_build
sphinx-build -b html doc docs/build/html

%install
%python_install
rm docs/build/html/.doctrees/environment.pickle

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.rst
%doc NEWS.rst README.rst TODO.rst
%{python_sitelib}/*

%files -n python-happybase-doc
%license LICENSE.rst
%doc docs/build/html

%changelog
