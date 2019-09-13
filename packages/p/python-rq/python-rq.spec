#
# spec file for package python-rq
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


%define mod_name rq
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rq
Version:        1.1.0
Release:        0
Summary:        Easy Job Queues for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/rq/rq
Source:         https://github.com/rq/rq/archive/v%{version}.tar.gz
BuildRequires:  %{python_module click >= 3.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
Requires:       python-click >= 3.0
Requires:       python-redis >= 3.0.0
%python_subpackages

%description
RQ (Redis Queue) is a simple Python library for queueing jobs and processing
them in the background with workers. It is backed by Redis. It can be
integrated into web stacks.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_failure_capture - circular dependency on sentry-sdk
export PATH="$PATH:%{buildroot}%{_bindir}"
%{_sbindir}/redis-server --port 6379 &
%pytest -k 'not test_failure_capture'
killall redis-server

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/*
%python3_only %{_bindir}/rq*

%changelog
