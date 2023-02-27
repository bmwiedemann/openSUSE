#
# spec file for package python-service_identity
#
# Copyright (c) 2023 SUSE LLC
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


%define oname   service_identity
Name:           python-service_identity
Version:        21.1.0
Release:        0
Summary:        Service identity verification for pyOpenSSL
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pyca/service_identity
# no tests in upstream tarball
Source:         https://github.com/pyca/service_identity/archive/%{version}.tar.gz
BuildRequires:  %{python_module attrs >= 19.1.0}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module idna}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL >= 0.14}
BuildRequires:  %{python_module pyasn1-modules}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.1.0
Requires:       python-cryptography
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
Requires:       python-six
Recommends:     python-idna
Recommends:     python-pyOpenSSL
BuildArch:      noarch
%ifpython2
Requires:       python-ipaddress
%endif
%python_subpackages

%description
service_identity aspires to give you all the tools you need for
verifying whether a certificate is valid for the intended purposes.

In the simplest case, this means host name verification. However,
service_identity implements RFC 6125 fully and plans to add other
relevant RFCs too.

%prep
%setup -q -n service-identity-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}*-info

%changelog
