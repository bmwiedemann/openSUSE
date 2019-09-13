#
# spec file for package stardict
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


%if 0%{?suse_version} >= 1500
%define espeakdev espeak-ng-compat-devel
%else
%define espeakdev espeak-devel
%endif

Name:           stardict
Version:        3.0.5
Release:        0
Summary:        A cross-platform and internationalized dictionary
License:        GPL-3.0-only
Group:          Productivity/Office/Dictionary
Url:            http://stardict-4.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE stardict-3.0.3-fix-path-for-sounds.patch -- adjust default path for sound files
Patch0:         stardict-3.0.3-fix-path-for-sounds.patch
# PATCH-FIX-OPENSUSE stardict-3.0.3-improve-desktop-file.patch -- add GenericName entry
Patch1:         stardict-3.0.3-improve-desktop-file.patch
# PATCH-FIX-OPENSUSE stardict-3.0.5-enable-gtk3.patch -- use gtk3 code
Patch2:         stardict-3.0.5-enable-gtk3.patch
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  %{espeakdev}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  gtk3-devel >= 3.0
BuildRequires:  intltool
BuildRequires:  libsigc++2-devel
BuildRequires:  libtool
BuildRequires:  perl-XML-Parser
BuildRequires:  sgml-skel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(libxml-2.0)
# gucharmap now uses gtk3, but stardict still uses gtk2
# BuildRequires:  gucharmap-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
StarDict is a Cross-Platform and international dictionary written in
Gtk3.

It has powerful features such as "Glob-style pattern matching", "Scan
selection word","Fuzzy query" etc.


%lang_package
%prep
%setup -q
%patch0
%patch1
%patch2

# Remove unneeded sigc++ header files to make it sure
# that we are using system-wide libsigc++
find src/sigc++* -name \*.h -or -name \*.cc | xargs rm -f

%build
%configure \
           --disable-dictdotcn \
           --disable-festival \
           --disable-gnome-support \
           --disable-gucharmap \
           --disable-schemas-install \
           --disable-scrollkeeper \
           --disable-tools
make %{?_smp_mflags}

%install
%make_install

#fix spurious-executable-perm RPMLINT warning
chmod 0644 COPYING

find %{buildroot}%{_libdir}/stardict/plugins -name "*.la" -print0 | xargs -0 rm -rf {} \;

%find_lang %{name}

%suse_update_desktop_file stardict Office Dictionary
# save space, create symlinks for identical files
%fdupes -s %{buildroot}

%clean
rm -rf %{buildroot}

%files  -f %{name}.lang
%defattr(-,root,root)
%doc dict/doc/FAQ dict/doc/HACKING dict/doc/HowToCreateDictionary dict/doc/StarDictFileFormat dict/doc/Translation dict/AUTHORS COPYING dict/ChangeLog dict/README
%{_libdir}/stardict
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/omf
%{_datadir}/pixmaps/*.png
%{_datadir}/stardict
%{_mandir}/man1/stardict.1.gz

%changelog
