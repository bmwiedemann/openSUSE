#
# spec file for package httpie
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           httpie
Version:        1.0.3
Release:        0
Summary:        CLI, cURL-like tool for humans
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Utilities
URL:            https://httpie.org/
Source:         https://github.com/jakubroztocil/httpie/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        http.1
BuildRequires:  %{python_module Pygments >= 2.1.3}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.18.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments >= 2.1.3
Requires:       python-requests >= 2.18.4
Suggests:       python-argparse >= 1.2.1
Suggests:       python-colorama >= 0.2.4
Provides:       httpie
BuildArch:      noarch
%python_subpackages

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
%python_build

%install
export LC_CTYPE=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/http.1

%check
export LC_CTYPE=en_US.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_version}

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE
%python3_only %{_bindir}/http
%{python_sitelib}/*
%{_mandir}/man1/http.1%{ext_man}

%changelog
