#
# spec file for package python-Pebble
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
Name:           python-Pebble
Version:        4.3.10
Release:        0
Summary:        Threading and multiprocessing eye-candy for Python
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/noxdafox/pebble
Source:         https://files.pythonhosted.org/packages/source/P/Pebble/Pebble-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-futures
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%ifpython2
Requires:       python-futures
%endif
BuildArch:      noarch

%python_subpackages

%description
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.

%prep
%setup -q -n Pebble-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
