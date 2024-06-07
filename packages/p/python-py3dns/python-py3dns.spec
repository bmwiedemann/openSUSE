#
# spec file for package python-py3dns
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


Name:           python-py3dns
Version:        4.0.2
Release:        0
Summary:        Python module for DNS (Domain Name Service)
License:        CNRI-Python
Group:          Development/Languages/Python
URL:            https://launchpad.net/py3dns
Source:         https://files.pythonhosted.org/packages/source/p/py3dns/py3dns-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package contains a module (dnslib) that implements a DNS
(Domain Name Server) client, plus additional modules that define some
symbolic constants used by DNS (dnstype, dnsclass, dnsopcode).

%prep
%autosetup -p1 -n py3dns-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Unable to run tests without resolv.conf and net
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test.py

%files %{python_files}
%license LICENSE
%doc README* CHANGES
%{python_sitelib}/DNS
%{python_sitelib}/py3dns-%{version}.dist-info

%changelog
