#
# spec file for package gtk2
#
# Copyright (c) 2025 SUSE LLC
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
%define gtk_binary_version 2.10.0
%define _name gtk
Name:           gtk2
Version:        2.24.33
Release:        0
# FIXME: when updating to next version, check whether we can remove the workaround for bgo#596977 below (removing -fomit-frame-pointer)
Summary:        The GTK+ toolkit library (version 2)
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://www.gtk.org/
#Source0:       http://download.gnome.org/sources/gtk+/2.24/%%{_name}-%%{version}.tar.xz
Source:         %{_name}-%{version}.tar.xz
Source1:        %{_name}-%{version}-po-upstream.tar.xz
Source2:        README.SUSE
Source3:        gtkrc
Source4:        baselibs.conf
Source5:        macros.gtk2
Source6:        %{_name}-%{version}-po-suse.tar.xz
Source99:       gtk2-rpmlintrc
# PATCH-FIX-OPENSUSE gtk2-GTK_PATH64.patch sbrabec@novell.com - 64-bit dual install. Use GTK_PATH64 environment variable instead of GTK_PATH
Patch0:         gtk2-GTK_PATH64.patch
# PATCH-FEATURE-UPSTREAM bugzilla-129753-gtk+-2.8.9-localize-font-style-name.diff bnc129753 bgo319484 mfabian@novell.com - Translate the font styles in the GUI
Patch1:         bugzilla-129753-gtk+-2.8.9-localize-font-style-name.diff
# PATCH-FIX-UPSTREAM gtk2-bnc130159-bgo319483-async-selection-in-gtk-font-selection.diff bnc130159 bgo319483 federico@novell.com - Load fonts asynchronously in GtkFontSelection to make it appear faster for CJK languages
Patch2:         gtk2-bnc130159-bgo319483-async-selection-in-gtk-font-selection.diff
# PATCH-FIX-OPENSUSE gtk-path-local.patch Search in /usr/local/%%{_lib} by default. bnc369696 bgo534474
Patch3:         gtk-path-local.patch
# PATCH-FIX-UPSTREAM gtk2-default-printer.patch bgo#577642 mgorse@suse.com -- Save selected printer as default
Patch4:         gtk2-default-printer.patch
# PATCH-FIX-UPSTREAM gtk2-bgo625202-30-bit-drawables-remain-black.patch bgo#625202 ku.b@gmx.de -- 30-bit drawables remain black
Patch5:         gtk2-bgo625202-30-bit-drawables-remain-black.patch
# PATCH-FIX-UPSTREAM gtk2-bgo743166-remember-printing-authentication.patch bgo#674264 joschibrauchle@gmx.de -- Credentials from gnome-keyring is not used while printing in GTK 2
Patch6:         gtk2-bgo743166-remember-printing-authentication.patch
# PATCH-FEATURE-OPENSUSE gtk2-updateiconcache_sort.patch olh@opensuse.org -- Have gtp-update-icon-cache sort the file list before producing a cache
Patch8:         gtk2-updateiconcache_sort.patch
# PATCH-FIX-UPSTREAM https://gitlab.gnome.org/GNOME/gtk/-/commit/c1fa916e88de20fc61dc06d3ff9f26722effa0df#note_1852594 -  Check for attribute availability before accessing it
Patch9:         gtk2-check-attribute.patch
# PATCH-FIX-UPSTREAM gtk2-gcc14.patch mgorse@suse.com -- fix building with gcc14.
Patch10:        gtk2-gcc14.patch
# PATCH-FIX-UPSTREAM CVE-2024-6655.patch -- CVE-2024-6655 Stop looking for modules in cwd
Patch11:        CVE-2024-6655.patch
# PATCH-FEATURE-OPENSUSE automake-1.17.patch -- Add automake 1.17 support to autogen.sh
Patch12:        automake-1.17.patch

BuildRequires:  cairo-devel
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libtiff-devel
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(atk)
# Needed for patches touching the build system / bootstrapping
BuildRequires:  libtool
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr) >= 1.2.99
BuildRequires:  pkgconfig(xrender)

