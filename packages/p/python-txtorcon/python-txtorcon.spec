#
# spec file for package python-txtorcon
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


Name:           python-txtorcon
Version:        24.8.0
Release:        0
Summary:        Twisted-based asynchronous Tor control protocol implementation
License:        MIT
URL:            https://txtorcon.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/t/txtorcon/txtorcon-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 36.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Automat
Requires:       python-Twisted-tls >= 15.5.0
Requires:       python-cryptography
Requires:       python-zope.interface >= 3.6.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  lsof
BuildRequires:  %{python_module Automat}
BuildRequires:  %{python_module Twisted-tls >= 15.5.0}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module zope.interface >= 3.6.1}
%python_subpackages

%description
Twisted-based asynchronous Tor control protocol implementation. Includes
unit-tests, examples, state-tracking code and configuration abstraction.

%prep
%autosetup -p1 -n txtorcon-%{version}

sed -i '/data_files/,/\]\,/s/^/#/' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
# remove the tests from distribution
%python_expand rm -rf %{buildroot}%{$python_sitelib}/test/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# looks more like integration tests
# Async tests don't work with pytest gh#crossbario/autobahn-python#1235
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m twisted.trial test
}

%files %{python_files}
%license LICENSE docs/*.rst
%{python_sitelib}/txtorcon
%{python_sitelib}/txtorcon-%{version}.dist-info
%{python_sitelib}/twisted/plugins/*

%changelog
