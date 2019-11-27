#
# spec file for package python-python-consul
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
%bcond_without test
Name:           python-python-consul
Version:        1.1.0
Release:        0
Summary:        Python client for Consul (http://www.consulio/)
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/cablehead/python-consul
Source:         https://files.pythonhosted.org/packages/source/p/python-consul/python-consul-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module requests >= 2.0}
BuildRequires:  %{python_module six >= 1.4}
%endif
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pytest-twisted}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
Requires:       python-requests >= 2.0
Requires:       python-six >= 1.4
Suggests:       python-aiohttp
Suggests:       python-tornado
Suggests:       python-twisted
Suggests:       python-treq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
Python client for `Consul.io <http://www.consul.io/>`_

%prep
%setup -q -n python-consul-%{version}

%build

%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.rst LICENSE README.rst
%{python_sitelib}/*

%changelog
