#
# spec file for package python-py3dns
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-py3dns
Version:        3.2.0
Release:        0
Summary:        Python module for DNS (Domain Name Service)
License:        CNRI-Python
Group:          Development/Languages/Python
URL:            https://launchpad.net/py3dns
Source:         https://files.pythonhosted.org/packages/source/p/py3dns/py3dns-%{version}.tar.gz
Patch0:         python3-py3dns-handle-absent-resolv.patch
Patch1:         python3-py3dns-py3_friendly_warning.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package contains a module (dnslib) that implements a DNS
(Domain Name Server) client, plus additional modules that define some
symbolic constants used by DNS (dnstype, dnsclass, dnsopcode).

%prep
%setup -q -n py3dns-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Unable to run tests without resolv.conf and net
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test.py

%files %{python_files}
%license LICENSE
%doc README* CHANGES
%{python_sitelib}/*

%changelog
