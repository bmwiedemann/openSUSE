#
# spec file for package gcompris
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


Name:           gcompris
Version:        17.05
Release:        0
Summary:        Multiactivity educational software for children aged 2–10
License:        GPL-3.0-or-later
Group:          Amusements/Teaching/Other
URL:            http://gcompris.net
Source0:        %{name}-%{version}.tar.bz2
Source1:        gcompris.desktop
Source2:        gcompris-edit.desktop
Source3:        gcompris-rpmlintrc
Source4:        gcompris.6

# PATCH-FIX-UPSTREAM gcompris-13.11-remove_build_date.patch -- Make build reproducible
Patch1:         gcompris-13.11-remove_build_date.patch
# PATCH-FIX-UPSTREAM gcompris-gstreamer-1.0.patch bgo#747949 deb#785840 badshah400@gmail.com -- Port to gstreamer 1.0; patch taken from debian patch tracker
Patch2:         gcompris-gstreamer-1.0.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  gnuchess >= 5.02
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel >= 3
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pycairo)
BuildRequires:  pkgconfig(pygtk-2.0)
Requires:       gcompris-voices >= %{version}
Requires:       gnucap
Requires:       gnuchess
Requires:       tuxpaint
# to get rid of the "GLib-GIO-WARNING **: FAMOpen failed, FAMErrno=0" messages,
# we need a running FAM server (not mandatory):
Recommends:     fam-server

%description
GCompris is an educational software suite comprising of numerous activities
for children aged 2 to 10. Some of the activities are game orientated,  but
nonetheless still educational. Below you can find a list of categories with
some of the activities available in that category.

-  computer discovery: keyboard, mouse, different mouse gesture, ...
-  algebra: table memory, enumeration, double entry table, mirror image, ...
-  science: the canal lock, the water cycle, the submarine, electric simulation ...
-  geography: place the country on the map
-  games: chess, memory, connect 4, oware, sudoku ...
-  reading: reading practice
-  other: learn to tell time, puzzle of famous paintings, vector drawing, ...

Currently, GCompris offers in excess of 80 activities.

%package devel
Summary:        Development package for gcompris
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains header files for developing new applications with gcompris.

%package voices-ar
Summary:        GCompris voices in Arabic
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:ar)
BuildArch:      noarch

%description voices-ar
Arabic voices for the GCompris game.

%package voices-br
Summary:        GCompris voices in Breton
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:br)
BuildArch:      noarch

%description voices-br
Breton voices for the GCompris game.

%package voices-cs
Summary:        GCompris voices in Czech
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:cs)
BuildArch:      noarch

%description voices-cs
Czech voices for the GCompris game.

%package voices-da
Summary:        GCompris voices in Danish
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:da)
BuildArch:      noarch

%description voices-da
Danish voices for the GCompris game.

%package voices-de
Summary:        GCompris voices in German
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:de)
BuildArch:      noarch

%description voices-de
German voices for the GCompris game.

%package voices-el
Summary:        GCompris voices in Greek
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:el)
BuildArch:      noarch

%description voices-el
Greek voices for the GCompris game.

%package voices-en
Summary:        GCompris voices in English
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:en)
BuildArch:      noarch

%description voices-en
English voices for the GCompris game.

%package voices-es
Summary:        GCompris voices in Spanish
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:es)
BuildArch:      noarch

%description voices-es
Spanish voices for the GCompris game.

%package voices-eu
Summary:        GCompris voices in Basque
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:eu)
BuildArch:      noarch

%description voices-eu
Basque voices for the GCompris game

%package voices-fi
Summary:        GCompris voices in Finnish
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:fi)
BuildArch:      noarch

%description voices-fi
Finish voices for the GCompris game.

%package voices-fr
Summary:        GCompris voices in French
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:fr)
BuildArch:      noarch

%description voices-fr
French voices for the GCompris game.

%package voices-hi
Summary:        GCompris voices in Hindi
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:hi)
BuildArch:      noarch

%description voices-hi
Hindi voices for the GCompris game.

%package voices-hu
Summary:        GCompris voices in Hungarian
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:hu)
BuildArch:      noarch

%description voices-hu
Hungarian voices for the GCompris game.

%package voices-id
Summary:        GCompris voices in Indonesian
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:id)
BuildArch:      noarch

%description voices-id
Indonesian voices for the GCompris game.

%package voices-it
Summary:        GCompris voices in Italian
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:it)
BuildArch:      noarch

%description voices-it
Italian voices for the GCompris game.

%package voices-nb
Summary:        GCompris voices in Norwegian
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:nb)
BuildArch:      noarch

%description voices-nb
Norwegian voices for the GCompris game.

%package voices-nl
Summary:        GCompris voices in Dutch
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:nl)
BuildArch:      noarch

%description voices-nl
Dutch voices for the GCompris game.

%package voices-mr
Summary:        GCompris voices in Marathi
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:mr)
BuildArch:      noarch

%description voices-mr
Marathi voices for the GCompris game.

%package voices-pt
Summary:        GCompris voices in Portuguese
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:pt_PT)
BuildArch:      noarch

%description voices-pt
Portuguese voices for the GCompris game.

%package voices-pt-br
Summary:        GCompris voices in Brazilian Portuguese
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:pt_BR)
BuildArch:      noarch

%description voices-pt-br
Brazilian Portuguese voices for the GCompris game.

%package voices-ru
Summary:        GCompris voices in Russian
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:ru)
BuildArch:      noarch

%description voices-ru
Russian voices for the GCompris game.

%package voices-so
Summary:        GCompris voices in Somali
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:so)
BuildArch:      noarch

