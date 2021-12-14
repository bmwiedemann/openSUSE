#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define         skip_python2 1
# current astropy in TW requires python >= 3.7
%define         skip_python36 1
Name:           python-asdf%{psuffix}
Version:        2.8.3
Release:        0
Summary:        Python tools to handle ASDF files
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/asdf-format/asdf
Source0:        https://files.pythonhosted.org/packages/source/a/asdf/asdf-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module importlib-resources >= 3 if %python-base < 3.9}
BuildRequires:  %{python_module jmespath >= 0.6.2}
BuildRequires:  %{python_module jsonschema >= 3.0.2}
BuildRequires:  %{python_module numpy >= 1.10}
BuildRequires:  %{python_module packaging >= 16.0}
BuildRequires:  %{python_module semantic_version >= 2.8}
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.10
Requires:       python-jmespath >= 0.6.2
Requires:       python-jsonschema >= 3.0.2
Requires:       python-numpy >= 1.10
Requires:       python-packaging >= 16.0
Requires:       python-semantic_version >= 2.8
%if %python_version_nodots < 39
Requires:       python-importlib-resources >= 3
%endif
Recommends:     python-lz4 >= 0.10
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module asdf}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module gwcs}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest-openfiles >= 0.3.1}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
%python_subpackages

%description
The Advanced Scientific Data Format (ASDF) is a next-generation
interchange format for scientific data. This package contains the
Python implementation of the ASDF Standard.

%prep
%setup -q -n asdf-%{version}
sed -i -e '/^#!\//, 1d' asdf/extern/RangeHTTPServer.py
chmod a-x asdf/extern/RangeHTTPServer.py
sed -i 's/\r$//' asdf/tests/data/example_schema.json
chmod a-x asdf/tests/data/example_schema.json
# https://github.com/asdf-format/asdf/pull/1036
sed -i 's/isSet/is_set/' asdf/tests/httpserver.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/asdftool
%{python_expand #
sed -i -e 's|^#!/usr/bin/env python|#!%{__$python}|' %{buildroot}%{$python_sitelib}/asdf/reference_files/generate/generate
%fdupes %{buildroot}%{$python_sitelib}
}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
# import everything from the source directory because of collection conflicts with buildroot
export PYTHONPATH=":x"
%pytest --import-mode=append
%endif

%post
%python_install_alternative asdftool

%postun
%python_uninstall_alternative asdftool

%if !%{with test}
%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/asdftool
%{python_sitelib}/asdf
%{python_sitelib}/asdf-%{version}*-info
%{python_sitelib}/pytest_asdf
%endif

%changelog
