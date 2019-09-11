#
# spec file for package python-chai
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
Name:           python-chai
Version:        1.1.2
Release:        0
Summary:        Mocking/stub framework for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/agoragames/chai
Source:         https://files.pythonhosted.org/packages/source/c/chai/chai-%{version}.tar.gz
BuildRequires:  %{python_module nose}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Chai provides an API for mocking/stubbing Python
objects, patterned after the Mocha library for Ruby.

%prep
%setup -q -n chai-%{version}
rm -rf chai.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec %{_bindir}/nosetests

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
