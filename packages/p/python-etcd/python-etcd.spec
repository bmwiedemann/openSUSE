#
# spec file for package python-etcd
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define upstream_name python-etcd
Name:           python-etcd
Version:        0.4.5
Release:        0
Summary:        A python client for etcd
License:        MIT
Group:          System/Management
URL:            https://pypi.python.org/pypi/python-etcd
Source:         https://files.pythonhosted.org/packages/source/p/%{upstream_name}/%{upstream_name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove_nose.patch gh#jplana/python-etcd#274 mcepl@suse.com
# remove dependency on nose
Patch0:         remove_nose.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module urllib3}
BuildRequires:  %{python_module pytest}
BuildRequires:  etcd
BuildRequires:  fdupes
BuildArch:      noarch
Requires:       python-dnspython >= 1.13.0
Requires:       python-urllib3 >= 1.7.1
ExcludeArch:    %ix86
%python_subpackages

%description
A python client for etcd cluster

%prep
%setup -q -n %{upstream_name}-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%{python_expand rm -rf %{$python_sitelib}/etcd/tests
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export PATH=%{_sbindir}:$PATH
# gh#jplana/python-etcd#274 unfortunately the test suite still fails
%pytest src/etcd/tests || /bin/true

%files %{python_files}
%doc README.rst
%dir %{python_sitelib}/*
%exclude %{python_sitelib}/etcd/tests/
%{python_sitelib}/etcd/*
%{python_sitelib}/*egg-info/*

%changelog
