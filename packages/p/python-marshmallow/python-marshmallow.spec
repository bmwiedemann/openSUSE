#
# spec file for package python-marshmallow
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%define psuffix -doc
%bcond_without doc
%else
%define psuffix %{nil}
%bcond_with doc
%endif
%{?sle15_python_module_pythons}
Name:           python-marshmallow
Version:        3.26.2
Release:        0
Summary:        ORM/ODM/framework-agnostic library to convert datatypes from/to Python types
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://marshmallow.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/m/marshmallow/marshmallow-%{version}.tar.gz
BuildRequires:  %{python_module autodocsumm}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 17.0
Suggests:       %{name}-doc
Suggests:       python-python-dateutil
Suggests:       python-simplejson
BuildArch:      noarch
%if %{with doc}
# SECTION doc build requirements
%if 0%{?suse_version} == 1500 && 0%{?sle_version} >= 150400
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module furo}
BuildRequires:  %{python_module marshmallow = %{version}}
BuildRequires:  %{python_module sphinx-autodoc-typehints}
BuildRequires:  %{python_module sphinx-copybutton}
BuildRequires:  %{python_module sphinx-issues}
BuildRequires:  %{python_module sphinxext-opengraph}
%else
BuildRequires:  python3-Sphinx
BuildRequires:  python3-furo
BuildRequires:  python3-marshmallow = %{version}
BuildRequires:  python3-sphinx-autodoc-typehints
BuildRequires:  python3-sphinx-issues
BuildRequires:  python3-sphinxcontrib-copybutton
BuildRequires:  python3-sphinxext-opengraph
%endif
# /SECTION
%endif
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module simplejson}
# /SECTION
%python_subpackages

%description
marshmallow is an ORM/ODM/framework-agnostic library for converting complex
datatypes, such as objects, to and from native Python datatypes.

%if %{with doc}
%package -n %{name}-doc
Summary:        Documentation files for %{name}
Group:          Documentation/Other
Provides:       %{name}-docs = %{version}
Obsoletes:      %{name}-docs < %{version}

%description -n %{name}-doc
HTML Documentation and examples for %{name}.
%endif

%prep
%setup -q -n marshmallow-%{version}
%autopatch -p1

%build
%if !%{with doc}
%pyproject_wheel
%else
sphinx-build docs/ docs/_build/html
rm -r docs/_build/html/.buildinfo docs/_build/html/.doctrees
%endif

%install
%if !%{with doc}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_from_timestamp_with_overflow_value fails on 32bit with different error (the value gets caught earlier)
%pytest -k "not test_from_timestamp_with_overflow_value"

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE NOTICE
%{python_sitelib}/marshmallow
%{python_sitelib}/marshmallow-*.dist-info
%else

%files -n %{name}-doc
%doc docs/examples docs/_build/html/
%endif

%changelog
