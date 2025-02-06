#
# spec file for package python-trustme
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-trustme
Version:        1.2.1
Release:        0
Summary:        Fake CA provider for Python tests
License:        Apache-2.0 OR MIT
URL:            https://github.com/python-trio/trustme
Source:         https://files.pythonhosted.org/packages/source/t/trustme/trustme-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module service_identity}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 41.0.1
Requires:       python-idna
BuildArch:      noarch
%python_subpackages

%description
trustme is a Python package that provides a fake certificate
authority (CA) that can be used to generate "fake" TLS certs to use
in tests. The CA and certificates are fake in the sense of
https://martinfowler.com/bliki/TestDouble.html, that is, the trust
circle of the CA is limited to the test environment.

%prep
%autosetup -p1 -n trustme-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%license LICENSE.MIT
%license LICENSE.APACHE2
%doc README.rst
%{python_sitelib}/trustme
%{python_sitelib}/trustme-%{version}.dist-info

%changelog
