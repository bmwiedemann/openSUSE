#
# spec file for package python-speaklater
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-speaklater
Version:        1.3
Release:        0
Summary:        Implements a lazy string for python useful for use with gettext
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/mitsuhiko/speaklater
Source:         https://files.pythonhosted.org/packages/source/s/speaklater/speaklater-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A module that provides lazy strings for translations.  Basically you
get an object that appears to be a string but changes the value every
time the value is evaluated based on a callable you provide.

%prep
%setup -q -n speaklater-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/speaklater.py
%pycache_only %{python_sitelib}/__pycache__/speaklater*
%{python_sitelib}/speaklater-%{version}*-info

%check
# no testsuite found

%changelog
