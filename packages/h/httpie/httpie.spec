#
# spec file for package httpie
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


%define _mtime 1730482196
%define _commit 2105caa

%define primary_python python311
%define python_version 3.11

Name:           httpie
Version:        3.2.4
Release:        0
Summary:        CLI, cURL-like tool for humans
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Utilities
URL:            https://httpie.org/
Source:         cli-%{version}.%{_mtime}.%{_commit}.tar.gz
Source1:        http.1
BuildRequires:  %{primary_python}
BuildRequires:  %{primary_python}-Jinja2
BuildRequires:  %{primary_python}-PySocks
BuildRequires:  %{primary_python}-PyYAML
BuildRequires:  %{primary_python}-Pygments >= 2.5.2
BuildRequires:  %{primary_python}-Werkzeug
BuildRequires:  %{primary_python}-charset-normalizer >= 2.0.0
BuildRequires:  %{primary_python}-defusedxml >= 0.6.0
BuildRequires:  %{primary_python}-flake8
BuildRequires:  %{primary_python}-flake8-comprehensions
BuildRequires:  %{primary_python}-flake8-deprecated
BuildRequires:  %{primary_python}-multidict >= 4.7.0
BuildRequires:  %{primary_python}-pip
BuildRequires:  %{primary_python}-pyOpenSSL
BuildRequires:  %{primary_python}-pytest
BuildRequires:  %{primary_python}-pytest-cov
BuildRequires:  %{primary_python}-pytest-httpbin >= 0.0.6
BuildRequires:  %{primary_python}-pytest-lazy-fixture >= 0.0.6
BuildRequires:  %{primary_python}-pytest-mock
BuildRequires:  %{primary_python}-requests >= 2.22.0
BuildRequires:  %{primary_python}-requests-toolbelt >= 0.9.1
BuildRequires:  %{primary_python}-responses
BuildRequires:  %{primary_python}-rich >= 9.10.0
BuildRequires:  %{primary_python}-setuptools
BuildRequires:  %{primary_python}-twine
BuildRequires:  %{primary_python}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       %{primary_python}
Requires:       %{primary_python}-PySocks
Requires:       %{primary_python}-Pygments >= 2.5.2
Requires:       %{primary_python}-charset-normalizer >= 2.0.0
Requires:       %{primary_python}-defusedxml >= 0.6.0
Requires:       %{primary_python}-multidict >= 4.7.0
Requires:       %{primary_python}-pip
Requires:       %{primary_python}-requests >= 2.22.0
Requires:       %{primary_python}-requests-toolbelt >= 0.9.1
Requires:       %{primary_python}-rich >= 9.10.0
Requires:       %{primary_python}-setuptools
Provides:       %{primary_python}-httpie = %{version}
Provides:       python3-httpie = %{version}
Obsoletes:      %{primary_python}-httpie < 2.3.0
Obsoletes:      python3-httpie < 2.3.0
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
HTTPie consists of a single "http" command designed for debugging and
interaction with HTTP servers, RESTful APIs, and web services.

It allows for issuing arbitrary HTTP requests and displays colorized
responses.

%prep
%setup -q -n cli-%{version}.%{_mtime}.%{_commit}
#drop shebang
sed -i -e '/^#!\//, 1d' httpie/__main__.py

%build
export LC_CTYPE=en_US.UTF-8
python%{python_version} setup.py build

%install
export LC_CTYPE=en_US.UTF-8
python%{python_version} setup.py install --root=%{buildroot}
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
# temporarily disable tests that fail with python 3.11
#pytest --deselect=tests/test_uploads.py --deselect=tests/test_plugins_cli.py
pytest --deselect=tests/test_uploads.py --deselect=tests/test_plugins_cli.py --deselect=tests/test_compress.py --deselect=tests/test_binary.py tests -v

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
