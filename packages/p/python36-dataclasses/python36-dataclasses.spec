#
# spec file for package python-dataclasses
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


Name:           python36-dataclasses
Version:        0.8
Release:        0
Summary:        A backport of the dataclasses module for Python 3.6
License:        Apache-2.0
URL:            https://github.com/ericvsmith/dataclasses
Source:         https://files.pythonhosted.org/packages/source/d/dataclasses/dataclasses-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python36-setuptools
BuildRequires:  python36-testsuite
BuildArch:      noarch

%description
This is an implementation of PEP 557, Data Classes. It is a backport for Python 3.6.

%prep
%setup -q -n dataclasses-%{version}

%build
%{python36_build}

%install
%{python36_install}
%fdupes %{buildroot}%{python36_sitelib}

%check
PYTHONPATH=%{buildroot}%{python36_sitelib} python3.6 test/test_dataclasses.py -v

%files
%doc README.rst
%license LICENSE.txt
%{python36_sitelib}/dataclasses.py
%{python36_sitelib}/__pycache__/dataclasses*
%{python36_sitelib}/dataclasses-%{version}*-info

%changelog
