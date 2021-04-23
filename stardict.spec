#
# spec file for package stardict
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


%if 0%{?suse_version} >= 1500
%define espeakdev espeak-ng-compat-devel
%else
%define espeakdev espeak-devel
%endif
Name:           stardict
Version:        3.0.6
Release:        0
Summary:        A powerful cross-platform dictionary written in GTK+3
License:        GPL-3.0-only
Group:          Productivity/Office/Dictionary
URL:            http://stardict-4.sourceforge.net/
Source0:        http://sourceforge.net/projects/stardict-4/files/%{version}/%{name}-%{version}.tar.bz2/download#/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE stardict-3.0.3-fix-path-for-sounds.patch -- adjust default path for sound files
Patch0:         stardict-3.0.3-fix-path-for-sounds.patch
# PATCH-FIX-OPENSUSE stardict-3.0.3-improve-desktop-file.patch -- add GenericName entry
Patch1:         stardict-3.0.3-improve-desktop-file.patch
# PATCH-FIX-OPENSUSE stardict-3.0.5-enable-gtk3.patch -- use gtk3 code
Patch2:         stardict-3.0.5-enable-gtk3.patch
BuildRequires:  %{espeakdev}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  gtk3-devel >= 3.0
BuildRequires:  intltool
BuildRequires:  libsigc++2-devel
BuildRequires:  libtool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
# gucharmap now uses gtk3, but stardict still uses gtk2
# BuildRequires:  gucharmap-devel

%description
StarDict is a cross-platform and international dictionary written in GTK+3.

It has features such as "Glob-style pattern matching", "Scan
selection word" and "Fuzzy query".

%lang_package

%prep
%setup -q
%patch0
%patch1
%patch2

# Remove unneeded sigc++ header files to make it sure
# that we are using system-wide libsigc++
find dict/src/sigc++* -name "*.h" -or -name "*.cc" -delete

%build
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

#fix spurious-executable-perm RPMLINT warning
chmod 0644 COPYING

find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %{name}

%suse_update_desktop_file stardict Office Dictionary
# save space, create symlinks for identical files
%fdupes -s %{buildroot}

%files -f %{name}.lang
%license COPYING
%doc dict/doc/FAQ dict/doc/HACKING dict/doc/HowToCreateDictionary dict/doc/StarDictFileFormat dict/doc/Translation dict/AUTHORS dict/ChangeLog dict/README
%{_libdir}/stardict
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/omf
%{_datadir}/pixmaps/*.png
%{_datadir}/stardict
%{_mandir}/man1/stardict.1%{?ext_man}

%changelog
