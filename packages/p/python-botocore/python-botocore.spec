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
# Multibuild: some tests need to find botocore in the system sitelib
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-botocore%{?psuffix}
Version:        1.29.26
Release:        0
Summary:        Python interface for AWS
License:        Apache-2.0
URL:            https://github.com/boto/botocore
Source:         https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jmespath < 1.0.0
Requires:       python-jmespath >= 0.7.1
Requires:       python-python-dateutil < 3.0.0
Requires:       python-python-dateutil >= 2.1
Requires:       python-requests
Requires:       python-six
Requires:       python-urllib3 < 1.27
Requires:       python-urllib3 >= 1.25.4
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module botocore = %{version}}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest >= 6.2.5}
BuildRequires:  procps
%endif
%python_subpackages

%description
A low-level interface to a growing number of Amazon Web Services.

%prep
%setup -q -n botocore-%{version}

# remove bundled cacert.pem
rm botocore/cacert.pem
# remove bundled 3rd party Python modules
rm -r botocore/vendored/
# fix all imports:
sed -i 's/from botocore\.vendored //' botocore/*.py tests/functional/*.py tests/integration/*.py tests/unit/*.py
sed -i 's/botocore.vendored.requests.model.Response/requests.model.Response/' botocore/endpoint.py
sed -i 's/botocore\.vendored\.//' botocore/*.py tests/functional/*.py tests/integration/*.py tests/unit/*.py

%if !%{with test}
%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# TODO: Figure out whether integration tests are possible offline
# no_bare_six_imports: we "fixed" that above.
%pytest --ignore tests/integration -k "not no_bare_six_imports"
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/botocore/
%{python_sitelib}/botocore-%{version}-py*.egg-info
%endif

%changelog
