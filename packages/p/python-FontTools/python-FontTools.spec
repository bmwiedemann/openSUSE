#
# spec file for package python-FontTools
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
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-FontTools%{psuffix}
Version:        4.61.1
Release:        0
Summary:        Suite of Tools and Libraries for Manipulating Fonts
License:        MIT AND OFL-1.1
Group:          Development/Languages/Python
URL:            https://github.com/fonttools/fonttools
# The PyPI archive lacks some test files, but the source is identical to the github archive
Source:         https://github.com/fonttools/fonttools/archive/refs/tags/%{version}.tar.gz#/fonttools-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Recommends:     python-Brotli >= 1.1.0
Recommends:     python-freetype-py >= 2.4.0
Recommends:     python-lxml
Recommends:     python-munkres >= 1.1.4
Recommends:     python-reportlab
Recommends:     python-scipy >= 1.11.4
Recommends:     python-sympy >= 1.12
Recommends:     python-ufoLib2 >= 0.16.0
Recommends:     python-unicodedata2 >= 17.0.0
Recommends:     python-zopfli >= 0.1.4
Provides:       python-fonttools = %{version}-%{release}
Obsoletes:      fonttools < %{version}-%{release}
Provides:       fonttools = %{version}-%{release}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
BuildRequires:  %{python_module Brotli >= 1.1.0}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
FontTools is a suite of tools and libraries for manipulating fonts
written in Python.

It currently reads and writes TrueType font files, reads PostScript
Type 1 fonts, and more. It contains two command line programs to
convert TrueType fonts to an XML based format (called TTX) and back.

%prep
%autosetup -p1 -n fonttools-%{version}

# Remove shebang
sed -i -e '/^#!\//, 1d' Lib/fontTools/mtiLib/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_mandir}/man1/ttx.1
%python_clone -a %{buildroot}%{_bindir}/ttx
%python_clone -a %{buildroot}%{_bindir}/pyftsubset
%python_clone -a %{buildroot}%{_bindir}/pyftmerge
%python_clone -a %{buildroot}%{_bindir}/fonttools
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
%pytest -ra
# We need these files to be installed for tests, but now we need them removed
# not to confuse %%files checks
%python_expand rm -r %{buildroot}%{$python_sitelib}
%if %{with libalternatives}
rm -r %{buildroot}%{_datadir}/libalternatives
%else
rm -r %{buildroot}%{_sysconfdir}/alternatives
%endif
rm -r %{buildroot}%{_bindir}
rm -r %{buildroot}%{_mandir}
%endif

%if %{without test}
%post
%python_install_alternative ttx ttx.1
%python_install_alternative pyftsubset
%python_install_alternative pyftmerge
%python_install_alternative fonttools

%postun
%python_uninstall_alternative ttx
%python_uninstall_alternative pyftsubset
%python_uninstall_alternative pyftmerge
%python_uninstall_alternative fonttools

%pre
%python_libalternatives_reset_alternative ttx
%python_libalternatives_reset_alternative pyftsubset
%python_libalternatives_reset_alternative pyftmerge
%python_libalternatives_reset_alternative fonttools

%files %{python_files}
%license LICENSE LICENSE.external
%doc README.rst NEWS.rst
%python_alternative %{_bindir}/pyftmerge
%python_alternative %{_bindir}/pyftsubset
%python_alternative %{_bindir}/ttx
%python_alternative %{_bindir}/fonttools
%python_alternative %{_mandir}/man1/ttx.1%{?ext_man}
%{python_sitelib}/fontTools
%{python_sitelib}/fonttools-%{version}.dist-info
%endif

%changelog
