#
# spec file for package python-pyOCD
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
Name:           python-pyOCD
Version:        0.21.0
Release:        0
Summary:        CMSIS-DAP debugger for python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mbedmicro/pyOCD
Source:         https://files.pythonhosted.org/packages/source/p/pyocd/pyocd-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm_git_archive}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-usb
Provides:       python-pyocd = %{version}
Obsoletes:      python-pyocd < %{version}
BuildArch:      noarch
%python_subpackages

%description
On-chip debugger and flasher tool for ARM microcontrollers.

%prep
%setup -q -n pyocd-%{version}

%build
%python_build

%install
%python_install
%python_clone %{buildroot}%{_bindir}/pyocd
%python_clone %{buildroot}%{_bindir}/pyocd-flashtool
%python_clone %{buildroot}%{_bindir}/pyocd-gdbserver
%python_clone %{buildroot}%{_bindir}/pyocd-tool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{_bindir}/pyocd-flashtool-%{python_bin_suffix}
%{_bindir}/pyocd-gdbserver-%{python_bin_suffix}
%{_bindir}/pyocd-tool-%{python_bin_suffix}
%{_bindir}/pyocd-%{python_bin_suffix}
%python3_only %{_bindir}/pyocd
%python3_only %{_bindir}/pyocd-flashtool
%python3_only %{_bindir}/pyocd-gdbserver
%python3_only %{_bindir}/pyocd-tool
%{python_sitelib}/*

%changelog
