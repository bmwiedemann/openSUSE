#
# spec file for package bluefish
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bluefish
Version:        2.2.10
Release:        0
Summary:        A feature-Rich HTML Editor
License:        GPL-3.0+
Group:          Productivity/Publishing/HTML/Editors
Url:            http://bluefish.openoffice.nl/
Source0:        http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2
Source1:        http://www.bennewitz.com/bluefish/stable/source/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE remove-python-class-shebang.patch - Remove unneeded shebang from python class files.
Patch0:         remove-python-class-shebang.patch
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  jing
BuildRequires:  man
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  tidy
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.24
BuildRequires:  pkgconfig(glib-2.0) >= 2.24
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.24
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.2.2
BuildRequires:  pkgconfig(gucharmap-2.90)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(python)
Requires:       sgml-skel
Recommends:     libxml2-tools
Recommends:     make
Provides:       bluefish-unstable = %{version}-%{release}
Obsoletes:      bluefish-unstable < 2.2.3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Bluefish is a HTML editor designed for the experienced Web designer
(supports HTML, PHP, Java, Perl, Python, Ruby, C, Pascal and more).

It is based on Gtk+.

%prep
%setup -q
%patch0 -p1

%build
# avoid aliasing warnings
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure  --with-icon-path=%{_datadir}/pixmaps \
            --disable-update-databases \
            --disable-xml-catalog-update \
            --enable-python
make %{?_smp_mflags} bflangsampledir="%{_docdir}/%{name}"

%install
%make_install \
             bflangsampledir="%{_docdir}/%{name}" \
             UPDATE_DESKTOP=echo \
             UPDATE_MIME=echo

%suse_update_desktop_file -r bluefish Application Network WebDevelopment GNOME
%fdupes %{buildroot}%{_datadir}

%find_lang bluefish
%find_lang bluefish_plugin_about
%find_lang bluefish_plugin_charmap
%find_lang bluefish_plugin_entities
%find_lang bluefish_plugin_htmlbar
%find_lang bluefish_plugin_infbrowser
%find_lang bluefish_plugin_snippets
%find_lang bluefish_plugin_zencoding
cat bluefish*.lang >> all.lang

%post
%mime_database_post
%desktop_database_post
if [ -x %{_bindir}/xmlcatalog ]; then
	%{_bindir}/xmlcatalog --noout --add \
         'delegateURI' \
         'http://bluefish.openoffice.nl/ns/bflang/2.0/' \
         '%{_datadir}/xml/bluefish' \
         '%{_sysconfdir}/xml/catalog' || :
fi

%preun
if [ -x %{_bindir}/xmlcatalog ]; then
	%{_bindir}/xmlcatalog --noout --del \
         'http://bluefish.openoffice.nl/ns/bflang/2.0/' \
         '%{_sysconfdir}/xml/catalog' || :
fi

%postun
%mime_database_postun
%desktop_database_postun

%files -f all.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README TODO
%{_docdir}/%{name}
%{_mandir}/man1/bluefish.1*
%dir %{_datadir}/xml/bluefish
%dir %{_datadir}/xml/bluefish/2.0
%{_libdir}/%{name}
%{_bindir}/bluefish
%{_datadir}/bluefish
%{_datadir}/pixmaps/*bluefish*.png
%{_datadir}/applications/bluefish*.desktop
%{_datadir}/xml/bluefish/2.0/bflang2.rng
%{_datadir}/xml/bluefish/catalog.xml
%{_datadir}/icons/hicolor/*/*/*
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/mime/packages/%{name}.xml

%changelog
