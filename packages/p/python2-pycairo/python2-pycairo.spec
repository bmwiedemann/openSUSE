#
# spec file for package python2-pycairo
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


Name:           python2-pycairo
Version:        1.18.1
Release:        0
Summary:        Python Bindings for Cairo
License:        LGPL-2.1-or-later OR MPL-1.1
URL:            https://github.com/pygobject/pycairo
Source:         https://github.com/pygobject/pycairo/releases/download/v%{version}/pycairo-%{version}.tar.gz
BuildRequires:  cairo-devel >= 1.13.1
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-rpm-macros
Provides:       python2-cairo = %{version}
Obsoletes:      python2-cairo < %{version}
Provides:       python-cairo = %{version}
Obsoletes:      python-cairo < %{version}

%description
Pycairo is a Python module providing bindings for the cairo graphics library.

%package        devel
Summary:        Development files for the Cairo Python bindings
Requires:       python-devel
Requires:       python2-pycairo = %{version}
Requires:       python2-pycairo-common-devel = %{version}
Provides:       python2-cairo-devel = %{version}
Obsoletes:      python2-cairo-devel < %{version}
Provides:       python-cairo-devel = %{version}
Obsoletes:      python-cairo-devel < %{version}

%description   devel
Pycairo is a Python module providing bindings for the cairo graphics library.

This package provides the development files needed to build
packages that depen on Pycairo.

%package     -n python2-pycairo-common-devel
Summary:        Headers for the Cairo Python bindings
Requires:       cairo-devel
Provides:       python-pycairo-common-devel = %{version}
Provides:       python2-cairo-common-devel = %{version}
Obsoletes:      python2-cairo-common-devel < %{version}
Provides:       python-cairo-common-devel = %{version}
Obsoletes:      python-cairo-common-devel < %{version}

%description -n python2-pycairo-common-devel
Pycairo is a Python module providing bindings for the cairo graphics library.

This package provides the headers and development files needed to build
packages that depen on Pycairo.

%prep
%setup -q -n pycairo-%{version}

%build
%python2_build

%install
%python2_install
%fdupes %{buildroot}%{python2_sitearch}

# move headers to not conflict with newer ones from py3
mv %{buildroot}%{_includedir}/pycairo/ %{buildroot}%{_includedir}/pycairo-py2/
sed -i -e 's:include/pycairo:include/pycairo-py2:g' %{buildroot}%{_libdir}/pkgconfig/pycairo.pc

# add the setuptools egg-info directory
rm %{buildroot}%{python2_sitearch}/pycairo-%{version}-py%{python2_version}.egg-info
mkdir -p %{buildroot}%{python2_sitearch}/pycairo-%{version}-py%{python2_version}.egg-info/
cp pycairo.egg-info/* %{buildroot}%{python2_sitearch}/pycairo-%{version}-py%{python2_version}.egg-info/

%files
%doc NEWS docs
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{python2_sitearch}/cairo/
%{python2_sitearch}/pycairo-*.egg-info

%files devel
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{_libdir}/pkgconfig/pycairo.pc

%files -n python2-pycairo-common-devel
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%{_includedir}/pycairo-py2/

%changelog
