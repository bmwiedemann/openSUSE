#
# spec file for package tclap-doc
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


Name:           tclap-doc
Version:        1.2.1
Release:        0
Summary:        API Documentation for %{name}
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://tclap.sf.net
Source0:        http://prdownloads.sourceforge.net/tclap/tclap-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildArch:      noarch

%description

This package contains the API documentation for TCLAP, the Templatized
C++ Command Line Parser.

%prep
%setup -q -n tclap-%{version}

%build
%configure \
	 --enable-doxygen
%make_build

%install
%make_install

install -d "%{buildroot}%{_docdir}/%{name}"

mv "%{buildroot}%{_datadir}/doc/tclap" "%{buildroot}%{_docdir}/%{name}/html"
rm -rf "%{buildroot}%{_docdir}/%{name}/html/html/CVS"

%fdupes -s "%{buildroot}%{_docdir}/%{name}/html"

rm -rf %{buildroot}/%{_includedir}/tclap
rm -f %{buildroot}/%{_libdir}/pkgconfig/tclap.pc

%files
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html

%changelog
