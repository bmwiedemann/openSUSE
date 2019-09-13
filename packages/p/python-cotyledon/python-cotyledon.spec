#
# spec file for package python
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
%global sname cotyledon
Name:           python-%{sname}
Version:        1.7.3
Release:        0
Summary:        A framework for defining long-running services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/sileht/cotyledon
Source:         https://files.pythonhosted.org/packages/source/c/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module oslo.config >= 3.14.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setproctitle}
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-setproctitle
BuildRequires:  fdupes
BuildArch:      noarch

%description
Cotyledon provides a framework for defining long-running services.

%python_subpackages

%package -n python-%{sname}-doc
Summary:        Documentation for cotyledon, a framework for long-running services
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description -n python-%{sname}-doc
Cotyledon provides a framework for defining long-running services.

This package contains documentation files for %{name}.

%prep
%setup -q -n %{sname}-%{version}
rm tox.ini

%build
%python_build
python3 setup.py build_sphinx
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest cotyledon/tests/test_unit.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/%{sname}
%{python_sitelib}/*.egg-info

%files -n python-%{sname}-doc
%license LICENSE
%doc README.rst
%doc doc/build/html

%changelog
