#
# spec file for package python-wsgi_intercept
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-wsgi_intercept
Version:        1.8.1
Release:        0
Summary:        Library for installing a WSGI application in place of a real URI for testing
License:        MIT
URL:            https://github.com/cdent/python3-wsgi-intercept
Source:         https://files.pythonhosted.org/packages/source/w/wsgi_intercept/wsgi_intercept-%{version}.tar.gz
Patch0:         httplib2.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module pytest >= 2.4}
BuildRequires:  %{python_module requests >= 2.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module urllib3 >= 1.11.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%if 0%{?_no_weakdeps}
Requires:       python-requests >= 2.0.1
%else
Recommends:     python-requests >= 2.0.1
%endif
%python_subpackages

%description
Testing a WSGI application normally involves starting a server at a local host
and port, then pointing your test code to that address. Instead, this library
lets you intercept calls to any specific host/port combination and redirect
them into a `WSGI application`_ importable by your test program.  Thus, you
can avoid spawning multiple processes or threads to test your Web app.

%prep
%setup -q -n wsgi_intercept-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
rm -r %{buildroot}%{python_sitelib}/wsgi_intercept/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export WSGI_INTERCEPT_SKIP_NETWORK=true
%pytest

%files %{python_files}
%{python_sitelib}/wsgi_intercept-%{version}-py%{py_ver}.egg-info
%{python_sitelib}/wsgi_intercept

%changelog
