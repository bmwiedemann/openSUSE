#
# spec file for package python-pybeam
#
# Copyright (c) 2019 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_with    doc
%bcond_without test
%define psuffix -test
%endif
%if "%{flavor}" == ""
%bcond_with    doc
%bcond_with    test
%endif
Name:           python-pybeam%{?psuffix}
Version:        0.5
Release:        0
Summary:        Python module to parse Erlang BEAM files
License:        MIT
Group:          Development/Languages/Python
URL:            http://github.com/matwey/pybeam
Source:         https://files.pythonhosted.org/packages/source/p/pybeam/pybeam-%{version}.tar.gz
Patch0:         make_sphinx_optional.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with doc}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module construct < 2.10}
BuildRequires:  %{python_module construct >= 2.9}
%endif
%if %{with test}
BuildRequires:  %{python_module pybeam == %{version}}
BuildRequires:  %{python_module six}
%endif
Requires:       python-construct < 2.10
Requires:       python-construct >= 2.9
Requires:       python-six >= 1.4.0
BuildArch:      noarch
%python_subpackages

%description
Python module to parse Erlang BEAM files, now it is able to read
imports, exports, atoms, as well as compile info and attribute
chunks in pretty python format.

%package -n %{name}-doc
Summary:        API Documentation for %name
Group:          Documentation/HTML

%description -n %{name}-doc
Python module to parse Erlang BEAM files, now it is able to read
imports, exports, atoms, as well as compile info and attribute
chunks in pretty python format.

%prep
%setup -q -n pybeam-%{version}
%patch0 -p1

%build
%if %{without test}
%python_build
%endif
%if %{with doc}
%python_build build_sphinx
%endif

%install
%if %{without test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%python_exec setup.py test
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/*
%endif

%if %{with doc}
%files -n %{name}-doc
%doc build/html
%endif

%changelog
