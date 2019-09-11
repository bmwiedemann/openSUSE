#
# spec file for package libqxp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global apiversion 0.0
%global pkgextension 0_0-0
Name:           libqxp
Version:        0.0.1
Release:        0
Summary:        Library to import QuarkXPress documents
License:        MPL-2.0
Group:          Development/Libraries/C and C++
URL:            http://wiki.documentfoundation.org/DLP/Libraries/libqxp
Source:         http://dev-www.libreoffice.org/src/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(librevenge-0.0)
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
%{name} is library providing ability to interpret and import QuarkXPress
document formats into various applications. Currently it only supports
QuarkXPress 3.1-4.1.

%package -n %{name}-%{pkgextension}
Summary:        Library to import QuarkXPress documents
Group:          System/Libraries

%description -n %{name}-%{pkgextension}
%{name} is library providing ability to interpret and import QuarkXPress
document formats into various applications. Currently it only supports
QuarkXPress 3.1-4.1.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{pkgextension} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation of %{name} API
Group:          Documentation/Other
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary:        Tools to transform QuarkXPress documents into other formats
Group:          Productivity/Office/Other
Requires:       %{name}-%{pkgextension} = %{version}-%{release}

%description tools
Tools to transform QuarkXPress documents into other formats.
Currently supported: SVG, plain text, raw.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-werror \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in qxp2raw qxp2svg qxp2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 qxp2*.1 %{buildroot}/%{_mandir}/man1

%post -n %{name}-%{pkgextension} -p /sbin/ldconfig
%postun -n %{name}-%{pkgextension} -p /sbin/ldconfig

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make %{?_smp_mflags} check

%files -n %{name}-%{pkgextension}
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog COPYING
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING
%doc AUTHORS NEWS README
%doc %{_docdir}/%{name}

%files tools
%{_bindir}/qxp2raw
%{_bindir}/qxp2svg
%{_bindir}/qxp2text
%{_mandir}/man1/qxp2raw.1*
%{_mandir}/man1/qxp2svg.1*
%{_mandir}/man1/qxp2text.1*

%changelog
