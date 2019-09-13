#
# spec file for package python-Pykka
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
Name:           python-Pykka
Version:        2.0.0
Release:        0
Summary:        A Python implementation of the actor model
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.pykka.org/
Source:         https://files.pythonhosted.org/packages/source/P/Pykka/Pykka-%{version}.tar.gz
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pykka is a Python implementation of the `actor model
<http://en.wikipedia.org/wiki/Actor_model>`_. The actor model introduces some
rules to control the sharing of state and cooperation between execution
units, with which one can build concurrent applications.

%prep
%setup -q -n Pykka-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
