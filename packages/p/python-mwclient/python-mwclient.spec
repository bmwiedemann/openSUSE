#
# spec file for package python-mwclient
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
Name:           python-mwclient
Version:        0.10.1
Release:        0
Summary:        MediaWiki API client
License:        MIT
URL:            https://github.com/btongminh/mwclient
Source:         https://files.pythonhosted.org/packages/source/m/mwclient/mwclient-%{version}.tar.gz
# PATCH-FIX-UPSTREAM demock.patch gh#mwclient/mwclient#276 mcepl@suse.com
# Remove dependency on mock
Patch0:         demock.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module responses >= 0.3.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests-oauthlib
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
MediaWiki API client

%prep
%autosetup -p1 -n mwclient-%{version}

sed -i -e '/^addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install --ignore-installed
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/mwclient-%{version}*-info
%{python_sitelib}/mwclient

%changelog
