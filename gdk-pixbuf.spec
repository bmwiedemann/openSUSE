#
# spec file for package gdk-pixbuf
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


# When updating the binary version, do not forget to also update baselibs.conf
%define gdk_pixbuf_binary_version 2.10.0

Name:           gdk-pixbuf
Version:        2.40.0
Release:        0
Summary:        An image loading library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://www.gnome.org/

# A filefrom the test suite is correctly identified by clamav to be a
# malicious BC.Gif.Exploit.Agent-1425366.Agent. This is an intentional part of
# the test suite to ensure it has no negative side effects. Change the Source0
# from tar.xz to zip to bypass clamav scanning on SLE.
Source0:        %{name}-%{version}.zip
Source1:        macros.gdk-pixbuf
Source2:        README.SUSE
Source3:        gdk-pixbuf-rpmlintrc
Source99:       baselibs.conf

# PATCH-FIX-UPSTREAM gdk-pixbuf-boo1174307-io-gif-overflow.patch boo#1174307 glgo#GNOME/gdk-pixbuf#132 zcjia@suse.com -- Avoid overflows by checking the memset length argument
Patch0:         gdk-pixbuf-boo1174307-io-gif-overflow.patch

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gtk-doc
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  unzip
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)

%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
Clutter.

%package -n libgdk_pixbuf-2_0-0
Summary:        An image loading library
# Provide %%{name} to make the lang package installable
Group:          System/Libraries
Requires(post): gdk-pixbuf-query-loaders
Conflicts:      gtk2 < 2.21.3
Provides:       %{name} = %{version}

%description  -n libgdk_pixbuf-2_0-0
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
Clutter.

%package -n typelib-1_0-GdkPixbuf-2_0
Summary:        Introspection bindings for gdk-pixbuf
Group:          System/Libraries

%description -n typelib-1_0-GdkPixbuf-2_0
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
Clutter.

This package provides the GObject Introspection bindings for gdk-pixbuf.

%package -n typelib-1_0-GdkPixdata-2_0
Summary:        Introspection bindings for gdk-pixdata
Group:          System/Libraries

%description -n typelib-1_0-GdkPixdata-2_0
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
Clutter.

This package provides the GObject Introspection bindings for gdk-pixdata.

%package query-loaders
Summary:        Utility to create a cache of gdk-pixbuf loaders
Group:          System/X11/Utilities

%description query-loaders
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
Clutter.

This package contains the utility to create the cache file needed for
loadable modules.

%package thumbnailer
Summary:        System helper creating thumbnails
Group:          System/X11/Utilities
Supplements:    libgdk_pixbuf-2_0-0

%description thumbnailer
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
Clutter.

This package contains the thumbnailer utility.

%package devel
Summary:        Development files for gdk-pixbuf, an image loading library
Group:          Development/Languages/C and C++
Requires:       libgdk_pixbuf-2_0-0 = %{version}
Requires:       typelib-1_0-GdkPixbuf-2_0 = %{version}
Requires:       typelib-1_0-GdkPixdata-2_0 = %{version}

%description devel
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
Clutter.

This package contains the development files for gdk-pixbuf.

%lang_package

%prep
%setup -c -T -q
unzip -P gecko %{SOURCE0}
translation-update-upstream
%patch0 -p1
%if "%{_lib}" == "lib64"
cp -a %{SOURCE2} .
%endif

%build
%meson \
	-Dpng=true \
	-Dtiff=true \
	-Djpeg=true \
	-Djasper=false \
	-Dx11=true \
	-Dbuiltin_loaders=none \
	-Ddocs=true \
	-Dgir=true \
	-Dman=true \
	-Drelocatable=false \
	-Dnative_windows_loaders=false \
	-Dinstalled_tests=false \
	%{nil}
%meson_build

