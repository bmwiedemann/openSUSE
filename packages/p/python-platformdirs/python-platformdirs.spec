#
# spec file for package python-platformdirs
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
%define skip_python2 1
Name:           python-platformdirs
Version:        2.4.1
Release:        0
Summary:        Module for determining appropriate platform-specific dirs
License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Source:         https://files.pythonhosted.org/packages/source/p/platformdirs/platformdirs-%{version}.tar.gz
# PATCH-FIX-OPENSUSE no-furo.patch mcepl@suse.com
# https://github.com/pradyunsg/furo/discussions/148#discussioncomment-1125486
# Don't use furo Sphinx theme
Patch0:         no-furo.patch
BuildRequires:  %{python_module appdirs == 1.4.4}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module pytest-mock >= 3.6}
BuildRequires:  %{python_module setuptools_scm >= 5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx >= 4
BuildRequires:  python3-sphinx-autodoc-typehints >= 1.12
BuildArch:      noarch
%python_subpackages

%description
A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".

%package -n %{name}-doc
Summary:        Documentation files for %{name}
Group:          Documentation/Other

%description -n %{name}-doc
HTML Documentation and examples for %{name}.

%prep
%autosetup -p1 -n platformdirs-%{version}

%build
%python_build

PYTHONPATH=src sphinx-build -b html docs/ docs/build/html
rm -r docs/build/html/.{buildinfo,doctrees}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
rm tox.ini
%pytest

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.txt
%{python_sitelib}/platformdirs
%{python_sitelib}/platformdirs-%{version}*-info

%files -n %{name}-doc
%doc docs/build/html/

%changelog
