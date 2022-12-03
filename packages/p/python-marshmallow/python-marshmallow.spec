#
# spec file for package python-marshmallow
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-marshmallow
Version:        3.19.0
Release:        0
Summary:        ORM/ODM/framework-agnostic library to convert datatypes from/to Python types
License:        BSD-3-Clause AND MIT
Group:          Development/Languages/Python
URL:            https://marshmallow.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/m/marshmallow/marshmallow-%{version}.tar.gz
# https://github.com/humitos/sphinx-version-warning/issues/22
Patch0:         python-marshmallow-no-version-warning.patch
BuildRequires:  %{python_module autodocsumm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       %{name}-docs
Suggests:       python-python-dateutil
Suggests:       python-simplejson
BuildArch:      noarch
# SECTION doc build requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-alabaster
BuildRequires:  python3-sphinx-issues
BuildRequires:  python3-sphinx-version-warning
# /SECTION
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module simplejson}
# /SECTION
%python_subpackages

%package -n %{name}-docs
Summary:        Documentation files for %{name}
Group:          Documentation/Other

%description
marshmallow is an ORM/ODM/framework-agnostic library for converting complex
datatypes, such as objects, to and from native Python datatypes.

%description -n %{name}-docs
HTML Documentation and examples for %{name}.

%prep
%setup -q -n marshmallow-%{version}
%autopatch -p1

%build
%python_build
sphinx-build-%{python3_bin_suffix} docs/ docs/_build/html
rm -r docs/_build/html/.buildinfo docs/_build/html/.doctrees

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE NOTICE
%{python_sitelib}/*

%files -n %{name}-docs
%doc examples docs/_build/html/

%changelog
