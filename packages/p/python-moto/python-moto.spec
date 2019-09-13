#
# spec file for package python-moto
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-moto
Version:        1.3.8
Release:        0
Summary:        Library to mock out the boto library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/spulec/moto
Source:         https://files.pythonhosted.org/packages/source/m/moto/moto-%{version}.tar.gz
Patch0:         unpin-reqs.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.7.3
Requires:       python-Werkzeug
Requires:       python-aws-xray-sdk >= 0.93
Requires:       python-boto >= 2.36.0
Requires:       python-boto3 >= 1.6.16
Requires:       python-botocore >= 1.12.13
Requires:       python-cfn-lint
Requires:       python-cryptography >= 2.3.0
Requires:       python-docker >= 2.5.1
Requires:       python-jsondiff >= 1.1.2
Requires:       python-mock
Requires:       python-pyaml
Requires:       python-python-dateutil >= 2.1
Requires:       python-python-jose
Requires:       python-pytz
Requires:       python-requests >= 2.5
Requires:       python-responses >= 0.9.0
Requires:       python-six > 1.9
Requires:       python-xmltodict
Recommends:     python-jsonpickle
Requires(post): update-alternatives
Requires(preun): update-alternatives
Recommends:     python-flask
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.7.3}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module aws-xray-sdk >= 0.93}
BuildRequires:  %{python_module boto >= 2.36.0}
BuildRequires:  %{python_module boto3 >= 1.6.16}
BuildRequires:  %{python_module botocore >= 1.12.13}
BuildRequires:  %{python_module cfn-lint}
BuildRequires:  %{python_module cryptography >= 2.3.0}
BuildRequires:  %{python_module docker >= 2.5.1}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module jsondiff >= 1.1.2}
BuildRequires:  %{python_module jsonpickle}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module python-jose}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.5}
BuildRequires:  %{python_module responses >= 0.9.0}
BuildRequires:  %{python_module six > 1.9}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module xmltodict}
BuildRequires:  python-backports.tempfile
# /SECTION
%ifpython2
Requires:       python-backports.tempfile
%endif
%python_subpackages

%description
A library that allows your python tests to mock out the boto
library.

%prep
%setup -q -n moto-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/moto_server

# Tests require a network connection
# %%check
# %%{python_expand export PYTHONPATH=%%{buildroot}%%{$python_sitelib}
# nosetests-%%{$python_bin_suffix} -sv ./tests/
# }

%post
%python_install_alternative moto_server

%preun
%python_uninstall_alternative moto_server

%files %{python_files}
%doc AUTHORS.md README.md
%license LICENSE
%python_alternative %{_bindir}/moto_server
%{python_sitelib}/*

%changelog
