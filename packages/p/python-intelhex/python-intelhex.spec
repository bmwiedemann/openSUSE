#
# spec file for package python-intelhex
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


Name:           python-intelhex
Version:        2.3.0
Release:        0
Summary:        Python library for Intel HEX files manipulations
License:        BSD-3-Clause
URL:            https://github.com/python-intelhex/intelhex
Source:         https://files.pythonhosted.org/packages/source/i/intelhex/intelhex-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
Provides:       intelhex = %version-%release
Obsoletes:      intelhex < %version-%release
%python_subpackages

%description
The Intel HEX file format is widely used in microprocessors and
microcontrollers area (embedded systems etc) as the de facto standard
for representation of code to be programmed into microelectronic
devices.

This work implements an ``intelhex`` Python library to read, write,
create from scratch and manipulate data from Intel HEX file format.

The distribution package also includes several convenience Python scripts,
including "classic" ``hex2bin`` and ``bin2hex`` converters and more,
those based on the library itself. Check the docs to know more.

%prep
%autosetup -p1 -n intelhex-%{version}

sed -i -e '/^#!\s*\/usr\/bin\/.*python/d' intelhex/bench.py

%build
%python_build

%install
%python_install
for exe in bin2hex hex2bin hex2dump hexdiff hexinfo hexmerge ; do
mv %{buildroot}%{_bindir}/$exe.py %{buildroot}%{_bindir}/ih_$exe
%python_clone -a %{buildroot}%{_bindir}/ih_$exe
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%post
%python_install_alternative ih_bin2hex
%python_install_alternative ih_hex2bin
%python_install_alternative ih_hex2dump
%python_install_alternative ih_hexdiff
%python_install_alternative ih_hexinfo
%python_install_alternative ih_hexmerge

%postun
%python_uninstall_alternative ih_bin2hex
%python_uninstall_alternative ih_hex2bin
%python_uninstall_alternative ih_hex2dump
%python_uninstall_alternative ih_hexdiff
%python_uninstall_alternative ih_hexinfo
%python_uninstall_alternative ih_hexmerge

%files %{python_files}
%python_alternative %{_bindir}/ih_bin2hex
%python_alternative %{_bindir}/ih_hex2bin
%python_alternative %{_bindir}/ih_hex2dump
%python_alternative %{_bindir}/ih_hexdiff
%python_alternative %{_bindir}/ih_hexinfo
%python_alternative %{_bindir}/ih_hexmerge

%{python_sitelib}/intelhex*

%changelog
