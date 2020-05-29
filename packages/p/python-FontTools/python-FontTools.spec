#
# spec file for package python-FontTools
#
# Copyright (c) 2020 SUSE LLC
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
%else
%define psuffix %{nil}
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-FontTools%{psuffix}
Version:        4.10.2
Release:        0
Summary:        Suite of Tools and Libraries for Manipulating Fonts
License:        MIT AND OFL-1.1
Group:          Development/Languages/Python
URL:            https://github.com/fonttools/fonttools
Source:         https://files.pythonhosted.org/packages/source/f/fonttools/fonttools-%{version}.zip
Source1:        https://raw.githubusercontent.com/fonttools/fonttools/master/Tests/cu2qu/data/curves.json
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-brotlipy >= 0.7.0
Requires:       python-fs >= 2.4.11
Requires:       python-lxml >= 4.0
Requires:       python-reportlab
Requires:       python-scipy >= 1.4.1
Requires:       python-sympy
Requires:       python-unicodedata2 >= 13.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if "%{flavor}" == "test"
BuildRequires:  zip
# SECTION test requirements
BuildRequires:  %{python_module brotlipy >= 0.7.0}
BuildRequires:  %{python_module fs >= 2.4.11}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.4.1}
BuildRequires:  %{python_module sympy}
BuildRequires:  %{python_module ufoLib2 >= 0.6.2}
BuildRequires:  %{python_module zopfli >= 0.1.6}
%endif
# /SECTION
%ifpython3
Obsoletes:      fonttools < %{version}
Provides:       fonttools = %{version}
Provides:       python-fonttools = %{version}
%endif
%python_subpackages

%description
FontTools is a suite of tools and libraries for manipulating fonts
written in Python.

It currently reads and writes TrueType font files, reads PostScript
Type 1 fonts, and more. It contains two command line programs to
convert TrueType fonts to an XML based format (called TTX) and back.

%prep
%setup -q -n fonttools-%{version}
# Remove shebang
sed -i -e '/^#!\//, 1d' Lib/fontTools/mtiLib/__init__.py
cp %{SOURCE1} Tests/cu2qu/data/curves.json

%build
%python_build

%install
%if "%{flavor}" != "test"
%python_install
%python_clone -a %{buildroot}%{_mandir}/man1/ttx.1
%python_clone -a %{buildroot}%{_bindir}/ttx
%python_clone -a %{buildroot}%{_bindir}/pyftsubset
%python_clone -a %{buildroot}%{_bindir}/pyftmerge
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# remove undocumented and non working script
rm %{buildroot}%{_bindir}/fonttools
%endif

%if "%{flavor}" == "test"
%check
ufodir='Tests/ufoLib/testdata/TestFont1 (UFO3).ufo'
if [ ! -e "${ufodir}z" ]; then
  # they forgot to ship Tests/ufoLib/testdata/TestFont1 (UFO3).ufoz
  pushd $(dirname "$ufodir")
  name=$(basename "$ufodir")
  zip -r "${name}z" "$name"
  popd
else
  echo "this can be removed (including zip buildrequires)"
  exit 1
fi
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%pytest

%else
%post
%python_install_alternative ttx ttx.1
%python_install_alternative pyftsubset
%python_install_alternative pyftmerge

%postun
%python_uninstall_alternative ttx
%python_uninstall_alternative pyftsubset
%python_uninstall_alternative pyftmerge

%files %{python_files}
%license LICENSE LICENSE.external
%doc README.rst NEWS.rst
%{python_sitelib}/*
%python_alternative %{_bindir}/pyftmerge
%python_alternative %{_bindir}/pyftsubset
%python_alternative %{_bindir}/ttx
%python_alternative %{_mandir}/man1/ttx.1%{?ext_man}

%endif

%changelog
