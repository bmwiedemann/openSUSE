#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define modname zdaemon
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        4.4
Release:        0
Summary:        Daemon process control library and tools
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/zdaemon
Source:         https://files.pythonhosted.org/packages/source/z/zdaemon/%{modname}-%{version}.tar.gz
Patch0:         obs-timeout.patch
BuildRequires:  %{python_module ZConfig}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zc.customdoctests}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ZConfig
Requires(post): update-alternatives
Requires(preun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
zdaemon is a Python package which provides APIs for managing
applications run as daemons. Its principal use to date has been to
manage the application server and storage server daemons for Zope / ZEO,
although it is not limited to running Python-based applications

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1
# remove unwanted shebang
sed -i '1 { /^#!/ d }' src/zdaemon/tests/nokill.py
rm -rf src/zdaemon.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/zdaemon

%check
# https://github.com/zopefoundation/zdaemon/issues/28
sed -i 's:import mock:from unittest import mock:' src/zdaemon/tests/testuser.py
pushd src
%pyunittest discover -v

%post
%python_install_alternative zdaemon

%postun
%python_uninstall_alternative zdaemon

%files %{python_files}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%python_alternative %{_bindir}/zdaemon
%{python_sitelib}/*

%changelog
