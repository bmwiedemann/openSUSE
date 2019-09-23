#
# spec file for package python-cursive
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
Name:           python-cursive
Version:        0.2.2
Release:        0
Summary:        Cursive implements OpenStack-specific validation of digital signatures
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://www.openstack.org/
Source:         https://pypi.io/packages/source/c/cursive/cursive-%{version}.tar.gz
BuildRequires:  %{python_module castellan >= 0.4.0}
BuildRequires:  %{python_module cryptography >= 1.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module oslo.i18n >= 2.1.0}
BuildRequires:  %{python_module oslo.serialization >= 1.10.0}
BuildRequires:  %{python_module oslo.utils >= 3.16.0}
BuildRequires:  %{python_module pbr >= 1.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# test requirements
BuildRequires:  %{python_module Sphinx >= 1.2.1}
BuildRequires:  %{python_module openstackdocstheme}
BuildRequires:  %{python_module oslotest >= 1.10.0}
BuildRequires:  %{python_module python-subunit >= 0.0.18}
BuildRequires:  %{python_module reno >= 1.8.0}
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  %{python_module testtools >= 1.4.0}
Requires:       python-castellan >= 0.4.0
Requires:       python-cryptography >= 1.0
Requires:       python-oslo.i18n >= 2.1.0
Requires:       python-oslo.log >= 1.14.0
Requires:       python-oslo.serialization >= 1.10.0
Requires:       python-oslo.utils >= 3.16.0
Requires:       python-pbr >= 1.6
BuildArch:      noarch

%python_subpackages

%description
Cursive implements OpenStack-specific validation of digital signatures.
As OpenStack continues to mature, robust security controls become increasingly
critical. The cursive project contains code extracted from various OpenStack
projects for verifying digital signatures. Additional capabilities will be
added to this project in support of various security features.

%prep
%setup -q -n cursive-%{version}

%build
%python_build

%install
%python_install

%check
%{python_expand rm -rf .testrepository
$python setup.py testr
}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/*

%changelog
