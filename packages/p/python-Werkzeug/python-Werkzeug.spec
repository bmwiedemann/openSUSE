#
# spec file for package python-Werkzeug
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-Werkzeug%{psuffix}
Version:        3.0.3
Release:        0
Summary:        The Swiss Army knife of Python web development
License:        BSD-3-Clause
URL:            https://werkzeug.palletsprojects.com
Source:         https://files.pythonhosted.org/packages/source/w/werkzeug/werkzeug-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
%if %{with test}
BuildRequires:  %{python_module Werkzeug = %{version}}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module ephemeral-port-reserve}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest >= 6.2.4}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xprocess}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  %{python_module watchdog >= 3.0.0}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-MarkupSafe >= 2.1.2
Recommends:     python-termcolor
Recommends:     python-watchdog >= 3.0.0
Obsoletes:      python-Werkzeug-doc < %{version}
Provides:       python-Werkzeug-doc = %{version}
BuildArch:      noarch
%python_subpackages

%description
Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).

%prep
%autosetup -p1 -n werkzeug-%{version}

sed -i "1d" examples/manage-{i18nurls,simplewiki,shorty,couchy,cupoftee,webpylike,plnt,coolmagic}.py # Fix non-executable scripts

%build
%pyproject_wheel

%install
%if ! %{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
# Tests that requires connection
donttest="test_basic"
donttest+=" or test_http_proxy"
donttest+=" or test_server"
donttest+=" or test_ssl_dev_cert"
donttest+=" or test_ssl_object"
donttest+=" or test_reloader_sys_path"
donttest+=" or test_chunked_request"
donttest+=" or test_streaming_close_response"
donttest+=" or test_streaming_chunked_response"
donttest+=" or test_streaming_chunked_truncation"
donttest+=" or test_untrusted_host"
donttest+=" or test_double_slash_path"
donttest+=" or test_500_error"
donttest+=" or test_wrong_protocol"
donttest+=" or test_content_type_and_length"
donttest+=" or test_multiple_headers_concatenated"
donttest+=" or test_multiline_header_folding"
%pytest -k "not ($donttest)"
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.md
%{python_sitelib}/werkzeug
%{python_sitelib}/werkzeug-%{version}.dist-info
%endif

%changelog
