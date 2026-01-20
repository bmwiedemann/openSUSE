#
# spec file for package python-apns2
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-apns2
Version:        0.7.2
Release:        0
Summary:        Python library for the HTTP/2 Apple Push Notification Service
License:        MIT
URL:            https://github.com/Pr0Ger/PyAPNs2
Source0:        https://files.pythonhosted.org/packages/source/a/apns2/apns2-%{version}.tar.gz
# Subset of https://github.com/Pr0Ger/PyAPNs2/pull/122.patch
Patch0:         pr_122.patch
# PATCH-FIX-OPENSUSE Based on gh#Pr0Ger/PyAPNs2#149, is gross
Patch1:         use-httpx.patch
# PATCH-FIX-UPSTREAM https://github.com/Pr0Ger/PyAPNs2/pull/163 Fix tests with pytest 9
Patch2:         pytest9.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyJWT >= 1.4.0
Requires:       python-cryptography >= 1.7.2
Requires:       python-h2
Requires:       python-httpx >= 0.13.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyJWT >= 1.4.0}
BuildRequires:  %{python_module cryptography >= 1.7.2}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module h2}
BuildRequires:  %{python_module httpx >= 0.13.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module respx}
# /SECTION
%python_subpackages

%description
A python library for interacting with the Apple Push Notification Service
via HTTP/2 protocol.

%prep
%autosetup -p1 -n apns2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/apns2
%{python_sitelib}/apns2-%{version}*-info

%changelog
