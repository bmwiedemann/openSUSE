#
# spec file for package python-cloudscraper
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


%define modname cloudscraper
%define skip_python2 1
Name:           python-cloudscraper
Version:        1.2.68
Release:        0
Summary:        A Python module to bypass Cloudflare's anti-bot page
License:        MIT
URL:            https://github.com/venomous/cloudscraper
Source:         https://github.com/VeNoMouS/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip broken test
donttest="test_getCookieString_challenge_js_challenge1_16_05_2020"
donttest+=" or test_bad_interpreter_js_challenge1_16_05_2020"
donttest+=" or test_bad_solve_js_challenge1_16_05_2020"
donttest+=" or test_Captcha_challenge_12_12_2019"
donttest+=" or test_reCaptcha_providers"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cloudscraper
%{python_sitelib}/cloudscraper-%{version}.dist-info

%changelog
