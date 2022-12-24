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

Name:           python-py7zr%{psuffix}
Version:        0.20.2
Release:        0
Summary:        Library and utility to support 7zip
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/miurahr/py7zr
Source0:        https://files.pythonhosted.org/packages/source/p/py7zr/py7zr-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 63}
BuildRequires:  %{python_module setuptools_scm >= 7.0.5}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli >= 1.0.9
Requires:       python-multivolumefile >= 0.2.3
Requires:       python-psutil
Requires:       python-pybcj >= 0.6.0
Requires:       python-pycryptodomex >= 3.6.6
Requires:       python-pyzstd >= 0.14.4
Requires:       python-texttable
Requires:       (python-pyppmd >= 0.18.1 with python-pyppmd < 1.1.0)
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib_metadata
%endif
%if 0%{?python_version_nodots} > 36
Requires:       python-inflate64 >= 0.3.1
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
%if %{with test}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module py7zr = %{version}}
BuildRequires:  %{python_module pyannotate}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-remotedata}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
%endif
BuildArch:      noarch
%python_subpackages

%description
py7zr is a library and utility to support 7zip archive compression, decompression, encryption and decryption written by Python programming language.

%prep
%setup -q -n py7zr-%{version}
# remove shebangs from source
sed -i '1{/#!/d}' py7zr/*.py

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/py7zr
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%post
%python_install_alternative py7zr

%postun
%python_uninstall_alternative py7zr

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst Changelog.rst
%{python_sitelib}/py7zr
%{python_sitelib}/py7zr-%{version}*-info
%python_alternative %{_bindir}/py7zr
%endif

%changelog
