#
# spec file for package stardict
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{?suse_version} >= 1500
%define espeakdev espeak-ng-compat-devel
%else
%define espeakdev espeak-devel
%endif
Name:           stardict
Version:        3.0.7
Release:        0
Summary:        A powerful cross-platform dictionary written in GTK+3
License:        GPL-3.0-only
Group:          Productivity/Office/Dictionary
URL:            https://stardict-4.sourceforge.net/
Source0:        http://download.sourceforge.net/stardict-4/%{name}-%{version}-2-src.7z#/%{name}-%{version}.7z
# PATCH-FIX-OPENSUSE stardict-3.0.3-fix-path-for-sounds.patch -- adjust default path for sound files
Patch0:         stardict-3.0.3-fix-path-for-sounds.patch
# PATCH-FIX-OPENSUSE stardict-3.0.3-improve-desktop-file.patch -- add GenericName entry
Patch1:         stardict-3.0.3-improve-desktop-file.patch
# PATCH-FIX-UPSTREAM stardict-drop-autotools-gconf.patch badshah400@gmail.com -- Drop unnecessary and no longer supported autotools gconf macro
Patch2:         stardict-drop-autotools-gconf.patch
BuildRequires:  %{espeakdev}
BuildRequires:  7zip
BuildRequires:  fdupes
BuildRequires:  flite-devel
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(zlib)

%description
StarDict is a cross-platform and international dictionary written in GTK+3.

It has features such as "Glob-style pattern matching", "Scan
selection word" and "Fuzzy query".

%lang_package

%prep
%autosetup -p1

# Remove unneeded sigc++ header files to make it sure
# that we are using system-wide libsigc++
find dict/src/sigc++* -name "*.h" -or -name "*.cc" -delete

%build
# Hack: There are innumerable `const char *` to `char *` conversions
export CFLAGS="%{optflags} -fpermissive"
export CXXFLAGS="%{optflags} -fpermissive"
NOCONFIGURE=1 ./autogen.sh
%configure \
           --disable-dictdotcn \
           --disable-festival \
           --disable-gnome-support \
           --disable-gucharmap \
           --disable-schemas-install \
           --disable-scrollkeeper \
           --disable-tools
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

# Move metadata file to correct dir
mkdir -p %{buildroot}%{_datadir}/metainfo
mv %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml \
   %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

# save space, create symlinks for identical files
%fdupes -s %{buildroot}

%files -f %{name}.lang
%license COPYING
%doc dict/doc/FAQ dict/doc/HACKING dict/doc/HowToCreateDictionary dict/doc/StarDictFileFormat dict/doc/Translation dict/AUTHORS dict/ChangeLog dict/README
%{_libdir}/stardict
%{_bindir}/*
%{_mandir}/man1/stardict-editor.1%{?ext_man}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/stardict/
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/stardict.1%{?ext_man}

%changelog
