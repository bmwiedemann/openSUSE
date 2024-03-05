#
# spec file for package python-tld
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


Name:           python-tld
Version:        0.13
Release:        0
Summary:        URL top level domain (TLD) extraction module
License:        GPL-2.0-only OR MPL-1.1 OR LGPL-2.1-or-later
URL:            https://github.com/barseghyanartur/tld
Source:         https://files.pythonhosted.org/packages/source/t/tld/tld-%{version}.tar.gz
# PATCH-FIX-OPENSUSE skip_internet_tests.patch
Patch0:         skip_internet_tests.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This module extracts the top level domain (TLD) from the URL given.
A list of TLD names is taken from Mozillas public suffix list:
<https://publicsuffix.org/list/effective_tld_names.dat>

%prep
%autosetup -p1 -n tld-%{version}
# https://github.com/barseghyanartur/tld/issues/75

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/update-tld-names
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative update-tld-names

%postun
%python_uninstall_alternative update-tld-names

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE_GPL2.0.txt LICENSE_LGPL_2.1.txt LICENSE_MPL_1.1.txt
%python_alternative %{_bindir}/update-tld-names
%{python_sitelib}/tld
%{python_sitelib}/tld-%{version}.dist-info

%changelog
