#
# spec file for package python-PyKMIP
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without  libalternatives
Name:           python-PyKMIP
Version:        0.11.0
Release:        0
Summary:        KMIP v11 library
License:        Apache-2.0
URL:            https://github.com/OpenKMIP/PyKMIP
Source:         https://files.pythonhosted.org/packages/source/p/pykmip/pykmip-%{version}.tar.gz
# https://github.com/OpenKMIP/PyKMIP/issues/668
Patch0:         python-PyKMIP-no-mock.patch
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-SQLAlchemy
Requires:       python-cryptography
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The standard
is governed by the `Organization for the Advancement of Structured Information
Standards`_ (OASIS). PyKMIP supports a subset of features in versions
1.0 - 1.2 of the KMIP specification.

%prep
%autosetup -p1 -n pykmip-%{version}
# Not needed, we use Python 3.4+ only
sed -i '/"enum-compat",/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pykmip-server
%python_group_libalternatives pykmip-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest kmip/tests/unit

%pre
%python_libalternatives_reset_alternative pykmip-server

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/kmip
%{python_sitelib}/[Pp]y[Kk][Mm][Ii][Pp]-%{version}.dist-info
%python_alternative %{_bindir}/pykmip-server

%changelog
