#
# spec file for package python-ez_setup
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
Name:           python-ez_setup
Version:        0.9
Release:        0
Summary:        Contains ez_setup.py and distribute_setup.py
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/ActiveState/ez_setup
Source:         https://files.pythonhosted.org/packages/source/e/ez_setup/ez_setup-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%ifpython2
# also provides distribute_setup.py
Conflicts:      python-mockito < 0.5.3
%endif
BuildArch:      noarch
%python_subpackages

%description
setup.py of several Python projects blindly import the setuptools bootstrap
module ez_setup.py without realizing that it is usually not installed in the
user's machine. This causes much trouble. Include ez_setup.py (and
distribute_setup.py) as a installable Python package so users can do
easy_install ez_setup troublesome_package as a workaround.

%prep
%setup -q -n ez_setup-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%doc NEWS.txt README.rst
%{python_sitelib}/*

%changelog