%description voices-so
Somali voices for the GCompris game.

%package voices-sr
Summary:        GCompris voices in Serbian
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:sr)
BuildArch:      noarch

%description voices-sr
Serbian voices for the GCompris game.

%package voices-sv
Summary:        GCompris voices in Swedish
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:sv)
BuildArch:      noarch

%description voices-sv
Swedish voices for the GCompris game.

%package voices-tr
Summary:        GCompris voices in Turkish
Group:          Amusements/Teaching/Other
Requires:       %{name} = %{version}
Provides:       gcompris-voices = %{version}
Provides:       locale(gcompris:tr)
BuildArch:      noarch

%description voices-tr
Turkish voices for the GCompris game.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
find . -name ".cvsignore" -delete
find . -name ".gitignore" -delete
# wrong-file-end-of-line-encoding
#sed -i "s|||g" ./docs/eu/topic.dat

%build
# workaround for missing config.rpath
if [ -f /usr/share/gettext/config.rpath -a ! -f config.rpath ] ; then
    cp -v /usr/share/gettext/config.rpath .
fi
autoreconf -fiv
%configure --quiet \
           --enable-sqlite \
           --disable-static \
           --localstatedir=%{_localstatedir}/%{_lib}
#            --enable-sugar
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
make DESTDIR=%{?buildroot:%{buildroot}} install
test -f %{buildroot}/%{_infodir}/dir && rm -f %{buildroot}/%{_infodir}/dir
#
# install man page
#
install -Dm644 %{SOURCE4} %{buildroot}%{_mandir}/man6/%{name}.6
#
# install desktop files
#
mkdir -p %{buildroot}/%{_datadir}/{pixmaps,applications}/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/

if [ ! -f %{buildroot}%{_datadir}/pixmaps/gcompris.png ]; then
	for png in gcompris.png gcompris-edit.png; do
		mv -v %{buildroot}/%{_datadir}/pixmaps/$png %{buildroot}%{_datadir}/pixmaps/
	done
	rm -rf %{buildroot}/%{_datadir}/pixmaps
fi

%suse_update_desktop_file -n -N GCompris -G "Educational suite GCompris" gcompris Education Teaching
%suse_update_desktop_file -n -N GCompris -G "GCompris Administration" gcompris-edit System SystemSetup
# remove old menu entry
rm -rf %{buildroot}/%{_libexecdir}/menu/gcompris
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

test -f %{buildroot}%{_datadir}/gcompris/boards/voices/recode.sh && chmod +x %{buildroot}%{_datadir}/gcompris/boards/voices/recode.sh
# fix old LOCALE dir
if [ -d %{buildroot}%{_datadir}/locale/sr@Latn ]; then
	mv %{buildroot}%{_datadir}/locale/sr@Latn %{buildroot}%{_datadir}/locale/sr@latin
fi

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%doc %{_mandir}/man6/gcompris*
%dir %{_libdir}/gcompris
%dir %{_datadir}/gcompris
%dir %{_datadir}/appdata
%{_datadir}/applications/*gcompris-edit.desktop
%{_datadir}/applications/*gcompris.desktop
%{_datadir}/pixmaps/*.png
%{_libdir}/gcompris/*.so.*
%{_libdir}/gcompris/*.so
%exclude %{_libdir}/gcompris/libgoocanvas.so
%{_datadir}/appdata/gcompris.appdata.xml
%{_datadir}/gcompris/boards
%{_datadir}/gcompris/python
%{_bindir}/*
%exclude %{_datadir}/gcompris/boards/voices/[a-z][a-z]
%exclude %{_datadir}/gcompris/boards/voices/pt_BR

%files devel
%{_libdir}/gcompris/libgoocanvas.so

%files voices-ar
%{_datadir}/gcompris/boards/voices/ar

%files voices-br
%{_datadir}/gcompris/boards/voices/br

%files voices-cs
%{_datadir}/gcompris/boards/voices/cs

%files voices-da
%{_datadir}/gcompris/boards/voices/da

%files voices-de
%{_datadir}/gcompris/boards/voices/de

%files voices-el
%{_datadir}/gcompris/boards/voices/el

%files voices-en
%{_datadir}/gcompris/boards/voices/en

%files voices-es
%{_datadir}/gcompris/boards/voices/es

%files voices-eu
%{_datadir}/gcompris/boards/voices/eu

%files voices-fi
%{_datadir}/gcompris/boards/voices/fi

%files voices-fr
%{_datadir}/gcompris/boards/voices/fr

%files voices-hi
%{_datadir}/gcompris/boards/voices/hi

%files voices-hu
%{_datadir}/gcompris/boards/voices/hu

%files voices-id
%{_datadir}/gcompris/boards/voices/id

%files voices-it
%{_datadir}/gcompris/boards/voices/it

%files voices-mr
%{_datadir}/gcompris/boards/voices/mr

%files voices-nb
%{_datadir}/gcompris/boards/voices/nb

%files voices-nl
%{_datadir}/gcompris/boards/voices/nl

%files voices-pt
%{_datadir}/gcompris/boards/voices/pt

%files voices-pt-br
%{_datadir}/gcompris/boards/voices/pt_BR

%files voices-ru
%{_datadir}/gcompris/boards/voices/ru

%files voices-so
%{_datadir}/gcompris/boards/voices/so

%files voices-sr
%{_datadir}/gcompris/boards/voices/sr

%files voices-sv
%{_datadir}/gcompris/boards/voices/sv

%files voices-tr
%{_datadir}/gcompris/boards/voices/tr

%changelog
