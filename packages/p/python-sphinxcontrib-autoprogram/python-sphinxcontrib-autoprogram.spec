#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%global short_name autoprogram
# https://github.com/sphinx-contrib/autoprogram/commit/457822502b71a449d97dfece63e77dbee910b581
%define skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sphinxcontrib-%{short_name}
Version:        0.1.7
Release:        0
Summary:        Sphinx extension to document CLI programs
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-contrib/%{short_name}
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 1.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.2
Requires:       python-six
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sphinxcontrib-autoprogram}
BuildRequires:  %{python_module sphinxcontrib-websupport >= 1.0.1}
%endif
%python_subpackages

%description
This contrib extension, sphinxcontrib.autoprogram, provides an automated way to
document CLI programs. It scans arparser.ArgumentParser object, and then expands
it into a set of .. program:: and .. option:: directives.

%package        doc
Summary:        Documentation for sphinxcontrib-autoprogram
Group:          Documentation/HTML

%description    doc
This package contains the documentation for the package
python-sphinxcontrib-autoprogram.

%prep
%autosetup -n %{short_name}-%{version} -p1

%build
%if !%{with test}
%python_build

# need to set PYTHONPATH, otherwise the build won't find the extension in the
# subfolder
export PYTHONPATH=$(pwd)
# set PYTHON so that the sphinx Makefile picks up the correct python version
%{python_expand export PYTHON=$python}
sphinx-build -b html -d doc/_build/doctrees doc doc/_build/html

# remove inventory file, not needed for the documentation
rm doc/_build/html/objects.inv
%endif

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export PYTHONPATH='doc'
%pyunittest sphinxcontrib/autoprogram.py
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%endif

%if !%{with test}
%files %{python_files doc}
%license LICENSE
%doc doc/_build/html/*
%endif

%changelog
