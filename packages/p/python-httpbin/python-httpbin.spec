#
# spec file for package python-httpbin
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


%define modname httpbin
%{?sle15_python_module_pythons}
Name:           python-httpbin
Version:        0.10.2
Release:        0
Summary:        HTTP Request and Response Service
License:        MIT
URL:            https://github.com/psf/httpbin
Source:         https://files.pythonhosted.org/packages/source/h/%{modname}/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#psf/httpbin#40
Patch0:         remove-six.patch
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Flask >= 2.2.4}
BuildRequires:  %{python_module Werkzeug >= 2.0}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module flasgger}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli
Requires:       python-Flask >= 2.2.4
Requires:       python-Werkzeug >= 2.2.2
Requires:       python-decorator
Requires:       python-flasgger
Requires:       python-gevent
BuildArch:      noarch
%python_subpackages

%description
httpbin(1): HTTP Request & Response Service

Testing an HTTP Library can become difficult sometimes.
RequestBin is fantastic for testing POST requests, but doesn't let
you control the response. This exists to cover
all kinds of HTTP scenarios. Additional endpoints are being considered.

All endpoint responses are JSON-encoded.

%prep
%autosetup -p1 -n %{modname}-%{version}
# we are running CPython, let us use Brotli instead of brotlicffi (they should be compatible)
sed -i 's/brotlicffi/brotli/' httpbin/filters.py

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/httpbin
%{python_sitelib}/httpbin-%{version}.dist-info

%changelog
