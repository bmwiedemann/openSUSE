#
# spec file for package python-botocore
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-botocore
Version:        1.17.56
Release:        0
Summary:        Python interface for AWS
License:        Apache-2.0
URL:            https://github.com/boto/botocore
Source:         https://files.pythonhosted.org/packages/source/b/botocore/botocore-%{version}.tar.gz
Patch0:         hide_py_pckgmgmt.patch
BuildRequires:  %{python_module docutils >= 0.10}
BuildRequires:  %{python_module jmespath < 1.0.0}
BuildRequires:  %{python_module jmespath >= 0.7.1}
BuildRequires:  %{python_module python-dateutil <= 3.0.0}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urllib3 < 1.26}
BuildRequires:  %{python_module urllib3 >= 1.20}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-docutils >= 0.10
Requires:       python-jmespath < 1.0.0
Requires:       python-jmespath >= 0.7.1
Requires:       python-python-dateutil <= 3.0.0
Requires:       python-python-dateutil >= 2.1
Requires:       python-requests
Requires:       python-six
Requires:       python-urllib3 < 1.26
Requires:       python-urllib3 >= 1.20
BuildArch:      noarch
%if 0%{?suse_version} <= 1315
# We need the ssl module, which is delivers by python and not python-base
BuildRequires:  python
%endif
# SECTION Testing requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
A low-level interface to a growing number of Amazon Web Services.

%prep
%setup -q -n botocore-%{version}
%patch0 -p1
# remove bundled cacert.pem
rm botocore/cacert.pem
# remove bundled 3rd party Python modules
rm -r botocore/vendored/
# fix all imports:
sed -i 's/from botocore\.vendored //' botocore/*.py tests/functional/*.py tests/integration/*.py tests/unit/*.py
sed -i 's/botocore.vendored.requests.model.Response/requests.model.Response/' botocore/endpoint.py
sed -i 's/botocore\.vendored\.//' botocore/*.py tests/functional/*.py tests/integration/*.py tests/unit/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix} -v tests/unit

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/botocore/
%{python_sitelib}/botocore-%{version}-py*.egg-info

%changelog
