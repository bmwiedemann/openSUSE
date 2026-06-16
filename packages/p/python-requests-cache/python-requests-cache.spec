#
# spec file for package python-requests-cache
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-requests-cache
Version:        1.3.2
Release:        0
Summary:        Persistent cache for requests library
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/requests-cache/requests-cache
Source:         https://github.com/requests-cache/requests-cache/archive/refs/tags/v%{version}.tar.gz#/requests-cache-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch1:         avoid-vacuum-in-transaction.patch
BuildRequires:  %{python_module hatchling >= 1.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 21.2
Requires:       python-cattrs >= 22.2
Requires:       python-platformdirs >= 2.5
Requires:       python-requests >= 2.22
Requires:       python-url-normalize >= 2.0
Requires:       python-urllib3 >= 1.25.5
Recommends:     python-itsdangerous >= 2.0
Recommends:     python-pyyaml >= 6.0.1
Recommends:     python-redis >= 3
Suggests:       python-boto3 >= 1.15
Suggests:       python-botocore >= 1.18
Suggests:       python-mongodb >= 3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 21.2}
BuildRequires:  %{python_module cattrs >= 22.2}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module httpbin}
BuildRequires:  %{python_module itsdangerous >= 2.0}
BuildRequires:  %{python_module platformdirs >= 2.5}
BuildRequires:  %{python_module psutil >= 5.0}
BuildRequires:  %{python_module pymongo >= 3}
BuildRequires:  %{python_module pytest >= 8.2}
BuildRequires:  %{python_module redis >= 3}
BuildRequires:  %{python_module requests >= 2.22}
BuildRequires:  %{python_module requests-mock >= 1.12}
BuildRequires:  %{python_module responses >= 0.19}
BuildRequires:  %{python_module rich >= 10.0}
BuildRequires:  %{python_module tenacity >= 8.0}
BuildRequires:  %{python_module time-machine >= 2.9}
BuildRequires:  %{python_module url-normalize >= 2.0}
BuildRequires:  %{python_module urllib3 >= 1.25.5}
BuildRequires:  redis
# /SECTION
%python_subpackages

%description
Requests-cache is a transparent persistent cache for requests_ library.

It can be useful when you are creating some simple data scraper with constantly
changing parsing logic or data format, and don't want to redownload pages or
write complex error handling and persistence.

Requests-cache ignores all cache headers, it just caches the data for the
time you specify.

If you need library which knows how to use HTTP headers and status codes,
take a look at `CacheControl <https://github.com/ionrock/cachecontrol>`_.

%prep
%autosetup -p1 -n requests-cache-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
gunicorn -b 127.0.0.1:8080 httpbin:app -k gevent &
%{_sbindir}/redis-server &
export HTTPBIN_URL=http://localhost:8080/
%pytest -k 'not (dynamodb or gridfs or mongodb)'
killall -w redis-server

%files %{python_files}
%license LICENSE
%doc README.md HISTORY.md docs/*.md docs/*.rst
%{python_sitelib}/requests_cache
%{python_sitelib}/requests_cache-%{version}*-info

%changelog
