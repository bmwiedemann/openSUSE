#
# spec file for package python-bindep
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-bindep
Version:        2.8.1
Release:        0
Summary:        Binary dependency utility
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://docs.openstack.org/infra/bindep
Source:         https://files.pythonhosted.org/packages/source/b/bindep/bindep-%{version}.tar.gz
BuildRequires:  %{python_module Parsley}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
Requires:       python-Parsley
Requires:       python-distro
Requires:       python-pbr
BuildArch:      noarch

%python_subpackages
%description
Bindep is a tool for checking the presence of binary packages needed to
use an application / library. It started life as a way to make it easier to set
up a development environment for OpenStack projects. While OpenStack depends
heavily on `pip` for installation of Python dependencies, some dependencies are
not Python based, and particularly for testing, some dependencies have to be
installed before `pip` can be used - such as `virtualenv` and `pip` itself.

%prep
%setup -q -n bindep-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bindep

%post
%{python_install_alternative bindep}

%postun
%python_uninstall_alternative bindep

## %check
## python setup.py testr

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst ChangeLog AUTHORS NEWS.rst
%python_alternative %{_bindir}/bindep
%{python_sitelib}/*

%changelog
