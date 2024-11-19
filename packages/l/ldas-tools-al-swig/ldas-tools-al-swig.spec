#
# spec file for package ldas-tools-al-swig
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


Name:           ldas-tools-al-swig
Version:        2.6.10
Release:        0
Summary:        LDAS (LIGO Data Analysis System) tools abstraction toolkit language bindings
License:        GPL-2.0-or-later
URL:            https://wiki.ligo.org/Computing/LDASTools
Source:         http://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module distutils-extra}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(ldastoolsal)
BuildRequires:  pkgconfig(ldastoolscmake)

%python_subpackages

%description
This provides different language bindings for the LDAS tools abstaction library.

%prep
%setup -q

%build
%{python_expand # Necessary to run cmake with all python flavors
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
%cmake -DPYTHON3_VERSION=%{$python_version}
%cmake_build
popd
}

%install
%{python_expand # Necessary to run cmake with all python flavors
export PYTHON=$python
pushd ../${PYTHON}_build
%cmake_install
popd
}

%files -n %{name}
%license COPYING
%{_includedir}/ldastoolsal/*.i

%files %{python_files}
%doc ChangeLog.md README
%license COPYING
%{python_sitearch}/LDAStools/

%changelog
