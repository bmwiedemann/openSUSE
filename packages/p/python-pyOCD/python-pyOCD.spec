#
# spec file for package python-pyOCD
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


Name:           python-pyOCD
Version:        0.36.0
Release:        0
Summary:        CMSIS-DAP debugger for python
License:        Apache-2.0
URL:            https://github.com/mbedmicro/pyOCD
Source:         https://files.pythonhosted.org/packages/source/p/pyocd/pyocd-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-usb
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-pyocd = %{version}
Obsoletes:      python-pyocd < %{version}
BuildArch:      noarch
%python_subpackages

%description
On-chip debugger and flasher tool for ARM microcontrollers.

%prep
%setup -q -n pyocd-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyocd
%python_clone -a %{buildroot}%{_bindir}/pyocd-gdbserver
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pyocd
%python_install_alternative pyocd-gdbserver

%postun
%python_uninstall_alternative pyocd
%python_uninstall_alternative pyocd-gdbserver

%files %{python_files}
%python_alternative %{_bindir}/pyocd
%python_alternative %{_bindir}/pyocd-gdbserver
%{python_sitelib}/pyocd
%{python_sitelib}/pyocd-%{version}.dist-info

%changelog
