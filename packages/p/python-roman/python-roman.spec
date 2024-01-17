#
# spec file for package python-roman
#
# Copyright (c) 2023 SUSE LLC
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


%define packagename roman
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{?sle15_python_module_pythons}
Name:           python-roman
Version:        3.3
Release:        0
Summary:        Integer to Roman numerals converter
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/roman
Source:         https://files.pythonhosted.org/packages/source/r/roman/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module converts from and to Roman numerals. It can convert numbers from
1 to 4999 and understands the common shortcuts (IX == 9), but not illegal ones (MIM == 1999).

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/%{packagename}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative %{packagename}

%post
%python_install_alternative %{packagename}

%postun
%python_uninstall_alternative %{packagename}

%check
%pyunittest discover -v src

%files %{python_files}
%doc CHANGES.txt
%pycache_only %{python_sitelib}/__pycache__/%{packagename}*
%{python_sitelib}/*egg-info/
%{python_sitelib}/%{packagename}.py
%python_alternative %{_bindir}/roman

%if 0%{?sle_version} > 0 && 0%{?sle_version} <= 150200
%{_prefix}/lib/python2.7/site-packages/%{packagename}.py*
%endif

%changelog
