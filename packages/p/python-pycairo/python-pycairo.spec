#
# spec file for package python-pycairo
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define         oldpython python
Name:           python-pycairo
Version:        1.22.0
Release:        0
Summary:        Python Bindings for Cairo
License:        LGPL-2.1-or-later OR MPL-1.1
URL:            https://github.com/pygobject/pycairo
Source:         %{url}/releases/download/v%{version}/pycairo-%{version}.tar.gz

BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cairo-devel >= 1.15.10
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-cairo = %{version}
Obsoletes:      python-cairo < %{version}
%python_subpackages

%description
Pycairo is a Python module providing bindings for the cairo graphics library.

%package        devel
Summary:        Development files for the Cairo Python bindings
Requires:       python-devel
Requires:       python-pycairo = %{version}
Requires:       python-pycairo-common-devel = %{version}
Provides:       python-cairo-devel = %{version}
Obsoletes:      python-cairo-devel < %{version}

%description   devel
Pycairo is a Python module providing bindings for the cairo graphics library.

This package provides the development files needed to build
packages that depend on Pycairo.

%package     -n python-pycairo-common-devel
Summary:        Headers for the Cairo Python bindings
Requires:       cairo-devel
Provides:       %{python_module cairo-common-devel = %{version}}
Provides:       %{python_module pycairo-common-devel = %{version}}
Obsoletes:      %{python_module cairo-common-devel < %{version}}
Provides:       %{python_module cairo-devel = %{version}}
Obsoletes:      %{python_module cairo-devel < %{version}}
Provides:       python-cairo-common-devel = %{version}
Obsoletes:      python-cairo-common-devel < %{version}

%description -n python-pycairo-common-devel
Pycairo is a Python module providing bindings for the cairo graphics library.

This package provides the headers and development files needed to build
packages that depend on Pycairo.

%prep
%autosetup -n pycairo-%{version} -p1

%build
%python_build

%install
%python_install
# Incorrectly installed by a python38-setuptools vendored distutils
# which does not play well with the distro patched python38.
# Later flavors installed the correct files into lib64 as well
if [ "%{_libdir}" != "%{_prefix}/lib" -a -d %{buildroot}%{_prefix}/lib/pkgconfig ]; then
  rm -r  %{buildroot}%{_prefix}/lib/pkgconfig
fi
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# this is not the deprecated setuptools test call but a custom setup compiling stuff and running pytest
%python_exec setup.py test

%files %{python_files}
%doc NEWS docs
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{python_sitearch}/cairo/
%exclude %{python_sitearch}/cairo/include
%{python_sitearch}/pycairo-*.egg-info

%files %{python_files devel}
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{python_sitearch}/cairo/include

%files -n python-pycairo-common-devel
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/py3cairo.pc

%changelog
