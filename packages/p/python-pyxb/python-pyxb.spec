#
# spec file for package python-pyxb
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


%define realnam PyXB
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyxb
Version:        1.2.6
Release:        0
Summary:        Python class code generator based on XMLSchemas
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://pyxb.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pyxb/%{realnam}-%{version}.tar.gz
Patch0:         PyXB-unbundle-six.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       python-xml
BuildArch:      noarch
%python_subpackages

%description
PyXB is a pure Python package that generates Python code for classes that correspond to data structures defined by XMLSchema.
In concept it is similar to JAXB for Java and CodeSynthesis XSD for C++.

%prep
%setup -q -n %{realnam}-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc NOTICE PKG-INFO README.txt
%{python_sitelib}/pyxb/
%{python_sitelib}/PyXB-%{version}-*.egg-info
%python3_only %{_bindir}/pyxbdump
%python3_only %{_bindir}/pyxbgen
%python3_only %{_bindir}/pyxbwsdl

%changelog
