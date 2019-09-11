#
# spec file for package python-autoupgrade-ng
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
Name:           python-autoupgrade-ng
Version:        0.3.0
Release:        0
Summary:        Automatic upgrade of PyPI packages
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/vuolter/autoupgrade
Source:         https://files.pythonhosted.org/packages/source/a/autoupgrade-ng/autoupgrade-ng-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-pip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
Automatic upgrade of PyPI packages from within Python scripts

The upgrade will be unattended and the python script will be restarted.

Old methods are still supported; you can accomplish the same task calling:

%prep
%setup -q -n autoupgrade-ng-%{version}

%build
%python_build
dos2unix README.rst

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
