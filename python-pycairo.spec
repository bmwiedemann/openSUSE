#
# spec file for package python-pycairo
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
%define         oldpython python
Name:           python-pycairo
Version:        1.18.1
Release:        0
Summary:        Python Bindings for Cairo
License:        LGPL-2.1-or-later OR MPL-1.1
Group:          Development/Libraries/Python
Url:            http://www.cairographics.org/pycairo
Source:         https://github.com/pygobject/pycairo/releases/download/v%{version}/pycairo-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  cairo-devel >= 1.13.1
BuildRequires:  python-rpm-macros
Provides:       python-cairo = %{version}
Obsoletes:      python-cairo < %{version}
%ifpython2
Provides:       %{oldpython}-cairo = %{version}
Obsoletes:      %{oldpython}-cairo < %{version}
%endif

%python_subpackages

%description
Pycairo is a Python module providing bindings for the cairo graphics library.

%package        devel
Summary:        Development files for the Cairo Python bindings
Group:          Development/Libraries/C and C++
Requires:       python-pycairo = %{version}
Requires:       python-pycairo-common-devel = %{version}
Requires:       python-devel
Provides:       python-cairo-devel = %{version}
Obsoletes:      python-cairo-devel < %{version}
%ifpython2
Provides:       %{oldpython}-cairo-devel = %{version}
Obsoletes:      %{oldpython}-cairo-devel < %{version}
%endif

%description   devel
Pycairo is a Python module providing bindings for the cairo graphics library.

This package provides the development files needed to build
packages that depen on Pycairo.

%package     -n python-pycairo-common-devel
Summary:        Headers for the Cairo Python bindings
Group:          Development/Libraries/C and C++
Provides:       %{python_module pycairo-common-devel = %{version}}
Provides:       %{python_module cairo-common-devel = %{version}}
Obsoletes:      %{python_module cairo-common-devel < %{version}}
Provides:       python-cairo-common-devel = %{version}
Obsoletes:      python-cairo-common-devel < %{version}
Requires:       cairo-devel

%description -n python-pycairo-common-devel
Pycairo is a Python module providing bindings for the cairo graphics library.

This package provides the headers and development files needed to build
packages that depen on Pycairo.

%prep
%setup -n pycairo-%{version}

%build
%python_build

%install
%python_install

%check
%python_exec setup.py test

%files %{python_files}
%doc NEWS docs
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{python_sitearch}/cairo/
%{python_sitearch}/pycairo-*.egg-info

%files %{python_files devel}
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%ifpython2
%{_libdir}/pkgconfig/pycairo.pc
%endif
%ifpython3
%{_libdir}/pkgconfig/py3cairo.pc
%endif

%files -n python-pycairo-common-devel
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{_includedir}/pycairo/

%changelog
