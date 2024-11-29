#
# spec file for package python-asdf-astropy
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
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-asdf-astropy%{psuffix}
Version:        0.7.0
Release:        0
Summary:        ASDF serialization support for astropy
License:        BSD-3-Clause
URL:            https://github.com/astropy/asdf-astropy
Source:         https://files.pythonhosted.org/packages/source/a/asdf-astropy/asdf_astropy-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module packaging >= 19}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 60}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-asdf >= 2.14.4
Requires:       python-asdf-coordinates-schemas >= 0.3
Requires:       python-asdf-standard >= 1.1.0
Requires:       python-asdf-transform-schemas >= 0.5
Requires:       python-astropy >= 5.2
Requires:       python-numpy >= 1.24
Requires:       python-packaging >= 19
%if %{with test}
BuildRequires:  %{python_module asdf-astropy = %{version}}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
%endif
BuildArch:      noarch
%python_subpackages

%description
ASDF serialization support for astropy

%prep
%autosetup -p1 -n asdf_astropy-%{version}
sed -i 's/--color=yes//' pyproject.toml
for c in asdf_astropy/conftest.py; do
  [ -f $c ] || exit 1 # does not exist anymore
  [ ! -s $c ] && echo '# empty module' > $c
done

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest -n auto
%endif

%if !%{with test}
%files %{python_files}
%{python_sitelib}/asdf_astropy
%{python_sitelib}/asdf_astropy-%{version}.dist-info
%endif

%changelog
