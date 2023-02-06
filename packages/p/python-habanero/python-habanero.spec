#
# spec file for package python-habanero
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


Name:           python-habanero
Version:        1.2.3
Release:        0
Summary:        Low Level Client for Crossref Search API
License:        MIT
URL:            https://github.com/sckott/habanero
Source:         https://files.pythonhosted.org/packages/source/h/habanero/habanero-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mark-vcr-tests.patch gh#sckott/habanero#114 mcepl@suse.com
# mark two more tests as vcr (to skip network access)
Patch0:         mark-vcr-tests.patch
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.7.0
Requires:       python-tqdm
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-vcr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module tqdm}
BuildRequires:  %{python_module vcrpy}
# /SECTION
%python_subpackages

%description
Low Level Client for Crossref Search API

%prep
%autosetup -p1 -n habanero-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not vcr'

%files %{python_files}
%doc Changelog.rst README.rst
%license LICENSE
%{python_sitelib}/habanero
%{python_sitelib}/habanero-%{version}*-info

%changelog
