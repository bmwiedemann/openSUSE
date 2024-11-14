#
# spec file for package python-mockito
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-mockito
Version:        1.5.3
Release:        0
Summary:        Spying framework
License:        MIT
URL:            https://github.com/kaste/mockito-python
# https://github.com/kaste/mockito-python/issues/36
Source:         https://github.com/kaste/mockito-python/archive/%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module numpy >= 2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Requires:       python2-funcsigs
%endif
%python_subpackages

%description
Mockito is a spying framework originally based on the Java library with the same name.

%prep
%autosetup -p1 -n mockito-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGES.txt README.rst
%license LICENSE
%{python_sitelib}/mockito
%{python_sitelib}/mockito-%{version}.dist-info

%changelog
