#
# spec file for package python-cotyledon
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-cotyledon
Version:        2.1.0
Release:        0
Summary:        A framework for defining long-running services
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/sileht/cotyledon
Source:         https://files.pythonhosted.org/packages/source/c/cotyledon/cotyledon-%{version}.tar.gz
BuildRequires:  %{python_module oslo.config >= 3.14.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setproctitle}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-setproctitle
BuildArch:      noarch
%python_subpackages

%description
Cotyledon provides a framework for defining long-running services.

%package -n python-cotyledon-doc
Summary:        Documentation for cotyledon, a framework for long-running services
Group:          Documentation/HTML

%description -n python-cotyledon-doc
Cotyledon provides a framework for defining long-running services.

This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n cotyledon-%{version}

%build
%pyproject_wheel
sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest cotyledon/tests/test_unit.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/cotyledon
%{python_sitelib}/cotyledon-%{version}.dist-info

%files -n python-cotyledon-doc
%license LICENSE
%doc README.rst
%doc doc/build/html

%changelog
