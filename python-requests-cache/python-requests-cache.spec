#
# spec file for package python-requests-cache
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
Name:           python-requests-cache
Version:        0.5.0
Release:        0
Summary:        Persistent cache for requests library
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/reclosedev/requests-cache
Source:         https://files.pythonhosted.org/packages/source/r/requests-cache/requests-cache-%{version}.tar.gz
BuildRequires:  %{python_module requests >= 1.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 1.1.0
BuildArch:      noarch
%python_subpackages

%description
Requests-cache is a transparent persistent cache for requests_ (version >= 1.1.0) library.

It can be useful when you are creating some simple data scraper with constantly
changing parsing logic or data format, and don't want to redownload pages or
write complex error handling and persistence.

Requests-cache ignores all cache headers, it just caches the data for the
time you specify.

If you need library which knows how to use HTTP headers and status codes,
take a look at `httpcache <https://github.com/Lukasa/httpcache>`_ and
`CacheControl <https://github.com/ionrock/cachecontrol>`_.

%prep
%setup -q -n requests-cache-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
