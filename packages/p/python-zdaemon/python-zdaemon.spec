#
# spec file for package python-zdaemon
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


%{?sle15_python_module_pythons}
%define modname zdaemon
Name:           python-%{modname}
Version:        5.0
Release:        0
Summary:        Daemon process control library and tools
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zdaemon
Source:         https://files.pythonhosted.org/packages/source/z/zdaemon/%{modname}-%{version}.tar.gz
Patch0:         obs-timeout.patch
BuildRequires:  %{python_module ZConfig}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zc.customdoctests}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ZConfig
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
zdaemon is a Python package which provides APIs for managing
applications run as daemons. Its principal use to date has been to
manage the application server and storage server daemons for Zope / ZEO,
although it is not limited to running Python-based applications

%prep
%autosetup -p1 -n %{modname}-%{version}
# remove unwanted shebang
sed -i '1 { /^#!/ d }' src/zdaemon/tests/nokill.py
rm -rf src/zdaemon.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/zdaemon

%check
pushd src
%pyunittest discover -v
popd

%post
%python_install_alternative zdaemon

%postun
%python_uninstall_alternative zdaemon

%files %{python_files}
%license LICENSE.txt
%doc README.rst CHANGES.rst
%python_alternative %{_bindir}/zdaemon
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
