#
# spec file for package python-mwclient
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-mwclient
Version:        0.11.0
Release:        0
Summary:        MediaWiki API client
License:        MIT
URL:            https://github.com/mwclient/mwclient
Source:         https://files.pythonhosted.org/packages/source/m/mwclient/mwclient-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module responses >= 0.3.0}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module wheel}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests-oauthlib
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
