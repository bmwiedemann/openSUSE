#
# spec file for package python-botocore
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
# Multibuild: some tests need to find botocore in the system sitelib
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-botocore%{?psuffix}
Version:        1.34.122
Release:        0
Summary:        Python interface for AWS
License:        Apache-2.0
URL:            https://github.com/boto/botocore
Source:         https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       (python-jmespath >= 0.7.1 with python-jmespath < 2.0.0)
Requires:       (python-python-dateutil >= 2.1 with python-python-dateutil < 3.0.0)
BuildArch:      noarch
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-botocore < %{version}
%endif
%if %{with test}
BuildRequires:  %{python_module botocore = %{version}}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module urllib3 < 2.1}
BuildRequires:  procps
%endif
%python_subpackages

%description
A low-level interface to a growing number of Amazon Web Services.

%prep
%setup -q -n botocore-%{version}

# remove bundled cacert.pem
rm botocore/cacert.pem

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# TODO: Figure out whether integration tests are possible offline
# no_bare_six_imports: we "fixed" that above.
%pytest %{?jobs:-n 4} --ignore tests/integration -k "not six"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/botocore/
%{python_sitelib}/botocore-%{version}.dist-info
%endif

%changelog
