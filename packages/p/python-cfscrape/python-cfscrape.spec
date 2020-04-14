#
# spec file for package python-cfscrape
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-cfscrape
Version:        2.1.1
Release:        0
Summary:        Python module to bypass Cloudflare's anti-bot page
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Anorov/cloudflare-scrape
Source:         https://github.com/Anorov/cloudflare-scrape/archive/%{version}.tar.gz#/cloudflare-scrape-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sure}
BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros
Requires:       nodejs
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
A simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm
Under Attack Mode", or IUAM), implemented with Requests.

This can be useful if you wish to scrape or crawl a website protected with
Cloudflare. Cloudflare's anti-bot page currently just checks if the client
supports Javascript, though they may add additional techniques in the future.

Due to Cloudflare continually changing and hardening their protection page,
cfscrape requires Node.js to solve Javascript challenges. This allows the script
to easily impersonate a regular web browser without explicitly deobfuscating and
parsing Cloudflare's Javascript.

Note: This only works when regular Cloudflare anti-bots is enabled (the
"Checking your browser before accessing..." loading page). If there is a
reCAPTCHA challenge, you're out of luck. Thankfully, the Javascript check page
is much more common.

%prep
%setup -q -n cloudflare-scrape-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# test suite requires internet access
# %%check
# %%python_exec setup.py develop --user
# %%python_exec -m pytest -v tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
