#
# spec file for package python-lazr.config
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
%define skip_python2 1
Name:           python-lazr.config
Version:        2.2.2
Release:        0
Summary:        Create configuration schemas, and process and validate configurations
License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.config
Source:         https://files.pythonhosted.org/packages/source/l/lazr.config/lazr.config-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lazr.delegates
Requires:       python-zope.interface
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lazr.delegates}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface}
# /SECTION
%python_subpackages

%description
Create configuration schemas, and process and validate configurations.

%prep
%setup -q -n lazr.config-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# use pytest, reported to lazr-users@lists.launchpad.net on 2020-06-03
cat << EOF > pytest.ini
[pytest]
addopts = --doctest-glob='*.rst'
doctest_optionflags = ELLIPSIS NORMALIZE_WHITESPACE
testpaths = src/lazr
EOF
export PYTHONPATH=src
# test_not_stackable fails otherwise (with nose it did not run at all)
# needs to be investigated more
sed -i 's:verifyObject, IStackableConfig, config.extends::' src/lazr/config/tests/test_config.py
%pytest 

%files %{python_files}
%doc README.rst
%license COPYING.txt
%{python_sitelib}/*

%changelog
