#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%define psuffix       %{nil}
%if "%{flavor}" != ""
%define psuffix      -%{flavor}
%endif
%global short_name autoprogram
# https://github.com/sphinx-contrib/autoprogram/commit/457822502b71a449d97dfece63e77dbee910b581
%define skip_python36 1
%define skip_python2 1
Name:           python-sphinxcontrib-%{short_name}%{psuffix}
Version:        0.1.7
Release:        0
%if "%{flavor}" == "" || "%{flavor}" == "test"
Summary:        Sphinx extension to document CLI programs
%endif
%if "%{flavor}" == "doc"
Summary:        Documentation for sphinxcontrib-autoprogram
%endif
License:        BSD-2-Clause
URL:            https://github.com/sphinx-contrib/%{short_name}
Source0:        %{URL}/archive/%{version}/python-sphinxcontrib-%{short_name}-%{version}.tar.gz
# https://github.com/sphinx-contrib/autoprogram/pull/25
Patch0:         python-sphinxcontrib-autoprogram-python310.patch
# PATCH-FIX-UPSTREAM skip-failing-test.patch gh#sphinx-contrib/autoprogram#54 mcepl@suse.com
# Switch off failing tests by the environmental variable SKIPTESTS
Patch1:         skip-failing-test.patch
BuildRequires:  %{python_module Sphinx >= 1.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.2
Requires:       python-six
BuildArch:      noarch
%if "%{flavor}" == "test"
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sphinxcontrib-autoprogram}
BuildRequires:  %{python_module sphinxcontrib-websupport >= 1.0.1}
%endif
%if "%{flavor}" == "doc"
BuildRequires:  %{python_module sphinxcontrib-autoprogram}
%endif
%python_subpackages

%if "%{flavor}" == "doc"
%description
This package contains the documentation for the package
python-sphinxcontrib-autoprogram.
%endif
%if "%{flavor}" == "" || "%{flavor}" == "test"
%description
This contrib extension, sphinxcontrib.autoprogram, provides an automated way to
document CLI programs. It scans arparser.ArgumentParser object, and then expands
it into a set of .. program:: and .. option:: directives.
%endif

%prep
%autosetup -n %{short_name}-%{version} -p1

%build
%if "%{flavor}" == ""
%python_build
%endif
%if "%{flavor}" == "doc"
sphinx-build -b html -d doc/_build/doctrees doc doc/_build/html
rm doc/_build/html/objects.inv
%endif

%install
%if "%{flavor}" == ""
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if "%{flavor}" == "test"
export SKIPTESTS=1
%pyunittest -v sphinxcontrib.autoprogram.suite
%endif

%if "%{flavor}" == ""
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/sphinxcontrib
%{python_sitelib}/sphinxcontrib_autoprogram-%{version}*-info
%{python_sitelib}/sphinxcontrib_autoprogram-%{version}*-nspkg.pth
%endif

%if "%{flavor}" == "doc"
%files %{python_files}
%license LICENSE
%doc doc/_build/html/*
%endif

%changelog
