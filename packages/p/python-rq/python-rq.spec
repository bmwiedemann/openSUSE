#
# spec file for package python-rq
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define mod_name rq
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-rq%{psuffix}
Version:        2.12.0
Release:        0
Summary:        Easy Job Queues for Python
License:        BSD-2-Clause
URL:            https://github.com/rq/rq
Source:         https://files.pythonhosted.org/packages/source/r/rq/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module click >= 5.0.0}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module redis >= 3.5.0}
BuildRequires:  fdupes
BuildRequires:  psmisc
BuildRequires:  python-rpm-macros
BuildRequires:  redis
Requires:       python-click >= 5.0.0
Requires:       python-croniter
Requires:       python-redis >= 3.5.0
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module %{mod_name} = %{version}}
BuildRequires:  %{python_module psutil >= 7}
BuildRequires:  %{python_module pytest >= 8.3.5}
%endif
%python_subpackages

%description
RQ (Redis Queue) is a simple Python library for queueing jobs and processing
them in the background with workers. It is backed by Redis. It can be
integrated into web stacks.

%prep
%autosetup -p1 -n %{mod_name}-%{version}
chmod -x rq/cli/cli.py

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rq
%python_clone -a %{buildroot}%{_bindir}/rqinfo
%python_clone -a %{buildroot}%{_bindir}/rqworker
%python_group_libalternatives rq rqinfo rqworker
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export PATH="$PATH:%{buildroot}%{_bindir}"
%{_sbindir}/redis-server --port 6379 &
trap 'killall redis-server || true' EXIT
# test_execution_order_with_sole_dependency assumes worker process w1 takes the
# first job within 0.5 s; on slow ppc64le builders w2 wins the race
# (uname, not %ifarch: both never match on a noarch package, rpm names the arch powerpc64le)
skip=
if [ "$(uname -m)" = ppc64le ]; then
  skip="--deselect tests/test_job_dependency.py::TestJobDependency::test_execution_order_with_sole_dependency"
fi
%pytest $skip
%endif

%if !%{with test}
%pre
%python_libalternatives_reset_alternative rq
%python_libalternatives_reset_alternative rqinfo
%python_libalternatives_reset_alternative rqworker

%post
%python_install_alternative rq rqinfo rqworker

%postun
%python_uninstall_alternative rq
%python_uninstall_alternative rqinfo
%python_uninstall_alternative rqworker

%files %{python_files}
%doc README.md CHANGES.md
%license LICENSE
%{python_sitelib}/rq
%{python_sitelib}/rq-%{version}.dist-info
%python_alternative %{_bindir}/rq
%python_alternative %{_bindir}/rqinfo
%python_alternative %{_bindir}/rqworker
%endif

%changelog
