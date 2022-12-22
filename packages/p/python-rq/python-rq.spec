#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%define mod_name rq
%define skip_python2 1

Name:           python-rq%{psuffix}
Version:        1.11.1
Release:        0
Summary:        Easy Job Queues for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/rq/rq
Source:         https://github.com/rq/rq/archive/v%{version}/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module click >= 5.0.0}
BuildRequires:  %{python_module redis >= 3.5.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
BuildRequires:  redis
Requires:       python-click >= 5.0.0
Requires:       python-redis >= 3.5.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch

%if %{with test}
BuildRequires:  %{python_module %{mod_name} = %{version}}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sentry-sdk}
%endif

%python_subpackages

%description
RQ (Redis Queue) is a simple Python library for queueing jobs and processing
them in the background with workers. It is backed by Redis. It can be
integrated into web stacks.

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%if !%{with test}
%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/rq
%python_clone -a %{buildroot}%{_bindir}/rqinfo
%python_clone -a %{buildroot}%{_bindir}/rqworker
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export PATH="$PATH:%{buildroot}%{_bindir}"
%{_sbindir}/redis-server --port 6379 &
%pytest
killall redis-server
%endif

%if !%{with test}
%post
%python_install_alternative rq
%python_install_alternative rqinfo
%python_install_alternative rqworker

%postun
%python_uninstall_alternative rq
%python_uninstall_alternative rqinfo
%python_uninstall_alternative rqworker

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/rq
%{python_sitelib}/rq-%{version}*-info
%python_alternative %{_bindir}/rq
%python_alternative %{_bindir}/rqinfo
%python_alternative %{_bindir}/rqworker
%endif

%changelog
