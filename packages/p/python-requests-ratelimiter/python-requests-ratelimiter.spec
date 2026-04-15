#
# spec file for package python-requests-ratelimiter
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


Name:           python-requests-ratelimiter
Version:        0.9.3
Release:        0
Summary:        Easy rate-limiting for python requests
License:        MIT
URL:            https://github.com/JWCook/requests-ratelimiter
Source:         https://files.pythonhosted.org/packages/source/r/requests_ratelimiter/requests_ratelimiter-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pytest >= 8.3}
BuildRequires:  %{python_module pytest-xdist >= 3.1}
BuildRequires:  %{python_module requests >= 2.20}
BuildRequires:  %{python_module requests-cache >= 1.2.0}
BuildRequires:  %{python_module requests-mock >= 1.11}
BuildRequires:  %{python_module pyrate-limiter >= 4.1 and %python-pyrate-limiter < 5}
Requires:       python-requests >= 2.20
Requires:       (python-pyrate-limiter >= 4.1 and python-pyrate-limiter < 5)
%python_subpackages

%description
This package is a simple wrapper around pyrate-limiter that adds convenient integration with the requests library.

%prep
%autosetup -p1 -n requests_ratelimiter-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest --numprocesses=auto

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/requests_ratelimiter
%{python_sitelib}/requests_ratelimiter-%{version}.dist-info

%changelog

