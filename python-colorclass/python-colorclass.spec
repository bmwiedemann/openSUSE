#
# spec file for package python-colorclass
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
Name:           python-colorclass
Version:        2.2.0
Release:        0
Summary:        ANSI text color library for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/Robpol86/colorclass
# https://github.com/Robpol86/colorclass/issues/25
Source:         https://github.com/Robpol86/colorclass/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Yet another ANSI color text library for Python. It provides "auto
colors" for dark/light terminals.

In Python 2.x, this library subclasses `unicode`, while on
Python 3.x, it subclasses `str`.

* Python 2.6, 2.7, PyPy, PyPy3, 3.3, 3.4, and 3.5 are supported

%prep
%setup -q -n colorclass-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_piped'

%files %{python_files}
%{python_sitelib}/*

%changelog
