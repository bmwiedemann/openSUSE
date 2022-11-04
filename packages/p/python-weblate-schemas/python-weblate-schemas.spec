#
# spec file for package python-weblate-schemas
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


%define skip_python2 1
Name:           python-weblate-schemas
Version:        2022.1
Release:        0
Summary:        A collection of schemas used by Weblate
License:        MIT
URL:            https://weblate.org/
Source:         https://files.pythonhosted.org/packages/source/w/weblate_schemas/weblate_schemas-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/WeblateOrg/weblate_schemas/commit/1465933db1bd10dd34e7373b1f0b6693d708277e tests: fix invalid test data
Patch0:         test-data.patch
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonschema
BuildArch:      noarch
%python_subpackages

%description
This module contains schemas used in Weblate exports.

%prep
%setup -q -n weblate_schemas-%{version}
%autopatch -p1
sed -i -e '/pytest-runner/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/weblate_schemas
%{python_sitelib}/weblate_schemas-%{version}*-info

%changelog
