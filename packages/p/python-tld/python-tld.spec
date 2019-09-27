#
# spec file for package python-tld
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-tld
Version:        0.9.6
Release:        0
Summary:        URL top level domain (TLD) extraction module
License:        MPL-1.1 OR GPL-2.0-only OR LGPL-2.1-only
Group:          Development/Languages/Python
Url:            https://github.com/barseghyanartur/tld
Source:         https://files.pythonhosted.org/packages/source/t/tld/tld-%{version}.tar.gz
# PATCH-FIX-OPENSUSE skip_internet_tests.patch
Patch0:         skip_internet_tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Faker}
BuildRequires:  %{python_module factory_boy}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module six >= 1.9}
BuildRequires:  %{python_module tox}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six >= 1.9
BuildArch:      noarch

%python_subpackages

%description
This module extracts the top level domain (TLD) from the URL given.
A list of TLD names is taken from Mozillas public suffix list:
<https://publicsuffix.org/list/effective_tld_names.dat>

%prep
%setup -q -n tld-%{version}
#sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' src/tld/bin/update-tld-names
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand chmod -x %{buildroot}%{$python_sitelib}/tld/res/old/effective_tld_names-2015-07-19.dat.txt}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE_GPL2.0.txt LICENSE_LGPL_2.1.txt
%python3_only %{_bindir}/update-tld-names
%{python_sitelib}/*

%changelog
