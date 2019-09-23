#
# spec file for package python-pyngus
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
%bcond_without test
Name:           python-pyngus
Version:        2.3.0
Release:        0
Summary:        Callback API implemented over Proton
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/kgiusti/pyngus
Source:         https://github.com/kgiusti/pyngus/archive/v%{version}.tar.gz#/pyngus-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-python-qpid-proton >= 0.9
BuildArch:      noarch
BuildRequires:  fdupes
%if %{with test}
BuildRequires:  %{python_module python-qpid-proton >= 0.9}
%endif
%python_subpackages

%description
A messaging framework built on the QPID Proton engine. It 
provides a callback-based API for message passing

%prep
%setup -q -n pyngus-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
# SSL Failure: error:1417C086:SSL routines:tls_process_client_certificate:certificate verify failed
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests/test-runner -i '*test_ssl_minimal'
%endif

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
