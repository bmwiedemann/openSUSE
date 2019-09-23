#
# spec file for package tclap
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tclap
Version:        1.2.1
Release:        0
Summary:        Templatized C++ Command Line Parser
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://tclap.sf.net
Source0:        http://prdownloads.sourceforge.net/tclap/tclap-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libstdc++-devel
BuildRequires:  pkg-config
Provides:       libtclap = %{version}
Provides:       libtclap-devel = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
TCLAP is a small, flexible library that provides a simple interface for
defining and accessing command line arguments. It was intially inspired by the
user friendly CLAP libary. The difference is that this library is templatized,
so the argument class is type independent. Type independence avoids
identical-except-for-type objects, such as IntArg, FloatArg, and StringArg.
While the library is not strictly compliant with the GNU or POSIX standards, it
is close.

%package doc
Summary:        API Documentation for %{name}
Group:          Development/Libraries/C and C++

%description doc
This package contains the API documentation for TCLAP, the Templatized
C++ Command Line Parser.

%prep
%setup -q

%build
%configure \
	 --enable-doxygen
make %{?_smp_mflags}

%install
%make_install

install -d "%{buildroot}%{_docdir}/%{name}"

mv "%{buildroot}%{_datadir}/doc/tclap" "%{buildroot}%{_docdir}/%{name}/html"
rm -rf "%{buildroot}%{_docdir}/%{name}/html/html/CVS"

echo -n > docfiles.lst
for f in AUTHORS ChangeLog COPYING NEWS README; do
	 install -m0644 "$f" "%{buildroot}%{_docdir}/%{name}/$f"
	 echo "%doc %{_docdir}/%{name}/${f}" >> docfiles.lst
done

%fdupes -s "%{buildroot}%{_docdir}/%{name}/html"

%check
make %{?_smp_mflags} check

%files -f docfiles.lst
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%{_includedir}/tclap
%{_libdir}/pkgconfig/tclap.pc

%files doc
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html

%changelog
