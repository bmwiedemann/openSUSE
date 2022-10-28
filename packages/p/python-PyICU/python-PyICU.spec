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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global modname PyICU
Name:           python-%{modname}
Version:        2.10.2
Release:        0
Summary:        Python Extension Wrapping the ICU C++ API
License:        MIT
Group:          Development/Libraries/Python
URL:            https://gitlab.pyicu.org
Source0:        https://files.pythonhosted.org/packages/source/P/PyICU/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
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
%setup -q -n %{modname}-%{version}

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -v -k 'not (testAcceptLanguage or testAcceptLanguageFromHTTP)' -rs test

%files %{python_files}
%license LICENSE
%doc CHANGES CREDITS README.md
%{python_sitearch}/*

%changelog
