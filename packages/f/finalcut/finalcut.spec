#
# spec file for package finalcut
#
# Copyright (c) 2020 by Markus Gans
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
Version:        0.7.1
Release:        0
Summary:        Console widget library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/gansm/finalcut/
Source:         https://github.com/gansm/finalcut/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++ >= 5.1
BuildRequires:  gdb
BuildRequires:  glib2-devel
BuildRequires:  gpm-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel

%description
FINAL CUT is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package -n libfinal-devel
Summary:        Development files for the FINAL CUT text widget library
Group:          Development/Libraries/C and C++
Requires:       bdftopcf
Requires:       coreutils
Requires:       gcc-c++ >= 5.1
Requires:       gpm-devel
Requires:       grep
Requires:       gzip
Requires:       libfinal%{sover} = %{version}
Requires:       ncurses-devel
Requires:       sed
Requires:       vim
Provides:       libfinal-devel = %{version}
Obsoletes:      libfinal-devel < %{version}
Recommends:     libfinal-examples = %{version}

%description -n libfinal-devel
FINAL CUT is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package -n libfinal-examples
Summary:        Example files for the FINAL CUT library
Group:          Development/Languages/C and C++
Provides:       libfinal-examples = %{version}
Obsoletes:      libfinal-examples < %{version}

%description -n libfinal-examples
FINAL CUT is a class library and widget toolkit with full mouse
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
FINAL CUT is a class library and widget toolkit with full mouse
support for creating a text-based user interface. The library supports
the programmer to develop an application for the text console. It allows
the simultaneous handling of multiple windows on the screen.
The C++ class design was inspired by the Qt framework. It provides
common controls like dialog windows, push buttons, check boxes,
radio buttons, input lines, list boxes, status bars and so on.

%package bitmap-fonts
Summary:        X11 bitmap font for FINAL CUT
Group:          System/X11/Fonts
Requires(pre):  fontconfig
# install the fonts only if we have X11 fonts anyways
Supplements:    packageand(libfinal%{sover}:xorg-x11-fonts-core)
BuildArch:      noarch

%description bitmap-fonts
Special X11 bitmap font used by FINAL CUT to display graphic objects.

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
%if 0%{?fedora} || 0%{?rhel} || 0%{?rhl} || 0%{?fc#} || 0%{?el#}
%global _miscfontsdir %{_datadir}/fonts
%endif
make install libdir=%{buildroot}%{_libdir}/ \
             includedir=%{buildroot}%{_includedir} \
             bindir=%{buildroot}%{_bindir} \
             docdir=%{buildroot}%{_docdir}/%{name}/ \
             fontdir=%{buildroot}%{_miscfontsdir}/%{name}/
mkdir -p %{buildroot}%{_miscfontsdir}/%{name}/
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_libdir}/%{name}/examples
mkdir -p %{buildroot}/etc/fonts/conf.d
mkdir -p %{buildroot}/usr/share/fontconfig/conf.avail
cp -p examples/.libs/* %{buildroot}%{_libdir}/%{name}/examples
cp -p examples/*.cpp %{buildroot}%{_libdir}/%{name}/examples
cp -p examples/Makefile.clang %{buildroot}%{_libdir}/%{name}/examples
cp -p examples/Makefile.gcc %{buildroot}%{_libdir}/%{name}/examples
cp -p fonts/40-finalcut-newfont.conf %{buildroot}/usr/share/fontconfig/conf.avail
ln -s /usr/share/fontconfig/conf.avail/40-finalcut-newfont.conf %{buildroot}/etc/fonts/conf.d/40-finalcut-newfont.conf
rm -f %{buildroot}%{_libdir}/libfinal.la
rm %{buildroot}%{_docdir}/%{name}/ChangeLog %{buildroot}%{_docdir}/%{name}/COPYING.LESSER
# Add config for X font path
mkdir -p %{buildroot}%{_datadir}/X11/xorg.conf.d
cat <<EOF > %{buildroot}%{_datadir}/X11/xorg.conf.d/80-finalcut-bitmap-fonts.conf
Section "Files"
    FontPath "%{_miscfontsdir}/finalcut:unscaled"
EndSection
EOF
# make sure we own all generated files
for i in .fonts-config-timestamp encodings.dir fonts.dir fonts.scale; do
    > %{buildroot}%{_miscfontsdir}/finalcut/$i
done

%post -n libfinal%{sover} -p /sbin/ldconfig
%postun -n libfinal%{sover} -p /sbin/ldconfig

%reconfigure_fonts_scriptlets -n %{name}-bitmap-fonts

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
%{_libdir}/%{name}

%files -n libfinal%{sover}
%{_libdir}/libfinal.so.*

%files bitmap-fonts
%dir %{_miscfontsdir}
%dir %{_miscfontsdir}/finalcut
%{_miscfontsdir}/finalcut/*.gz
%{_miscfontsdir}/finalcut/fonts.alias
%ghost %{_miscfontsdir}/finalcut/fonts.dir
%ghost %{_miscfontsdir}/finalcut/fonts.scale
%ghost %{_miscfontsdir}/finalcut/encodings.dir
%ghost %{_miscfontsdir}/finalcut/.fonts-config-timestamp
%dir /etc/fonts/conf.d/
%dir /usr/share/fontconfig/conf.avail
%dir %{_datadir}/X11
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/80-finalcut-bitmap-fonts.conf
/etc/fonts/conf.d/40-finalcut-newfont.conf
/usr/share/fontconfig/conf.avail/40-finalcut-newfont.conf

%changelog
