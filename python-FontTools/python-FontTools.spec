#
# spec file for package python-FontTools
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
Name:           python-FontTools
Version:        3.39.0
Release:        0
Summary:        Suite of Tools and Libraries for Manipulating Fonts
License:        MIT AND OFL-1.1
Group:          Development/Languages/Python
URL:            http://github.com/fonttools/fonttools
Source:         https://files.pythonhosted.org/packages/source/f/fonttools/fonttools-%{version}.zip
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-brotlipy >= 0.7.0
%ifpython2
Requires:       python-enum34
%endif
Requires:       python-fs >= 2.4.4
Requires:       python-reportlab
Requires:       python-scipy >= 1.2.1
Requires:       python-sympy
# SECTION test requirements
BuildRequires:  %{python_module brotlipy >= 0.7.0}
BuildRequires:  %{python_module fs >= 2.4.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.2.1}
BuildRequires:  %{python_module sympy}
BuildRequires:  python2-enum34
BuildRequires:  zip
# /SECTION
%ifpython3
Obsoletes:      fonttools
Provides:       fonttools
%endif
BuildArch:      noarch
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# remove undocumented and non working script
rm %{buildroot}%{_bindir}/fonttools

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

%files %{python_files}
%license LICENSE LICENSE.external
%doc README.rst NEWS.rst
%{python_sitelib}/*
%python3_only %{_bindir}/pyftmerge
%python3_only %{_bindir}/pyftsubset
%python3_only %{_bindir}/ttx
%python3_only %{_mandir}/man1/ttx.1%{?ext_man}

%changelog
