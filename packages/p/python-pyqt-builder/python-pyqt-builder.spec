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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-pyqt-builder
Version:        1.18.2
Release:        0
Summary:        The PEP 517 compliant PyQt build system
License:        BSD-2-Clause
URL:            https://github.com/Python-PyQt/PyQt-builder
Source0:        https://files.pythonhosted.org/packages/source/p/pyqt_builder/pyqt_builder-%{version}.tar.gz
Source99:       python-pyqt-builder.rpmlintrc
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
Requires:       python-sip-devel >= 6.7
Provides:       python-PyQt-builder = %{version}-%{release}
BuildArch:      noarch
%if 0%{?suse_version} < 1600
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm >= 7}
%else
BuildRequires:  %{python_module setuptools >= 77}
BuildRequires:  %{python_module setuptools_scm >= 8}
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
%autosetup -p1 -n pyqt_builder-%{version}
# Make it work with setuptools < 77 and setuptools_scm < 8
%if 0%{?suse_version} < 1600
sed -i pyproject.toml \
    -e 's/version_file/write_to/' \
    -e 's/license = .*/license = { file = "LICENSE" }/' \
    -e '/license-files/d'
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyqt-bundle
%python_clone -a %{buildroot}%{_bindir}/pyqt-qt-wheel
%python_group_libalternatives pyqt-bundle pyqt-qt-wheel
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

%pre
%python_libalternatives_reset_alternative pyqt-bundle

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/pyqt-bundle
%python_alternative %{_bindir}/pyqt-qt-wheel
%{python_sitelib}/pyqtbuild
%{python_sitelib}/[Pp]y[Qq]t_builder-%{version}.dist-info

%changelog
