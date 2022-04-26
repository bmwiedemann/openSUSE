#
# spec file for package httpie
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


Name:           httpie
Version:        2.6.0
Release:        0
Summary:        CLI, cURL-like tool for humans
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Utilities
URL:            https://httpie.org/
Source:         https://github.com/jakubroztocil/httpie/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        http.1
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Pygments >= 2.5.2
BuildRequires:  python3-charset-normalizer >= 2.0.0
BuildRequires:  python3-defusedxml >= 0.6.0
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-httpbin
BuildRequires:  python3-requests >= 2.22.0
BuildRequires:  python3-requests-toolbelt >= 0.9.1
BuildRequires:  python3-responses
BuildRequires:  python3-setuptools
Requires:       python3-Pygments >= 2.5.2
Requires:       python3-charset-normalizer >= 2.0.0
Requires:       python3-defusedxml >= 0.6.0
Requires:       python3-requests >= 2.22.0
Requires:       python3-requests-toolbelt >= 0.9.1
Requires:       python3-responses
Provides:       python3-httpie = 2.3.0
Provides:       python38-httpie = 2.3.0
Obsoletes:      python3-httpie < 2.3.0
Obsoletes:      python38-httpie < 2.3.0
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
HTTPie consists of a single "http" command designed for debugging and
interaction with HTTP servers, RESTful APIs, and web services.

It allows for issuing arbitrary HTTP requests and displays colorized
responses.

%prep
%setup -q
#drop shebang
sed -i -e '/^#!\//, 1d' httpie/__main__.py

%build
export LC_CTYPE=en_US.UTF-8
%python3_build

%install
export LC_CTYPE=en_US.UTF-8
%python3_install
%fdupes %{buildroot}%{$python_sitelib}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/http.1

%check
export LC_CTYPE=en_US.UTF-8
# disable tests that fail on OBS with [Errno -3] Temporary failure in name resolution
#pytest --deselect=tests/test_uploads.py
pytest --deselect=tests/test_uploads.py tests -v

%files
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%{_bindir}/http
%{_bindir}/https
%{python_sitelib}/httpie*
%{_mandir}/man1/http.1%{?ext_man}

%changelog
