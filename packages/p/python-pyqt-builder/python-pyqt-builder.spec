#
# spec file for package python-pyqt-builder
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


%define mname pyqt-builder
Name:           python-%{mname}
Version:        1.14.1
Release:        0
Summary:        The PEP 517 compliant PyQt build system
License:        GPL-2.0-only OR GPL-3.0-only OR SUSE-SIP
URL:            https://www.riverbankcomputing.com/software/pyqt-builder
Source0:        https://files.pythonhosted.org/packages/source/P/PyQt-builder/PyQt-builder-%{version}.tar.gz
# PATCH-FEATURE-SUSE support-python3.6.patch alarrosa@suse.com
Patch0:         support-python3.6.patch
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires:       python-sip-devel >= 6.7
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-PyQt-builder = %{version}-%{release}
BuildArch:      noarch
# SECTION Test Requirements
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module sip-devel >= 6.7}
# /SECTION
%python_subpackages

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt. It extends the sip build system and uses Qt’s qmake to perform the
actual compilation and installation of extension modules.

Projects that use PyQt-builder provide an appropriate pyproject.toml file and an
optional project.py script. Any PEP 517 compliant frontend, for example
sip-install or pip can then be used to build and install the project.

%prep
%autosetup -p1 -n PyQt-builder-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyqt-bundle
%python_clone -a %{buildroot}%{_bindir}/pyqt-qt-wheel
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1 # boo#1047218
%{python_expand # no real unit tests; check import and bundle entry point
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c 'import pyqtbuild'
%{buildroot}%{_bindir}/pyqt-bundle-%{$python_bin_suffix} -V
}

%post
%python_install_alternative pyqt-bundle pyqt-qt-wheel

%postun
%python_uninstall_alternative pyqt-bundle

%files %{python_files}
%license LICENSE*
%doc README NEWS ChangeLog
%python_alternative %{_bindir}/pyqt-bundle
%python_alternative %{_bindir}/pyqt-qt-wheel
%{python_sitelib}/pyqtbuild
%{python_sitelib}/PyQt_builder-%{version}*-info

%changelog
