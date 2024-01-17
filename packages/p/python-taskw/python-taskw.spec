#
# spec file for package python-taskw
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-taskw
Version:        2.0.0
Release:        0
Summary:        Python bindings for taskwarrior
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ralphbean/taskw
Source:         https://files.pythonhosted.org/packages/source/t/taskw/taskw-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-kitchen
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       taskwarrior
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module kitchen}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  taskwarrior
# /SECTION
%python_subpackages

%description
Python bindings for your taskwarrior database.

%prep
%setup -q -n taskw-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
