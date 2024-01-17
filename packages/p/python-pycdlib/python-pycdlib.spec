#
# spec file for package python-pycdlib
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pycdlib
Version:        1.14.0
Release:        0
Summary:        Pure python ISO manipulation library
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/clalancette/pycdlib
Source:         https://files.pythonhosted.org/packages/source/p/pycdlib/pycdlib-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  mkisofs
BuildRequires:  python-rpm-macros
BuildRequires:  timezone
Requires:       mkisofs
Requires:       python3-pycdlib-common
BuildArch:      noarch
%python_subpackages

%description
PyCdlib is a pure python library to parse, write (master), and create ISO9660
files, suitable for writing to a CD or USB.

The original ISO9660 (including ISO9660-1999) specification is supported, as
well the El Torito, Joliet, Rock Ridge, and UDF extensions.

Please see https://clalancette.github.io/pycdlib/ for much more documentation

%package -n python3-pycdlib-common
Summary:        Pure python ISO manipulation library - common files
Group:          Development/Languages/Python

%description -n python3-pycdlib-common
PyCdlib is a pure python library to parse, write (master), and create ISO9660
files, suitable for writing to a CD or USB.

The original ISO9660 (including ISO9660-1999) specification is supported, as
well the El Torito, Joliet, Rock Ridge, and UDF extensions.

This package includes the common files.

%prep
%setup -q -n pycdlib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pycdlib-explorer
%python_clone -a %{buildroot}%{_bindir}/pycdlib-extract-files
%python_clone -a %{buildroot}%{_bindir}/pycdlib-genisoimage

%check
export LC_ALL=ja_JP.UTF-8
export TZ=Asia/Tokyo
%pytest -k unit

%post
%{python_install_alternative pycdlib-explorer pycdlib-extract-files pycdlib-genisoimage}

%postun
%{python_uninstall_alternative pycdlib-explorer pycdlib-extract-files pycdlib-genisoimage}

%files %{python_files}
%doc README.md
%license COPYING
%python_alternative %{_bindir}/pycdlib-explorer
%python_alternative %{_bindir}/pycdlib-extract-files
%python_alternative %{_bindir}/pycdlib-genisoimage
%{python_sitelib}/*

%files -n python3-pycdlib-common
%{_mandir}/man1/pycdlib-explorer.1%{?ext_man}
%{_mandir}/man1/pycdlib-extract-files.1%{?ext_man}
%{_mandir}/man1/pycdlib-genisoimage.1%{?ext_man}

%changelog
