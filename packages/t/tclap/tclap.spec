#
# spec file for package tclap
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


Name:           tclap
Version:        1.2.1
Release:        0
Summary:        Templatized C++ Command Line Parser
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://tclap.sf.net
Source0:        http://prdownloads.sourceforge.net/tclap/tclap-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
Provides:       libtclap = %{version}
Provides:       libtclap-devel = %{version}

%description
TCLAP is a small, flexible library that provides a simple interface for
defining and accessing command line arguments. It was intially inspired by the
user friendly CLAP libary. The difference is that this library is templatized,
so the argument class is type independent. Type independence avoids
identical-except-for-type objects, such as IntArg, FloatArg, and StringArg.
While the library is not strictly compliant with the GNU or POSIX standards, it
is close.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

install -d "%{buildroot}%{_docdir}/%{name}"
mv "%{buildroot}%{_datadir}/doc/tclap" "%{buildroot}%{_docdir}/%{name}/html"
rm -rf "%{buildroot}%{_docdir}/%{name}"

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_includedir}/tclap
%{_libdir}/pkgconfig/tclap.pc

%changelog
