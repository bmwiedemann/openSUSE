#
# spec file for package httpie
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


Name:           httpie
Version:        3.2.2
Release:        0
Summary:        CLI, cURL-like tool for humans
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Utilities
URL:            https://httpie.org/
Source:         https://github.com/jakubroztocil/httpie/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        http.1
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PySocks
BuildRequires:  python3-PyYAML
BuildRequires:  python3-Pygments >= 2.5.2
BuildRequires:  python3-Werkzeug
BuildRequires:  python3-charset-normalizer >= 2.0.0
BuildRequires:  python3-defusedxml >= 0.6.0
BuildRequires:  python3-flake8
BuildRequires:  python3-flake8-comprehensions
BuildRequires:  python3-flake8-deprecated
BuildRequires:  python3-multidict >= 4.7.0
BuildRequires:  python3-pip
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-httpbin >= 0.0.6
BuildRequires:  python3-pytest-lazy-fixture >= 0.0.6
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-requests >= 2.22.0
BuildRequires:  python3-requests-toolbelt >= 0.9.1
BuildRequires:  python3-responses
BuildRequires:  python3-rich >= 9.10.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-twine
BuildRequires:  python3-wheel
Requires:       python3-PySocks
Requires:       python3-Pygments >= 2.5.2
Requires:       python3-charset-normalizer >= 2.0.0
Requires:       python3-defusedxml >= 0.6.0
Requires:       python3-multidict >= 4.7.0
Requires:       python3-pip
Requires:       python3-requests >= 2.22.0
Requires:       python3-requests-toolbelt >= 0.9.1
Requires:       python3-rich >= 9.10.0
Requires:       python3-setuptools
Provides:       python%{python_version}-httpie = 3.2.2
Provides:       python3-httpie = 3.2.2
Obsoletes:      python%{python_version}-httpie < 2.3.0
Obsoletes:      python3-httpie < 2.3.0
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
%fdupes %{buildroot}%{_prefix}/lib/python%{python_version}/site-packages
install -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/http.1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
# Install bash & fish completion, credit to Fedora for providing this: https://src.fedoraproject.org/rpms/httpie/blob/rawhide/f/httpie.spec
cp -a extras/httpie-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/http
ln -s ./http %{buildroot}%{_datadir}/bash-completion/completions/https
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d/
cp -a extras/httpie-completion.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/http.fish
ln -s ./http.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/https.fish

%check
export LC_CTYPE=en_US.UTF-8
# disable tests that fail on OBS with [Errno -3] Temporary failure in name resolution
#pytest --deselect=tests/test_uploads.py --deselect=tests/test_plugins_cli.py
pytest --deselect=tests/test_uploads.py --deselect=tests/test_plugins_cli.py tests -v

%files
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%{_bindir}/http
%{_bindir}/https
%{_bindir}/%{name}
%{python_sitelib}/httpie*
%{_mandir}/man1/http.1%{?ext_man}
%{_mandir}/man1/https.1%{?ext_man}
%{_mandir}/man1/%{name}.1%{?ext_man}
# co-own the entire directory structures, again credit to Fedora: https://src.fedoraproject.org/rpms/httpie/blob/rawhide/f/httpie.spec
%{_datadir}/bash-completion/
%{_datadir}/fish/

%changelog
