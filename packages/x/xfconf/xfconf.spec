#
# spec file for package xfconf
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


%bcond_with git
%define libname libxfconf-0-3

Name:           xfconf
Version:        4.14.3
Release:        0
Summary:        Simple Configuration Storage for Xfce
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfconf/start
Source0:        https://archive.xfce.org/src/xfce/xfconf/4.14/%{name}-%{version}.tar.bz2
Source1:        xfconf-query.1
Source100:      %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE xfconf-remove-rpath.patch gber@opensuse.org -- Do not set RPATH for Xfconf.so
Patch0:         xfconf-4.7.3-remove-rpath.patch
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  perl(ExtUtils::Depends)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  perl(Glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.10.0
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Recommends:     %{name}-lang = %{version}

%description
Xfconf is a simple client-server configuration storage and query system for the
Xfce desktop.

%package -n perl-xfconf
Summary:        Perl Interface to xfconf
Group:          Development/Libraries/Perl
Requires:       %{name} = %{version}
Requires:       perl = %{perl_version}
Requires:       perl(Glib)

%description -n perl-xfconf
This package contains the Perl interface to %{name}.

%package -n %{libname}
Summary:        Xfconf Shared Library
Group:          System/Libraries
Requires:       %{name} >= %{version}
Provides:       libxfce4mcs = %{version}
Obsoletes:      libxfce4mcs < %{version}

%description -n %{libname}
This package contains the xfconf shared library.

%package -n libxfconf-devel
Summary:        Development Files for xfconf
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Provides:       libxfce4mcs-devel = %{version}
Obsoletes:      libxfce4mcs-devel < %{version}
Provides:       xfce-mcs-manager-devel = %{version}
Obsoletes:      xfce-mcs-manager-devel < %{version}

%description  -n libxfconf-devel
This package contains the files needed for developing applications using
xfconf.

# this should be replaced by %%lang_package once bnc#513786 is resolved
%package lang
Summary:        Languages for package %{name}
Group:          System/Localization
Requires:       %{libname} = %{version}
Provides:       %{name}-lang-all = %{version}
Supplements:    packageand(bundle-lang-other:%{libname})
BuildArch:      noarch

%description lang
Provides translations to the package %{name}

%prep
%autosetup -p1

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --disable-static \
    --with-helper-path-prefix=%{_libexecdir} \
    --enable-perl-bindings \
    --with-perl-options='NOECHO= OPTIMIZE="%{optflags}" CCDLFLAGS="-Wl,-E" INSTALLDIRS=vendor' \
    --enable-gtk-doc
%else
%configure \
    --disable-static \
    --with-helper-path-prefix=%{_libexecdir} \
    --enable-perl-bindings \
    --with-perl-options='NOECHO= OPTIMIZE="%{optflags}" CCDLFLAGS="-Wl,-E" INSTALLDIRS=vendor' \
    --enable-gtk-doc
%endif
%make_build

%install
%make_install
install -D -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/xfconf-query.1

rm -f %{buildroot}%{_libdir}/*.la \
    %{buildroot}%{perl_vendorarch}/auto/Xfce4/Xfconf/Xfconf.bs

%perl_process_packlist

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,ur_PK}

%find_lang %{name} %{?no_lang_C}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%doc AUTHORS NEWS TODO
%license COPYING
%{_bindir}/xfconf-query
%dir %{_libexecdir}/xfce4
%dir %{_libexecdir}/xfce4/xfconf
%{_libexecdir}/xfce4/xfconf/xfconfd
%{_datadir}/dbus-1/services/org.xfce.Xfconf.service
%doc %{_mandir}/man1/xfconf-query.1*

%files -n %{libname}
%license COPYING
%{_libdir}/libxfconf-*.so.*

%files lang -f %{name}.lang

%files -n libxfconf-devel
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/xfconf
%{_includedir}/xfce4
%{_libdir}/libxfconf-*.so
%{_libdir}/pkgconfig/libxfconf-*.pc

%files -n perl-xfconf
%doc %{_mandir}/man3/Xfce4::Xfconf.3pm*
%dir %{perl_vendorarch}/Xfce4
%{perl_vendorarch}/Xfce4/Xfconf
%{perl_vendorarch}/Xfce4/Xfconf.pm
%dir %{perl_vendorarch}/auto
%dir %{perl_vendorarch}/auto/Xfce4
%{perl_vendorarch}/auto/Xfce4/Xfconf

%changelog