%description
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package -n libgtk-2_0-0
Summary:        The GTK+ toolkit library (version 2)
# While hicolor is not a Requires strictly speaking, we put it as
# such instead of as a Recommends because many applications just
# assume it's there and we need to have a low-level package to
# bring it in.
Group:          System/Libraries
Requires:       hicolor-icon-theme
Requires(post): %{name}-tools >= 2.24.20
# gtk+ can work without branding/data/translations. Built in defaults will be used then.
Recommends:     %{name}-branding
Recommends:     %{name}-data = %{version}
Recommends:     gvfs
# Provide %%{name} to make the lang and immodules packages installable
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
# gail is part of gtk+ as of 2.13.x
Provides:       gail = 1.22.1
Obsoletes:      gail < 1.22.1
#

%description -n libgtk-2_0-0
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package -n typelib-1_0-Gtk-2_0
Summary:        Introspection bindings for the GTK+ toolkit library v2
Group:          System/Libraries

%description -n typelib-1_0-Gtk-2_0
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides the GObject Introspection bindings for GTK+.

%package immodule-amharic
Summary:        Amharic input method for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools >= 2.24.20
Requires(postun): %{name}-tools >= 2.24.20
Provides:       locale(%{name}:am)

%description immodule-amharic
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Amharic.

%package immodule-inuktitut
Summary:        Inuktitut input method for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools >= 2.24.20
Requires(postun): %{name}-tools >= 2.24.20
Provides:       locale(%{name}:iu)

%description immodule-inuktitut
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Inuktitut.

%package immodule-multipress
Summary:        Multipress input method for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools >= 2.24.20
Requires(postun): %{name}-tools >= 2.24.20

%description immodule-multipress
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method which allows text entry via the
multi-press method, as on a mobile phone.

%package immodule-thai
Summary:        Thai-Lao input method for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools >= 2.24.20
Requires(postun): %{name}-tools >= 2.24.20
Provides:       locale(%{name}:lo)
Provides:       locale(%{name}:th)

%description immodule-thai
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Thai-Lao.

%package immodule-tigrigna
Summary:        Tigrigna input methods for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools >= 2.24.20
Requires(postun): %{name}-tools >= 2.24.20
Provides:       %{name}-immodules-tigrigna = %{version}
Provides:       locale(%{name}:ti)
Obsoletes:      %{name}-immodules-tigrigna < %{version}

%description immodule-tigrigna
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides two input methods for Tigrigna.

%package immodule-vietnamese
Summary:        Vietnamese input method for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools >= 2.24.20
Requires(postun): %{name}-tools >= 2.24.20
Provides:       locale(%{name}:vi)

%description immodule-vietnamese
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method for Vietnamese.

%package immodule-xim
Summary:        X input method for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       %{name} = %{version}
Requires(post): %{name}-tools >= 2.24.20
Requires(postun): %{name}-tools >= 2.24.20
Provides:       locale(%{name}:ja)
Provides:       locale(%{name}:ko)
Provides:       locale(%{name}:th)
Provides:       locale(%{name}:zh)

%description immodule-xim
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package provides an input method based on the X Input Method.

%package tools
Summary:        Auxiliary utilities for the GTK+ toolkit library v2
Group:          System/Libraries

%description tools
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package data
Summary:        Data files for the GTK+ toolkit library v2
Group:          System/Libraries
BuildArch:      noarch

%description data
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package branding-upstream
Summary:        Upstream theme configuration for the GTK+ toolkit library v2
Group:          System/Libraries
Requires:       libgtk-2_0-0 = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: Provides /etc/gtk-2.0/gtkrc, to define default theme and icon theme.
#BRAND: Do not forget to add proper Requires in branding package if changing
#BRAND: those.

%description branding-upstream
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

%package devel
Summary:        Development files for the GTK+ toolkit library v2
Group:          Development/Libraries/X11
Requires:       libgtk-2_0-0 = %{version}
# gtk-builder-convert needs this.
Requires:       python3-xml
Requires:       typelib-1_0-Gtk-2_0 = %{version}
# gail is part of gtk+ as of 2.13.x
Provides:       gail-devel = 1.22.1
Obsoletes:      gail-devel < 1.22.1
Provides:       gtk2-doc = %{version}
Obsoletes:      gtk2-doc < %{version}
#

%description devel
GTK+ is a multi-platform toolkit for creating graphical user interfaces.
Offering a complete set of widgets, GTK+ is suitable for projects
ranging from small one-off projects to complete application suites.

This package contains the development files for GTK+ 2.x.

%lang_package

