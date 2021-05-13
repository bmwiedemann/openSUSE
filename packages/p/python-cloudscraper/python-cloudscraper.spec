#
# spec file for package python-cloudscraper
#
# Copyright (c) 2021 SUSE LLC
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
%define modname cloudscraper
%define skip_python2 1
Name:           python-cloudscraper
Version:        1.2.58
Release:        0
Summary:        A Python module to bypass Cloudflare's anti-bot page
License:        MIT
URL:            https://github.com/venomous/cloudscraper
Source:         https://github.com/VeNoMouS/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Js2Py}
BuildRequires:  %{python_module pyparsing >= 2.4.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.9.2}
BuildRequires:  %{python_module requests-toolbelt >= 0.9.1}
BuildRequires:  %{python_module responses}
BuildRequires:  nodejs-default
# /SECTION
BuildRequires:  fdupes
Requires:       python-pyparsing >= 2.4.7
Requires:       python-requests >= 2.9.2
Requires:       python-requests-toolbelt >= 0.9.1
BuildArch:      noarch
%python_subpackages

%description
A Python module to bypass Cloudflare's anti-bot page.

%prep
%autosetup -p1 -n cloudscraper-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
