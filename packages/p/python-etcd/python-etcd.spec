#
# spec file for package python-etcd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define upstream_name python-etcd
Name:           python-etcd
Version:        0.4.5
Release:        0
Summary:        A python client for etcd
License:        MIT 
Group:          System/Management
Url:            https://pypi.python.org/pypi/python-etcd
Source0:        https://pypi.python.org/packages/a1/da/616a4d073642da5dd432e5289b7c1cb0963cc5dde23d1ecb8d726821ab41/%{upstream_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
%ifpython2
Requires:       python-urllib3 >= 1.7.1
Requires:       python-dnspython >= 1.13.0
%else
Requires:       python3-urllib3 >= 1.7.1
Requires:       python3-dnspython >= 1.13.0
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
A python client for etcd cluster

%package test
Summary:        Unit tests
Group:          Development/Languages/Python
Requires:       %{name} == %{version}
Requires:       python-mock >= 1.0.1
Requires:       python-nose
Requires:       python-setuptools

%description test
Unit tests for etcd python client

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%python_build

%install
%python_install
%fdupes %{buildroot}

%check

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%dir %{python_sitelib}/*
%exclude %{python_sitelib}/etcd/tests/
%{python_sitelib}/etcd/*
%{python_sitelib}/*egg-info/*

%files %{python_files test}
%defattr(-,root,root,-)
%dir %{python_sitelib}/etcd/tests
%{python_sitelib}/etcd/tests/*

%changelog
