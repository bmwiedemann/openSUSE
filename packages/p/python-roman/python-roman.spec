#
# spec file for package python-roman
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-roman
Version:        5.0
Release:        0
Summary:        Integer to Roman numerals converter
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/roman
Source:         https://files.pythonhosted.org/packages/source/r/roman/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
This module converts from and to Roman numerals. It can convert numbers from
1 to 4999 and understands the common shortcuts (IX == 9), but not illegal ones (MIM == 1999).

%prep
%setup -q -n %{packagename}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/%{packagename}
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative %{packagename}

%pre
%python_libalternatives_reset_alternative %{packagename}

%post
%python_install_alternative %{packagename}

%postun
%python_uninstall_alternative %{packagename}

%check
%pyunittest discover -v src

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE.txt
%pycache_only %{python_sitelib}/__pycache__/%{packagename}*pyc
%{python_sitelib}/%{packagename}-%{version}.dist-info
%{python_sitelib}/%{packagename}.py
%python_alternative %{_bindir}/roman

%if 0%{?sle_version} > 0 && 0%{?sle_version} <= 150200
%{_prefix}/lib/python2.7/site-packages/%{packagename}.py*
%endif

%changelog
