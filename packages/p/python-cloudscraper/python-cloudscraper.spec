#
# spec file for package python-cloudscraper
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


%define modname cloudscraper
%{?sle15_python_module_pythons}
Name:           python-cloudscraper
Version:        3.0.0
Release:        0
Summary:        A Python module to bypass Cloudflare's anti-bot page
License:        MIT
URL:            https://github.com/venomous/cloudscraper
Source:         https://github.com/VeNoMouS/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Brotli >= 1.1.0}
BuildRequires:  %{python_module Js2Py >= 0.74}
BuildRequires:  %{python_module certifi >= 2024.2.2}
BuildRequires:  %{python_module pyOpenSSL >= 24.0.0}
BuildRequires:  %{python_module pycryptodome >= 3.20.0}
BuildRequires:  %{python_module pyparsing >= 3.1.0}
BuildRequires:  %{python_module pytest >= 8.0.0}
BuildRequires:  %{python_module requests >= 2.31.0}
BuildRequires:  %{python_module requests-toolbelt >= 1.0.0}
BuildRequires:  %{python_module responses >= 0.24.0}
BuildRequires:  %{python_module websocket-client >= 1.7.0}
BuildRequires:  nodejs-default
# /SECTION
BuildRequires:  fdupes
Requires:       nodejs-default
Requires:       python-Brotli >= 1.1.0
Requires:       python-Js2Py >= 0.74
Requires:       python-certifi >= 2024.2.2
Requires:       python-pyOpenSSL >= 24.0.0
Requires:       python-pycryptodome >= 3.20.0
Requires:       python-pyparsing >= 3.1.0
Requires:       python-requests >= 2.31.0
Requires:       python-requests-toolbelt >= 1.0.0
Requires:       python-websocket-client >= 1.7.0
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
donttest+=" or test_403_handling"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/cloudscraper
%{python_sitelib}/cloudscraper-%{version}.dist-info

%changelog
