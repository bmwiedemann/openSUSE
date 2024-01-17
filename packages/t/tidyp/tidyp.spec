#
# spec file for package tidyp
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           tidyp
Version:        1.04
Release:        0
Summary:        Utility to Clean Up and Pretty-print HTML, XHTML or XML Markup
License:        W3C
Group:          Productivity/Publishing/HTML/Tools
Url:            http://tidy.sourceforge.net/
Source0:        http://github.com//downloads/petdance/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tidy is a commandline frontend to TidyLib which allows for cleaning up and
pretty printing HTML, XHTML and XML markup in a variety of file encodings. For
HTML variants, it can detect and report proprietary elements as well as many
common coding errors, correct them and produce visually equivalent markup
which is both compliant with W3C standards and works on most browsers.
Furthermore, it can convert plain HTML to XHTML. For generic XML files, Tidy is
limited to correcting basic well-formedness errors and pretty printing.

%package -n libtidyp-1_04-0
Summary:        Library to Clean Up and Pretty-print HTML, XHTML or XML Markup
Group:          Productivity/Publishing/HTML/Tools

%description -n libtidyp-1_04-0
TidyLib is a library for cleaning up and pretty printing HTML, XHTML and XML
markup in a variety of file encodings. For HTML variants, it can detect and
report proprietary elements as well as many common coding errors, correct them
and produce visually equivalent markup which is both compliant with W3C
standards and works on most browsers. Furthermore, it can convert plain HTML
into XHTML. For generic XML files, Tidy is limited to correcting basic
well-formedness errors and pretty printing.

There is a commandline frontend for this library, contained in the package
"tidy".

%package -n libtidyp-devel
Summary:        Include Files and Libraries for Development
Group:          Development/Libraries/C and C++
Requires:       libtidyp-1_04-0 = %{version} glibc-devel

%description -n libtidyp-devel
This package contains all necessary include files and libraries needed
to develop applications using functions provided by the TidyLib library.


%prep
%setup -q 

%build
%configure --disable-static --with-pic --disable-dependency-tracking 
make %{?_smp_mflags} all

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/libtidyp.la

%post -n libtidyp-1_04-0 -p /sbin/ldconfig

%postun -n libtidyp-1_04-0 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%_bindir/tidyp

%files -n libtidyp-1_04-0
%defattr(-, root, root)
%{_libdir}/libtidy*.so.*

%files -n libtidyp-devel
%defattr(-, root, root)
%{_includedir}/%{name}
%_libdir/libtidyp.so

%changelog
