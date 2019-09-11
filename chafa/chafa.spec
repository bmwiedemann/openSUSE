#
# spec file for package chafa
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           chafa
Version:        1.2.1
Release:        0
Summary:        Image-to-text converter for terminal
License:        LGPL-3.0-or-later
Group:          Amusements/Toys/Graphics
URL:            https://hpjansson.org/chafa/
Source0:        https://github.com/hpjansson/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  ImageMagick-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libtool
Requires:       libchafa0 = %{version}

%description
Chafa is a command-line utility that converts all kinds of images, including
animated image formats like GIFs, into ANSI/Unicode character output that can
be displayed in a terminal.

%package -n libchafa0
Summary:        Shared library for %{name}
Group:          Development/Libraries/C and C++

%description -n libchafa0
Shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libchafa0 = %{version}

%description devel
Development files for %{name}.

%package doc
Summary:        Chafa documentation
Group:          Documentation/HTML
Recommends:     %{name}-devel

%description doc
Documentation for %{name}.

%prep
%setup -q
autoreconf -ivf

# rpath
sed -i -e 's|hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
       -e 's|runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
       -e "s|runpath_var='LD_RUN_PATH'|runpath_var=DIE_RPATH_DIE|g" \
    configure

%build
%configure --disable-rpath
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libdir}/libchafa.{a,la}

%post -n libchafa0 -p /sbin/ldconfig
%postun -n libchafa0 -p /sbin/ldconfig

%files
%license COPYING.LESSER
%doc AUTHORS README* NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n libchafa0
%doc AUTHORS
%license COPYING.LESSER
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.1.1

%files devel
%doc AUTHORS
%license COPYING.LESSER
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%files doc
%doc AUTHORS
%license COPYING.LESSER
%doc %{_datadir}/gtk-doc/html/%{name}

%changelog
