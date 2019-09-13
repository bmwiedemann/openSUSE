#
# spec file for package python-python-twitter
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
%ifarch %{ix86}
# (type(resp[0]) is int) is not true for python 2.7, as it is long
%define skip -k 'not (testGetFollowerIDsPaged or testGetFollowersIDs or testGetRetweeters)'
%endif
%define oldpython python
Name:           python-python-twitter
Version:        3.5
Release:        0
Summary:        A Python wrapper around the Twitter API
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/bear/python-twitter
Source:         https://github.com/bear/python-twitter/archive/v%{version}.tar.gz
# https://github.com/bear/python-twitter/commit/f7eb83d9dca3ba0ee93e629ba5322732f99a3a30
# fix test for PostDirectMessage endpoint with new data
Patch0:         python-python-twitter-fix-test.patch
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
# /SECTION
BuildRequires:  fdupes
Requires:       python-future
Requires:       python-requests
Requires:       python-requests-oauthlib
%ifpython2
Provides:       %{oldpython}-twitter = %{version}
Obsoletes:      %{oldpython}-twitter < %{version}
%endif
BuildArch:      noarch

%python_subpackages

%description
This library provides a Python interface for the Twitter API <https://dev.twitter.com/>.

Twitter <http://twitter.com> provides a service that allows people to connect via the web, IM, and SMS. Twitter exposes a web services API
which can be used using this library.

%prep
%setup -q -n python-twitter-%{version}
%patch0 -p1
sed -i -e '/^#!\/usr\/bin\/env/d' twitter/*.py
echo %skip

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest %{?skip}

%files %{python_files}
%doc AUTHORS.rst CHANGES README.rst GAE.rst NOTICE
%license LICENSE
%{python_sitelib}/*

%changelog
