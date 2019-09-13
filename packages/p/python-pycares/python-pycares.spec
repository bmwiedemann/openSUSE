#
# spec file for package python-pycares
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pycares
Version:        3.0.0
Release:        0
Summary:        Python interface for c-ares
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/saghul/pycares
Source:         https://files.pythonhosted.org/packages/source/p/pycares/pycares-%{version}.tar.gz
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
Requires:       python-cffi
Recommends:     python-idna
%python_subpackages

%description
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously

%prep
%setup -q -n pycares-%{version}
rm -Rf

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitearch}/*

%changelog
