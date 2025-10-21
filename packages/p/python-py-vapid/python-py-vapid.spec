#
# spec file for package python-py-vapid
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


%bcond_without libalternatives
Name:           python-py-vapid
Version:        1.9.2
Release:        0
Summary:        VAPID header generation library
License:        MPL-2.0
URL:            https://github.com/mozilla-services/vapid
Source:         https://files.pythonhosted.org/packages/source/p/py-vapid/py_vapid-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#web-push-libs/vapid#108
Patch0:         remove-mock.patch
# PATCH-FIX-UPSTREAM Based on gh#web-push-libs/vapid#110
Patch1:         support-new-cryptography.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-cryptography >= 2.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography >= 2.5}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
VAPID header generation library.

%prep
%autosetup -p1 -n py_vapid-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/vapid
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative vapid

%files %{python_files}
%doc README.md README.rst
%license LICENSE
%python_alternative %{_bindir}/vapid
%{python_sitelib}/py[-_]vapid
%{python_sitelib}/py[-_]vapid-%{version}.dist-info

%changelog
