#
# spec file for package beaver
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           beaver
Summary:        Beaver is an Early AdVanced EditoR
License:        GPL-2.0
Group:          System/GUI/GNOME
Version:        0.4.1
Release:        0
Url:            http://beaver-editor.sourceforge.net
Source0:        %name-%version.tar.bz2
Patch0:         %{name}-add-mime-types.patch
# PATCH-OPENSUSE - allow for reproducible binaries
Patch1:         reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files

%description
Beaver starts up fast and doesn't use a lot of memory.
Beaver's only dependency is GTK+2, so no need to install
other libraries eating your disk space. These things make
Beaver very suitable for old computers and use in small Linux distributions.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make V=1 %{?_smp_mflags} all doc

%install
%makeinstall
%suse_update_desktop_file -r %name Utility TextEditor
%__mkdir_p %buildroot/%_datadir/doc/beaver
cp -R docs/html %buildroot/%_datadir/doc/beaver
rm %buildroot/%_libdir/beaver/plugins/*.la
# remove sample plugin doing nothing
rm %buildroot/%_libdir/beaver/plugins/sample.so
%fdupes -s %{buildroot}

%clean
%__rm -fr %buildroot

%if 0%{?suse_version} >= 1140

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%_bindir/beaver
%dir %_libdir/beaver
%dir %_libdir/beaver/plugins
%_libdir/beaver/plugins/ascii.so
%_libdir/beaver/plugins/tools.so
%_datadir/applications/beaver.desktop
%dir %_datadir/beaver
%dir %_datadir/beaver/pixmaps
%dir %_datadir/beaver/resource
%_datadir/beaver/pixmaps/*
%_datadir/beaver/resource/*
%dir %_datadir/doc/beaver/
%dir %_datadir/doc/beaver/html
%_datadir/doc/beaver/html/*
%_datadir/icons/hicolor/*x*/apps/*
%_datadir/pixmaps/beaver.png
%_mandir/man1/*.gz
%_includedir/beaver.h

%changelog
