#
# spec file for package python-txtorcon
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


%{?!python_module:%define python_module() python-%{**} %{!?skip_python3:python3-%{**}}}
Name:           python-txtorcon
Version:        19.0.0
Release:        0
Summary:        Twisted-based asynchronous Tor control protocol implementation
License:        MIT
Group:          Development/Languages/Python
URL:            https://txtorcon.readthedocs.org
Source:         https://files.pythonhosted.org/packages/source/t/txtorcon/txtorcon-%{version}.tar.gz
# https://github.com/meejah/txtorcon/commit/5d7ebea5086f361efe7f14aea58e512a04b401f3
Patch0:         python-txtorcon-methods-are-bytes.patch
BuildRequires:  %{python_module setuptools >= 36.2}
BuildRequires:  fdupes
BuildRequires:  python-ipaddress
BuildRequires:  python-rpm-macros
Requires:       python-Automat
Requires:       python-GeoIP >= 1.2.9
Requires:       python-Twisted >= 15.5.0
Requires:       python-incremental
Requires:       python-zope.interface >= 3.6.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Automat}
BuildRequires:  %{python_module GeoIP >= 1.2.9}
BuildRequires:  %{python_module Twisted >= 15.5.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface >= 3.6.1}
# /SECTION
%ifpython2
Requires:       python-ipaddress >= 1.0.16
%endif
%python_subpackages

%description
Twisted-based asynchronous Tor control protocol implementation. Includes
unit-tests, examples, state-tracking code and configuration abstraction.

%prep
%setup -q -n txtorcon-%{version}
%patch0 -p1

sed -i '/data_files/,/\]\,/s/^/#/' setup.py

%build
%python_build

%install
%python_install
# remove the tests from distribution
%python_expand rm -rf %{buildroot}%{$python_sitelib}/test/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# looks more like integration tests
%pytest -k 'not (test_real_addr or test_return_geoip_object)'

%files %{python_files}
%license LICENSE docs/*.rst
%{python_sitelib}/*

%changelog
