#
# spec file for package python-pybeam
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%endif
%if "%{flavor}" == ""
%bcond_with    test
%endif
Name:           python-pybeam%{?psuffix}
Version:        0.8
Release:        0
Summary:        Python module to parse Erlang BEAM files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matwey/pybeam
Source:         https://files.pythonhosted.org/packages/source/p/pybeam/pybeam-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-construct < 2.11
Requires:       python-construct >= 2.9
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module construct < 2.11}
BuildRequires:  %{python_module construct >= 2.9}
BuildRequires:  %{python_module pybeam}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Python module to parse Erlang BEAM files, now it is able to read
imports, exports, atoms, as well as compile info and attribute
chunks in pretty python format.

%package -n %{name}-doc
Summary:        API Documentation for %{name}
Group:          Documentation/HTML

%description -n %{name}-doc
Python module to parse Erlang BEAM files, now it is able to read
imports, exports, atoms, as well as compile info and attribute
chunks in pretty python format.

%prep
%autosetup -p1 -n pybeam-%{version}

%build
%if %{without test}
%pyproject_wheel
%endif

%install
%if %{without test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if %{without test}
%files %{python_files}
%license LICENSE
%{python_sitelib}/pybeam
%{python_sitelib}/pybeam-*-info
%endif

%changelog
