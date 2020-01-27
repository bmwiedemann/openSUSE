#
# spec file for package dasher
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


Name:           dasher
Version:        4.11
Release:        0
Summary:        Zooming Predictive Text Entry System
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.inference.phy.cam.ac.uk/dasher/
Source0:        ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/4.5/%{name}-%{version}.tar.bz2
Source1:        dasher-data-lang.sh
Source2:        locale-map.txt
# PATCH-FIX-UPSTREAM dasher-linkX11.patch bgo#657306 dimstar@opensuse.org -- Remove unneded code requiring to link against libX11.
Patch0:         dasher-linkX11.patch
# PATCH-FIX-UPSTREAM dasher-gcc6.patch boo#985108 dimstar@opensuse.org -- Fix build with gcc 6 (bool can't be used as return value for functions returning string)
Patch1:         dasher-gcc6.patch
BuildRequires:  cairo-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gconf2-devel
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libexpat-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xtst)
Recommends:     %{name}-data-recommended
Suggests:       %{name}-data-extras
%{gconf_schemas_prereq}

%description
Dasher is a zooming predictive text entry system, designed for
situations where keyboard input is impractical (for instance:
accessibility or PDAs). It is usable with greatly limited amounts of
physical input while still allowing high rates of text entry.

%package data-recommended
Summary:        Zooming Predictive Text Entry System -- Data files for common languages
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Provides:       locale(%{name}:de;ru;it;pl;es;pt;fr;nl)
BuildArch:      noarch

%description data-recommended
Dasher is a zooming predictive text entry system, designed for
situations where keyboard input is impractical (for instance:
accessibility or PDAs). It is usable with greatly limited amounts of
physical input while still allowing high rates of text entry.

This package contains data files to use dasher with common languages.

%package data-extras
Summary:        Zooming Predictive Text Entry System -- Data files for additional languages
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Provides:       locale(%{name}:ada;af;ak;am;ar;as;az;be;bg;bn;br;bs;ca;chr;co;cs;cy;da;dv;ee;el;eo;et;eu;fa;fi;fo;gaa;gd;gez;gl;gu;ha;haw;he;hi;hr;hu;hy;id;ig;is;ja;ka;kk;kn;ko;ku;ky;la;lb;lo;lt;lv;mk;ml;mn;mr;ms;mt;my;ne;no;nr;nso;oc;om;or;pa;ps;rm;rn;ro;sa;se;si;sk;sl;so;sq;sr;ss;st;sv;sw;ta;te;tg;th;ti;tk;tl;tn;tr;ts;uk;ur;uz;ve;vi;xh;yo;zh;zu)
BuildArch:      noarch

%description data-extras
Dasher is a zooming predictive text entry system, designed for
situations where keyboard input is impractical (for instance:
accessibility or PDAs). It is usable with greatly limited amounts of
physical input while still allowing high rates of text entry.

This package contains data files to use dasher with additional languages.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
translation-update-upstream
cp %{SOURCE2} .

%build
%configure --with-pic \
    --with-gnome \
    --disable-scrollkeeper \
    --disable-a11y
make %{?_smp_mflags}

%install
%make_install
%if 0%{?suse_version} <= 1120
rm %{buildroot}%{_datadir}/locale/en@shaw/LC_MESSAGES/*
%endif
%suse_update_desktop_file -G "Text Entry Tool" %{name} GNOME
%find_lang %{name} %{?no_lang_C}
%find_gconf_schemas
sh %{SOURCE1} %{buildroot} "%{_datadir}" %{name}-data-recommended.lst %{name}-data-extras.lst %{name}-excluded.lst
%fdupes %{buildroot}

%pre -f %{name}.schemas_pre
%post
%desktop_database_post
%icon_theme_cache_post

%posttrans -f %{name}.schemas_posttrans
%preun -f %{name}.schemas_preun
%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f %{name}.schemas_list -f %{name}-excluded.lst
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%dir %{_datadir}/gnome/
%dir %{_datadir}/gnome/help/
%dir %{_datadir}/gnome/help/%{name}/
%doc %{_datadir}/gnome/help/%{name}/C/
%dir %{_datadir}/omf/
%dir %{_datadir}/omf/%{name}/
%doc %{_datadir}/omf/%{name}/%{name}-C.omf
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/dasher
%{_datadir}/icons/hicolor/48x48/apps/dasher.png
%{_datadir}/icons/hicolor/scalable/apps/dasher.svg
%{_mandir}/man?/*%{ext_man}

%files data-recommended -f %{name}-data-recommended.lst

%files data-extras -f %{name}-data-extras.lst

%files lang -f %{name}.lang

%changelog
