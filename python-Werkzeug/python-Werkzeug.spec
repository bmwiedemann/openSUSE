#
# spec file for package python-Werkzeug
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Werkzeug
Version:        0.15.5
Release:        0
Summary:        The Swiss Army knife of Python web development
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://werkzeug.pocoo.org/
Source:         https://files.pythonhosted.org/packages/source/W/Werkzeug/Werkzeug-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001_create_a_thread_to_reap_death_process.patch bsc#954591
Patch0:         0001_create_a_thread_to_reap_death_process.patch
%if 0%{?suse_version} < 1500
BuildRequires:  python
%endif
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Recommends:     python-termcolor
Recommends:     python-watchdog
Obsoletes:      python-Werkzeug-doc < %{version}
Provides:       python-Werkzeug-doc = %{version}

%ifpython2
Provides:       %{oldpython}-werkzeug = %{version}
Obsoletes:      %{oldpython}-werkzeug < %{version}
%endif
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
%setup -q -n Werkzeug-%{version}
sed -i "1d" examples/manage-{i18nurls,simplewiki,shorty,couchy,cupoftee,webpylike,plnt,coolmagic}.py # Fix non-executable scripts
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%pytest

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