%prep
%setup -q -n %{_name}-%{version} -a1 -a6
%if "%{_lib}" == "lib64"
cp -a %{SOURCE2} .
# WARNING: This patch does not patch not installed demos and tests.
%patch -P 0 -p1
%endif

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
for TRANSLATIONS in upstream suse ; do
	cd $TRANSLATIONS
	for PO in */*.po ; do
		if test -f ../$PO ; then
			# Ignore plural form clash. It is a false error.
			msgcat --use-first $PO ../$PO -o ../$PO.new || :
			mv ../$PO.new ../$PO
		else
			ln $PO ../$PO
		fi
	done
	cd -
done
cd po
ls -1 *.po | sed 's/\.po//g' >LINGUAS
# Trick: Handle incomplete translations that have no po-properties.
# Create a dumb copy, then delete the installed file.
cd ..
ln po/{en,lg,zu}.po po-properties/

%build
NOCONFIGURE=1 ./autogen.sh
export CFLAGS="%{optflags}"
export CFLAGS="$CFLAGS -fstack-protector -std=gnu99"
%ifarch ppc64
export CFLAGS="$CFLAGS -mminimal-toc"
%endif
# fix crash in gdm, nautilus, etc. (bgo#596977)
export CFLAGS=`echo $CFLAGS | sed -e 's/-fomit-frame-pointer//g'`
%configure \
        --disable-static \
        --enable-man \
        --with-xinput=xfree \
        --enable-introspection \
        --enable-gtk-doc
make %{?_smp_mflags}
cd po
# en.po is special and we want only key names there.
mv en.po en.po.save
make %{?_smp_mflags} update-po
mv en.po.save en.po
cd ../po-properties
make %{?_smp_mflags} update-po

%install
%make_install
rm %{buildroot}%{_datadir}/locale/{en,lg,zu}/LC_MESSAGES/gtk20-properties.mo
find %{buildroot} -type f -name "*.la" -delete -print
%if 0%{?suse_version} <= 1130
rm %{buildroot}%{_datadir}/locale/kg/LC_MESSAGES/*
%endif
%find_lang gtk20
%find_lang gtk20-properties
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/gtk-2.0
touch %{buildroot}%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules.cache
%if "%{_lib}" == "lib64"
  mv %{buildroot}%{_bindir}/gtk-query-immodules-2.0 %{buildroot}%{_bindir}/gtk-query-immodules-2.0-64
%endif
# drop gtk-update-icon-cache tool - GTK2 is old enough to be able to rely on GTK3 doing the caching
rm %{buildroot}%{_bindir}/gtk-update-icon-cache %{buildroot}%{_mandir}/man1/gtk-update-icon-cache.1
# Install rpm macros
mkdir -p %{buildroot}%{_rpmmacrodir}
cp %{SOURCE5} %{buildroot}%{_rpmmacrodir}
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}
%python3_fix_shebang

###########################################################################
# Note: when updating scriptlets, don't forget to also update baselibs.conf
###########################################################################

# Convenient %%define for the scriplets
%if "%{_lib}" == "lib64"
%define _gtk_query_immodules %{_bindir}/gtk-query-immodules-2.0-64
%else
%define _gtk_query_immodules %{_bindir}/gtk-query-immodules-2.0
%endif
%define _gtk_query_immodules_update_cache %{_gtk_query_immodules} --update-cache

%post -n libgtk-2_0-0
/sbin/ldconfig
%if 0
# In case libgtk-2_0-0 gets installed before gtk2-tools, we don't want to fail.
# So we make the call to gtk-query-immodules-2.0 dependent on the existence of
# the binary. This is why we also have a %%post for gtk2-tools.
%endif
if test -f %{_gtk_query_immodules}; then
  %{_gtk_query_immodules_update_cache}
fi

%post immodule-amharic
%{_gtk_query_immodules_update_cache}

%post immodule-inuktitut
%{_gtk_query_immodules_update_cache}

%post immodule-multipress
%{_gtk_query_immodules_update_cache}

%post immodule-thai
%{_gtk_query_immodules_update_cache}

%post immodule-tigrigna
%{_gtk_query_immodules_update_cache}

%post immodule-vietnamese
%{_gtk_query_immodules_update_cache}

%post immodule-xim
%{_gtk_query_immodules_update_cache}

%post tools
%if 0
# If we install gtk2-tools for the first time, then we should run it in case
# libgtk-2_0-0 was installed first (ie, if
# %%{_libdir}/gtk-2.0/%%{gtk_binary_version} already exists) which means
# gtk-query-immodules-2.0 couldn't run there.
%endif
if [ $1 = 1 ]; then
  test -d %{_libdir}/gtk-2.0/%{gtk_binary_version}
  if test $? -eq 0; then
    %{_gtk_query_immodules_update_cache}
  fi
fi

%if 0
# No need to call gtk-query-immodules-2.0 in postun:
# - if it's an upgrade, it will have been called in post
# - if it's an uninstall, we don't care about this anymore
%endif

%postun -n libgtk-2_0-0 -p /sbin/ldconfig

%postun immodule-amharic
%{_gtk_query_immodules_update_cache}

%postun immodule-inuktitut
%{_gtk_query_immodules_update_cache}

%postun immodule-multipress
%{_gtk_query_immodules_update_cache}

%postun immodule-thai
%{_gtk_query_immodules_update_cache}

%postun immodule-tigrigna
%{_gtk_query_immodules_update_cache}

%postun immodule-vietnamese
%{_gtk_query_immodules_update_cache}

%postun immodule-xim
%{_gtk_query_immodules_update_cache}

%files -n libgtk-2_0-0
%license COPYING
%doc AUTHORS NEWS
%if "%{_lib}" == "lib64"
%doc README.SUSE
%endif
%dir %{_sysconfdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/%{gtk_binary_version}
%dir %{_libdir}/gtk-2.0/%{gtk_binary_version}/engines
%{_libdir}/gtk-2.0/%{gtk_binary_version}/engines/libpixmap.so
%dir %{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-cedilla.so
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-cyrillic-translit.so
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-ipa.so
%dir %{_libdir}/gtk-2.0/%{gtk_binary_version}/printbackends
%{_libdir}/gtk-2.0/%{gtk_binary_version}/printbackends/libprintbackend-cups.so
%{_libdir}/gtk-2.0/%{gtk_binary_version}/printbackends/libprintbackend-file.so
%{_libdir}/gtk-2.0/%{gtk_binary_version}/printbackends/libprintbackend-lpr.so
%ghost %{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules.cache
%dir %{_libdir}/gtk-2.0/modules
%{_libdir}/gtk-2.0/modules/libgail.so
%{_libdir}/libgailutil.so.*
%{_libdir}/libgdk-x11-2.0.so.*
%{_libdir}/libgtk-x11-2.0.so.*

%files -n typelib-1_0-Gtk-2_0
%{_libdir}/girepository-1.0/Gdk-2.0.typelib
%{_libdir}/girepository-1.0/GdkX11-2.0.typelib
%{_libdir}/girepository-1.0/Gtk-2.0.typelib

%files immodule-amharic
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-am-et.so

%files immodule-inuktitut
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-inuktitut.so

%files immodule-multipress
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-multipress.so
%config %{_sysconfdir}/gtk-2.0/im-multipress.conf

%files immodule-thai
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-thai.so

%files immodule-tigrigna
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-ti-er.so
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-ti-et.so

%files immodule-vietnamese
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-viqr.so

%files immodule-xim
%{_libdir}/gtk-2.0/%{gtk_binary_version}/immodules/im-xim.so

%files tools
%{_bindir}/gtk-query-immodules-2.0*
%{_mandir}/man1/gtk-query-immodules-2.0*.1%{?ext_man}

%files data
%{_datadir}/themes/Default/
%{_datadir}/themes/Emacs/
%{_datadir}/themes/Raleigh/

%files branding-upstream
%config %{_sysconfdir}/gtk-2.0/gtkrc

%files lang -f gtk20.lang -f gtk20-properties.lang

%files devel
%doc %{_datadir}/gtk-doc/html/gail-libgail-util/
%doc %{_datadir}/gtk-doc/html/gdk2/
%doc %{_datadir}/gtk-doc/html/gtk2/
%{_bindir}/gtk-builder-convert
%{_bindir}/gtk-demo
%{_mandir}/man1/gtk-builder-convert.1*
%{_datadir}/aclocal/gtk-2.0.m4
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gtk-2.0
%{_datadir}/gtk-2.0/demo/
%{_includedir}/gail-1.0/
%{_includedir}/gtk-2.0/
%{_includedir}/gtk-unix-print-2.0/
%{_libdir}/gtk-2.0/include/
%{_libdir}/gtk-2.0/modules/libferret.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libgailutil.so
%{_libdir}/libgdk-x11-2.0.so
%{_libdir}/libgtk-x11-2.0.so
%{_rpmmacrodir}/macros.gtk2

%changelog
