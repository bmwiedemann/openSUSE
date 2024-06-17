#
# spec file for package python-PyICU
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
%global modname PyICU
Name:           python-%{modname}
Version:        2.13.1
Release:        0
Summary:        Python Extension Wrapping the ICU C++ API
License:        MIT
Group:          Development/Libraries/Python
URL:            https://gitlab.pyicu.org
Source0:        https://files.pythonhosted.org/packages/source/P/PyICU/PyICU-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove_six.patch mcepl@suse.com
# Remove dependency on six
Patch0:         remove_six.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
Provides:       %{modname} = %{version}
Provides:       python-ICU = %{version}
Obsoletes:      python-ICU < 1.2
%python_subpackages

%description
Python extension wrapping IBM's International Components for Unicode C++
library (ICU).

%prep
%autosetup -p1 -n pyicu-%{version}

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%if 0%{?sle_version} && 0%{?sle_version} <= 150500
# The timezone package is not up to date
%pytest_arch -v -k 'not (testAcceptLanguage or testAcceptLanguageFromHTTP or testTransition)' -rs test
%else
%pytest_arch -v -k 'not (testAcceptLanguage or testAcceptLanguageFromHTTP)' -rs test
%endif

%files %{python_files}
%license LICENSE
%doc CHANGES CREDITS README.md
%{python_sitearch}/icu
%{python_sitearch}/PyICU-%{version}*-info

%changelog
