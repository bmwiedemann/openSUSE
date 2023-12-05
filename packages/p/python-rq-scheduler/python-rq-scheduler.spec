#
# spec file for package python-rq-scheduler
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


Name:           python-rq-scheduler
Version:        0.13.1
Release:        0
Summary:        Provides job scheduling capabilities to RQ (Redis Queue)
License:        MIT
URL:            https://github.com/rq/rq-scheduler
Source:         https://files.pythonhosted.org/packages/source/r/rq-scheduler/rq-scheduler-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module crontab >= 0.23.0}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module rq >= 0.13}
# /SECTION
BuildRequires:  fdupes
Requires:       python-crontab >= 0.23.0
Requires:       python-freezegun
Requires:       python-python-dateutil
Requires:       python-rq >= 0.13
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Provides job scheduling capabilities to RQ (Redis Queue)

%prep
%autosetup -p1 -n rq-scheduler-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rqscheduler
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative rqscheduler

%postun
%python_uninstall_alternative rqscheduler

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/rqscheduler
%{python_sitelib}/rq_scheduler
%{python_sitelib}/rq_scheduler-%{version}.dist-info

%changelog
