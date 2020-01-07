#
# spec file for package python-pomegranate
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pomegranate
Version:        0.12.0
Release:        0
Summary:        A graphical models library for Python
License:        MIT
URL:            https://github.com/jmschrei/pomegranate
Source:         https://github.com/jmschrei/pomegranate/archive/v%{version}.tar.gz#/pomegranate-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.22.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy >= 1.8.0}
BuildRequires:  %{python_module numpy-devel >= 1.8.0}
BuildRequires:  %{python_module scipy >= 0.17.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-joblib >= 0.9.0b4
Requires:       python-networkx >= 2.0
Requires:       python-numpy >= 1.8.0
Requires:       python-PyYAML
Requires:       python-scipy >= 0.17.0
# SECTION test requirements
BuildRequires:  %{python_module joblib >= 0.9.0b4}
BuildRequires:  %{python_module networkx >= 2.0}
BuildRequires:  %{python_module numpy >= 1.8.0}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module scipy >= 0.17.0}
# /SECTION
%python_subpackages

%description
Pomegranate is a graphical models library for Python, implemented in Cython for speed.

%package        devel
Summary:        Development files for %{name}
Requires:       python-pomegranate = %{version}

%description    devel
Pomegranate is a graphical models library for Python, implemented in Cython for speed.

This package provides development files needed to run software that depends on
Pomegranate.

%prep
%setup -q -n pomegranate-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/pomegranate/
%{python_sitearch}/pomegranate-%{version}-py*.egg-info
%exclude %{python_sitearch}/pomegranate/*.c
%exclude %{python_sitearch}/pomegranate/*/*.c

%files %{python_files devel}
%license LICENSE
%{python_sitearch}/pomegranate/*.c
%{python_sitearch}/pomegranate/*/*.c

%changelog
