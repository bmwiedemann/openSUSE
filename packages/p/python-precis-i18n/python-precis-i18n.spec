#
# spec file for package python-precis-i18n
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

%{?sle15_python_module_pythons}
%define _name   precis_i18n
Name:           python-precis-i18n
Version:        1.1.0
Release:        0
Summary:        Internationalised Usernames and Passwords
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/byllyfish/precis_i18n
Source:         https://github.com/byllyfish/precis_i18n/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-unicodedata2
BuildArch:      noarch
Provides:       python-%{_name} = %{version}-%{release}
%python_subpackages

%description
The PRECIS framework makes internationalised user names and
passwords safer for use by applications. PRECIS profiles transform
unicode strings into a canonical form, suitable for comparison.

This module implements the PRECIS Framework as described in:
 - PRECIS Framework: Preparation, Enforcement, and Comparison of
   Internationalized Strings in Application Protocols (RFC 8264).
 - Preparation, Enforcement, and Comparison of Internationalized
   Strings Representing Usernames and Passwords (RFC 8265).
 - Preparation, Enforcement, and Comparison of Internationalized
   Strings Representing Nicknames (RFC 8266).

%prep
%autosetup -n %{_name}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
%pyunittest -v

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{python_sitelib}/%{_name}/
%{python_sitelib}/%{_name}-%{version}.dist-info

%changelog
