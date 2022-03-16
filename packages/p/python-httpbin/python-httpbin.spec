#
# spec file for package python-httpbin
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-httpbin
Version:        0.7.0+git20181107.f8ec666
Release:        0
Summary:        HTTP Request and Response Service
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Runscope/httpbin
Source:         python-httpbin-%{version}.tar.xz
# https://github.com/postmanlabs/httpbin/pull/555
Patch0:         werkzeug.patch
# Based on https://github.com/postmanlabs/httpbin/pull/553
Patch1:         fix-setup-py.patch
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module MarkupSafe}
BuildRequires:  %{python_module Werkzeug >= 2.0}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module flasgger}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module itsdangerous}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli
Requires:       python-Flask
Requires:       python-MarkupSafe
Requires:       python-Werkzeug >= 2.0
Requires:       python-blinker
Requires:       python-decorator
Requires:       python-flasgger
Requires:       python-gevent
Requires:       python-itsdangerous
Requires:       python-six
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
%autosetup -p1

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
