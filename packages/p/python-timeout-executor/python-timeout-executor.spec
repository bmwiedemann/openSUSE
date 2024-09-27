#
# spec file for package python-timeout-executor
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-timeout-executor
Version:        0.7.1
Release:        0
Summary:        Library to execute python functions with timeout
License:        MIT
URL:            https://github.com/phi-friday/timeout-executor
Source:         https://files.pythonhosted.org/packages/source/t/timeout-executor/timeout_executor-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module anyio >= 4.0.0}
BuildRequires:  %{python_module async-wrapper >= 0.9.0}
BuildRequires:  %{python_module cloudpickle >= 3.0.0}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module tblib >= 3.0.0}
BuildRequires:  %{python_module typing-extensions >= 4.4.0}
BuildRequires:  %{python_module httpx >= 0.27.2}
BuildRequires:  %{python_module pytest >= 8.0.2}
BuildRequires:  %{python_module pytest-cov >= 5.0.0}
BuildRequires:  %{python_module pytest-xdist >= 3.6.1}
BuildRequires:  %{python_module trio >= 0.24.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-anyio >= 4.0.0
Requires:       python-async-wrapper >= 0.9.0
Requires:       python-cloudpickle >= 3.0.0
Requires:       python-psutil
Requires:       python-tblib >= 3.0.0
Requires:       python-typing-extensions >= 4.4.0
Suggests:       python-uvloop
BuildArch:      noarch
%python_subpackages

%description
Library to execute python functions with timeout

%prep
%autosetup -p1 -n timeout_executor-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/timeout_executor
%{python_sitelib}/timeout_executor-%{version}.dist-info

%changelog