%install
%meson_install
rm -rf %{buildroot}{%{_libexecdir},%{_datadir}}/installed-tests/
%find_lang %{name}
touch %{buildroot}%{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders.cache
%if "%{_lib}" == "lib64"
  mv %{buildroot}%{_bindir}/gdk-pixbuf-query-loaders %{buildroot}%{_bindir}/gdk-pixbuf-query-loaders-64
  mv %{buildroot}%{_mandir}/man1/gdk-pixbuf-query-loaders.1 %{buildroot}%{_mandir}/man1/gdk-pixbuf-query-loaders-64.1
%endif
# Install rpm macros
mkdir -p %{buildroot}%{_rpmmacrodir}
cp %{SOURCE1} %{buildroot}%{_rpmmacrodir}

#############################################################################
# Note: when updating scriptlets, don't forget to also update baselibs.conf #
#############################################################################

# Convenient %%define for the scriplets
%if "%{_lib}" == "lib64"
%define _gdk_pixbuf_query_loaders %{_bindir}/gdk-pixbuf-query-loaders-64
%else
%define _gdk_pixbuf_query_loaders %{_bindir}/gdk-pixbuf-query-loaders
%endif
%define _gdk_pixbuf_query_loaders_update_cache %{_gdk_pixbuf_query_loaders} --update-cache

%post -n libgdk_pixbuf-2_0-0
/sbin/ldconfig
%if 0
# In case libgdk_pixbuf-2_0-0 gets installed before gdk-pixbuf-query-loaders,
# we don't want to fail. So we make the call to gdk-pixbuf-query-loaders
# dependent on the existence of the binary. This is why we also have a %%post
# for gdk-pixbuf-query-loaders.
%endif
if test -f %{_gdk_pixbuf_query_loaders}; then
  %{_gdk_pixbuf_query_loaders_update_cache}
fi

%post query-loaders
%if 0
# If we install gdk-pixbuf-query-loaders for the first time, then we should run
# it in case libgdk_pixbuf-2_0-0 was installed first (ie, if
# %%{_libdir}/gdk-pixbuf-2.0/%%{gdk_pixbuf_binary_version} already exists) which
# means gdk-pixbuf-query-loaders couldn't run there.
%endif
if [ $1 = 1 ]; then
  test -d %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}
  if test $? -eq 0; then
    %{_gdk_pixbuf_query_loaders_update_cache}
  fi
fi

%if 0
# No need to call gdk-pixbuf-query-loaders in postun:
# - if it's an upgrade, it will have been called in post
# - if it's an uninstall, we don't care about this anymore
%endif

%postun -n libgdk_pixbuf-2_0-0 -p /sbin/ldconfig

%files -n libgdk_pixbuf-2_0-0
%license COPYING
%doc NEWS
%if "%{_lib}" == "lib64"
%doc README.SUSE
%endif
%{_libdir}/libgdk_pixbuf-2.0.so.0*
%{_libdir}/libgdk_pixbuf_xlib-2.0.so.0*
%dir %{_libdir}/gdk-pixbuf-2.0
%dir %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}
%dir %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders
%{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders/*.so
%ghost %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders.cache

%files -n typelib-1_0-GdkPixbuf-2_0
%{_libdir}/girepository-1.0/GdkPixbuf-2.0.typelib

%files -n typelib-1_0-GdkPixdata-2_0
%{_libdir}/girepository-1.0/GdkPixdata-2.0.typelib

%files query-loaders
%{_bindir}/gdk-pixbuf-query-loaders*
%{_mandir}/man1/gdk-pixbuf-query-loaders*.1*

%files thumbnailer
%{_bindir}/gdk-pixbuf-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer

%files devel
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-pixdata
%{_mandir}/man1/gdk-pixbuf-csource.1*
%{_includedir}/gdk-pixbuf-2.0
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/GdkPixbuf-2.0.gir
%{_datadir}/gir-1.0/GdkPixdata-2.0.gir
%doc %{_datadir}/gtk-doc/html/gdk-pixbuf
%{_rpmmacrodir}/macros.gdk-pixbuf

%files lang -f %{name}.lang

%changelog
