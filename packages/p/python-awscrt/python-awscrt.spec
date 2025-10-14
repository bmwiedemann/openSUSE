#
# spec file for package python-awscrt
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2024 Dominik Wombacher <dominik@wombacher.cc>
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

%{?sle15_python_module_pythons}
Name:           python-awscrt
Version:        0.28.1
Release:        0
Summary:        A common runtime for AWS Python projects
License:        Apache-2.0
URL:            https://github.com/awslabs/aws-crt-python
Source:         %{url}/archive/v%{version}.tar.gz#/awscrt-%{version}.tar.gz

# PATCH-FIX-OPENSUSE skip-test-requiring-network.patch nforro@redhat.com -- one test requires internet connection, skip it
Patch:          skip-test-requiring-network.patch

BuildRequires:  python-rpm-macros
BuildRequires:  cmake(aws-c-auth)
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-checksums)
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-c-compression)
BuildRequires:  cmake(aws-c-event-stream)
BuildRequires:  cmake(aws-c-http)
BuildRequires:  cmake(aws-c-mqtt)
BuildRequires:  cmake(aws-c-io)
BuildRequires:  cmake(aws-c-s3)
BuildRequires:  cmake(aws-c-sdkutils)
BuildRequires:  cmake(s2n)
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module websockets}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  ca-certificates-mozilla

%python_subpackages

%description
A common runtime for AWS Python projects


%prep
%autosetup -p1 -n aws-crt-python-%{version}


%build
%pyproject_wheel


%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}


%check
%pyunittest_arch -v


%files %{python_files}
%doc README.md
%license LICENSE NOTICE
%{python_sitearch}/_awscrt*
%{python_sitearch}/awscrt
%{python_sitearch}/awscrt-*-info


%changelog

