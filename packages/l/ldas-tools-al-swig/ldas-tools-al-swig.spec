#
# spec file for package ldas-tools-al-swig
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

Name:           ldas-tools-al-swig
Version:        2.6.7
Release:        0
Summary:        LDAS (LIGO Data Analysis System) tools abstraction toolkit language bindings
License:        GPL-2.0-or-later
URL:            https://wiki.ligo.org/Computing/LDASTools 
Source:         http://software.ligo.org/lscsoft/source/ldas-tools-al-swig-2.6.7.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(ldastoolsal)
BuildRequires:  pkgconfig(ldastoolscmake)

%description
This provides different language bindings for the LDAS tools abstaction library.

%python_subpackages

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_includedir}/ldastoolsal/*.i

%files %{python_files}
%doc ChangeLog README
%license COPYING
%{python_sitearch}/*

%changelog
