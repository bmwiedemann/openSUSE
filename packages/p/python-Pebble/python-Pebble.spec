#
# spec file for package python-Pebble
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-Pebble
Version:        5.2.0
Release:        0
Summary:        Threading and multiprocessing eye-candy for Python
License:        LGPL-3.0-only
URL:            https://github.com/noxdafox/pebble
Source:         https://files.pythonhosted.org/packages/source/p/pebble/pebble-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Pebble provides an API to manage threads and processes within an application.
It wraps Python’s standard library threading and multiprocessing objects.

%prep
%setup -q -n pebble-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Seems to actually deadlock
%pytest -k 'not test_pool_deadlock_stop_cancel'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pebble
%{python_sitelib}/[Pp]ebble-%{version}.dist-info

%changelog
