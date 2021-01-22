#
# spec file for package python-eliot
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
%define skip_python2 1
Name:           python-eliot
Version:        1.12.0
Release:        0
Summary:        A logging system that tells the user why something happened
License:        Apache-2.0
URL:            https://github.com/itamarst/eliot/
Source0:        https://github.com/itamarst/eliot/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module boltons >= 19.0.1}
BuildRequires:  %{python_module cffi >= 1.1.2}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module hypothesis >= 3.47.0}
BuildRequires:  %{python_module pyrsistent >= 0.11.8}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 40}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sphinx_rtd_theme}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module twine >= 1.12.1}
BuildRequires:  %{python_module yapf}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  ((python3-aiocontextvars and python3-base < 3.7) or (python36-aiocontextvars and python36-base))
Requires:       python-boltons >= 19.0.1
Requires:       python-pyrsistent >= 0.11.8
Requires:       python-six
%if 0%{?python_version_nodots} < 37
Requires:       python-aiocontextvars
%endif
Requires:       python-zope.interface
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
eliot is a Python logging system that outputs causal chains of actions: actions can spawn other actions,
and eventually they either succeed or fail.
The resulting logs tell the story of what the software did: what happened, and what caused it.

%prep
%setup -q -n eliot-%{version}

%build
export LC_CTYPE=en_US.UTF-8
%python_build

%install
export LC_CTYPE=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/eliot-prettyprint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative eliot-prettyprint

%postun
%python_uninstall_alternative eliot-prettyprint

%check
# skip prettyprint as it needs the binary to execute
# test_parse_stream is too slow in obs
%pytest eliot/tests -k 'not (prettyprint or test_parse_stream)'

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/eliot-prettyprint
%{python_sitelib}/*

%changelog
