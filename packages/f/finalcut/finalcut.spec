#
# spec file for package finalcut.spec
#
# Copyright (c) 2018 by Markus Gans
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


%define sover   0
Name:           finalcut
Version:        0.5.0
Release:        0
Summary:        Console widget library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/gansm/finalcut/
Source:         https://github.com/gansm/finalcut/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gpm-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel

%description
The Final Cut is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package -n libfinal-devel
Summary:        Development files for The Final Cut text widget library
Group:          Development/Libraries/C and C++
Requires:       libfinal%{sover} = %{version}
Requires:       bdftopcf
Requires:       coreutils
Requires:       gcc-c++
Requires:       grep
Requires:       gzip
Requires:       sed
Requires:       vim
Provides:       finalcut-devel = %{version}
Obsoletes:      finalcut-devel < %{version}
Recommends:     %{name}-examples = %{version}

%description -n libfinal-devel
The Final Cut is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package -n libfinal-examples
Summary:        Example files for The Final Cut library
Group:          Development/Languages/C and C++
BuildArch:      noarch
Provides:       finalcut-examples = %{version}
Obsoletes:      finalcut-examples < %{version}

%description -n libfinal-examples
The Final Cut is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package -n libfinal%{sover}
Summary:        Console widget toolkit
Group:          System/Libraries

%description -n libfinal%{sover}
The Final Cut is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%prep
%setup -q

%build
autoreconf -vif
export CPPFLAGS="%{optflags} -Wall -Wextra -Wpedantic"
%ifnarch %ix86 x86_64
export CPPFLAGS="$CPPFLAGS -Wno-error=unused-parameter"
%endif
%configure --disable-static
make %{?_smp_mflags} V=1

%install
make install libdir=%{buildroot}%{_libdir}/ \
	     includedir=%{buildroot}%{_includedir} \
	     bindir=%{buildroot}%{_bindir} \
	     docdir=%{buildroot}%{_docdir}/%{name}/
mkdir -p %{buildroot}%{_docdir}/%{name}/examples
cp -p examples/*.cpp %{buildroot}%{_docdir}/%{name}/examples
cp -p examples/Makefile.clang %{buildroot}%{_docdir}/%{name}/examples
cp -p examples/Makefile.gcc %{buildroot}%{_docdir}/%{name}/examples
rm -f %{buildroot}%{_libdir}/libfinal.la %{buildroot}%{_libdir}/%{name}/examples
rm %{buildroot}%{_docdir}/%{name}/ChangeLog %{buildroot}%{_docdir}/%{name}/COPYING.LESSER

%post -n libfinal%{sover} -p /sbin/ldconfig
%postun -n libfinal%{sover} -p /sbin/ldconfig

%files -n libfinal-devel
%if 0%{?sle_version} > 120200 || 0%{?suse_version} > 1500
%license COPYING.LESSER
%else
%doc COPYING.LESSER
%endif
%doc ChangeLog README.md
%exclude %{_docdir}/%{name}/examples
%{_docdir}/%{name}
%{_libdir}/libfinal.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/final

%files -n libfinal-examples
%{_docdir}/%{name}/examples

%files -n libfinal%{sover}
%{_libdir}/libfinal.so.*

%changelog
