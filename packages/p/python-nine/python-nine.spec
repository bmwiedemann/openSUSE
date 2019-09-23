#
# spec file for package python-nine
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
%bcond_without test
Name:           python-nine
Version:        1.0.0
Release:        0
Summary:        Python 2 / 3 compatibility, like six, but favouring Python 3
License:        SUSE-Public-Domain
Group:          Development/Languages/Python
URL:            https://github.com/nandoflorestan/nine
Source:         https://files.pythonhosted.org/packages/source/n/nine/nine-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
python-nine is python-six "turned around": whereas python-six used
to make python2 idioms work in python3, python-nine makes python3
idioms work in python2.

%prep
%setup -q -n nine-%{version}

%build

%python_build

%install
%python_install

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/*

%changelog
