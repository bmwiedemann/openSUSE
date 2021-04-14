#
# spec file for package smooth
#
# Copyright (c) 2021 SUSE LLC
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


%define _uver   0_9
%define _lver   0.9
%define sover   0
Name:           smooth
Version:        0.9.7
Release:        0
Summary:        C++ class library for widgets, IO, XML and more
License:        Artistic-2.0
URL:            http://www.smooth-project.org
Source0:        https://sourceforge.net/projects/smooth/files/smooth/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcpuid) >= 0.5
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libxml-2.0)

%description
smooth is an object oriented C++ class library. It provides basic
functionality and platform support for applications and libraries.

Features provided by smooth include:

  * user interface API with various widgets
  * multithreading API
  * file and network IO interface
  * transparent Unicode and software internationalization support
  * a libxml2-based XML parser

%package        devel
Summary:        Development files for %{name}
Requires:       lib%{name}-%{_uver}-%{sover} = %{version}
Requires:       pkgconfig(x11)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n lib%{name}-%{_uver}-%{sover}
Summary:        C++ class library for widgets, IO, XML and more

%description -n lib%{name}-%{_uver}-%{sover}
smooth is an object oriented C++ class library. It provides basic
functionality and platform support for applications and libraries.

Features provided by smooth include:

  * user interface API with various widgets
  * multithreading API
  * file and network IO interface
  * transparent Unicode and software internationalization support
  * a libxml2-based XML parser

%prep
%autosetup -p1
dos2unix Copying Readme.md

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build config=systemlibcpuid

%install
%make_install libdir=%{_libdir} includedir=%{_includedir} bindir=%{_bindir}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n lib%{name}-%{_uver}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-%{_uver}-%{sover} -p /sbin/ldconfig

%files
%license Copying
%doc ChangeLog Readme.md
%{_bindir}/%{name}-translator

%files devel
%doc ChangeLog Readme.md
%license Copying
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}-%{_lver}.so

%files -n lib%{name}-%{_uver}-%{sover}
%license Copying
%{_libdir}/lib%{name}-%{_lver}.so.%{sover}

%changelog
