#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-Werkzeug%{psuffix}
Version:        2.2.3
Release:        0
Summary:        The Swiss Army knife of Python web development
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://werkzeug.palletsprojects.com
Source:         https://files.pythonhosted.org/packages/source/W/Werkzeug/Werkzeug-%{version}.tar.gz
# PATCH-FIX-UPSTREAM moved_root.patch bsc#[0-9]+ mcepl@suse.com
# this patch makes things totally awesome
Patch1:         moved_root.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
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
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-MarkupSafe >= 2.1.1
Recommends:     python-termcolor
Recommends:     python-watchdog
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
%autosetup -p1 -n Werkzeug-%{version}

sed -i "1d" examples/manage-{i18nurls,simplewiki,shorty,couchy,cupoftee,webpylike,plnt,coolmagic}.py # Fix non-executable scripts

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export LANG=en_US.UTF-8
# workaround pytest 6.2 (like https://github.com/pallets/werkzeug/commit/16718f461d016b88b6457d3ef63816b7df1f0d1f, but shorter)
%pytest -k 'not (dev_server or test_reloader_sys_path or test_chunked_encoding or test_basic or test_server or test_ssl or test_http_proxy or test_500_error or test_untrusted_host or test_double_slash_path or test_wrong_protocol or test_content_type_and_length or test_multiple_headers_concatenated or test_multiline_header_folding or test_exclude_patterns)'
%endif

%if ! %{with test}
%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/werkzeug
%{python_sitelib}/Werkzeug-%{version}*-info
%endif

%changelog
