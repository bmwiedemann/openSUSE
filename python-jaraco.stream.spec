#
# spec file for package python-jaraco.stream
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


%define _name   jaraco.stream
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-jaraco.stream
Version:        3.0.3
Release:        0
Summary:        Routines for dealing with data streams
License:        MIT
URL:            https://github.com/jaraco/jaraco.stream
Source:         https://files.pythonhosted.org/packages/source/j/%{_name}/%{_name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-more-itertools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pytest}
# /SECTION
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module jaraco.packaging >= 8.2}
BuildRequires:  %{python_module pylons-sphinx-themes}
BuildRequires:  %{python_module rst.linker >= 1.9}
# /SECTION
%python_subpackages

%description
Routines for handling streaming data, including a set of generators
for loading gzip data on the fly.

%package     -n %{name}-doc
Summary:        Documentation files for %{name}
Provides:       %{python_module jaraco.stream-doc = %{version}}

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n %{_name}-%{version}
rm -rf jaraco.stream.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo

%check
#  work around for gh#pytest-dev/pytest#3396 until gh#pytest-dev/pytest#10088 lands in a pytest release
touch jaraco/__init__.py
cp -r %{python3_sitelib}/jaraco/* jaraco/
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/stream/
%{python_sitelib}/jaraco.stream-%{version}*-info

%files -n %{name}-doc
%doc build/sphinx/html

%changelog
