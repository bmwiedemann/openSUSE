#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-asdf%{psuffix}
Version:        2.13.0
Release:        0
Summary:        Python tools to handle ASDF files
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/asdf-format/asdf
Source0:        https://files.pythonhosted.org/packages/source/a/asdf/asdf-%{version}.tar.gz
# PATCH-FIX-UPSTREAM  asdf-pr1185+pr1203-fix-jsonschema.patch gh#asdf-format/asdf#1185, gh#asdf-format/asdf#1203
Patch0:         asdf-pr1185+pr1203-fix-jsonschema.patch
# PATCH-FIX-UPSTREAM  asdf-pr1214-installed-packages.patch gh#asdf-format/asdf#1214
Patch1:         asdf-pr1214-installed-packages.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.10
Requires:       python-asdf-standard >= 1.0.1
Requires:       python-asdf-transform-schemas >= 0.2.2
Requires:       python-jmespath >= 0.6.2
Requires:       python-jsonschema >= 4.0.1
Requires:       python-numpy >= 1.10
Requires:       python-packaging >= 16.0
Requires:       python-semantic_version >= 2.8
%if 0%{?python_version_nodots} < 39
Requires:       python-importlib-resources >= 3
%endif
Recommends:     python-lz4 >= 0.10
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module asdf = %{version}}
BuildRequires:  %{python_module astropy >= 5.0.4}
BuildRequires:  %{python_module gwcs}
BuildRequires:  %{python_module lz4}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest-openfiles >= 0.3.1}
BuildRequires:  %{python_module pytest-remotedata}
BuildRequires:  %{python_module pytest-sugar}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
%python_subpackages

%description
The Advanced Scientific Data Format (ASDF) is a next-generation
interchange format for scientific data. This package contains the
Python implementation of the ASDF Standard.

%prep
%autosetup -p1 -n asdf-%{version}
sed -i -e '/^#!\//, 1d' asdf/extern/RangeHTTPServer.py
chmod a-x asdf/extern/RangeHTTPServer.py
sed -i 's/\r$//' asdf/tests/data/example_schema.json
chmod a-x asdf/tests/data/example_schema.json
sed -i '/addopts/ s/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/asdftool
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
# remove source directory in order to avoid import mismatches
mv asdf asdf.moved
%pytest --pyargs asdf --remote-data=none
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
