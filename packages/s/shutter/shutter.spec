#
# spec file for package shutter
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 8/2011 - now by open-slx GmbH <Sascha.Manns@open-slx.de>
# Copyright (c) 12/2010 - 7/2011 by Sascha Manns <saigkill@opensuse.org>  
# Copyright (c) 7/2010 - 12/2010 by Ray Chen <swyear@gmail.com>
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


Name:           shutter
Version:        0.94
Release:        0
Summary:        Featureful screenshot tool
License:        GPL-3.0+
Group:          Productivity/Graphics/Other
Url:            http://shutter-project.org/
Source0:        https://launchpad.net/shutter/0.9x/0.94/+download/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Remove Unity only actions
Patch0:         desktop-shortcut-fix.diff
# PATCH-FIX-OPENSUSE make Dropbox support optional
Patch2:         remove-provide-dropbox.diff
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
Requires:       %{name}-lang = %{version}
Requires:       ImageMagick
Requires:       hicolor-icon-theme
Requires:       procps
Requires:       xdg-utils
Requires:       perl(File::BaseDir)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(File::Which)
Requires:       perl(Glib)
Requires:       perl(Gnome2)
Requires:       perl(Gnome2::Canvas)
Requires:       perl(Gnome2::VFS)
Requires:       perl(Gnome2::Wnck)
Requires:       perl(Gtk2)
Requires:       perl(Gtk2::AppIndicator)
Requires:       perl(Gtk2::ImageView)
Requires:       perl(Gtk2::Unique)
Requires:       perl(Image::Magick)
Requires:       perl(JSON)
Requires:       perl(JSON::XS)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Locale::gettext)
Requires:       perl(Net::DBus)
Requires:       perl(Path::Class)
Requires:       perl(Proc::ProcessTable)
Requires:       perl(Proc::Simple)
Requires:       perl(Sort::Naturally)
Requires:       perl(WWW::Mechanize)
Requires:       perl(X11::Protocol)
Requires:       perl(XML::Simple)
Recommends:     gnome-web-photo
Recommends:     nautilus-sendto
Recommends:     perl(Goo::Canvas)
Recommends:     perl(Image::ExifTool)
# For UbuntuOne support
Recommends:     perl(Net::DBus-GLib)
# For Dropbox support
Recommends:     perl(Net::Dropbox-API)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%lang_package

%description
Shutter is a GTK+ 2.0 screenshot application written in perl.
Shutter covers all features of common command line tools like
scrot or import and adds reasonable new features combined
with a comfortable GUI using the GTK+ 2.0 framework

%prep
%setup -q
%patch0
%patch2

%build

%install
# Creating the Folder for Binary and Data. Copy the Bin into Bindir
install -d -m 0755 -p %{buildroot}%{_bindir}
install -m 755 bin/%{name} %{buildroot}%{_bindir}

# Create Datadir Folder
install -d -m 755 %{buildroot}%{_datadir}/
cp -pfr share/* %{buildroot}%{_datadir}/

%suse_update_desktop_file -r %{name} Utility DesktopUtility

%find_lang %{name} --all-name

rm -f %{buildroot}%{_datadir}/applications/%{name}.desktop~
rm -f %{buildroot}%{_datadir}/applications/%{name}.desktop.orig

%fdupes %{buildroot}%{_datadir}/

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}/*
%{_mandir}/man1/%{name}.1%{ext_man}
%dir %{_datadir}/appdata/
%{_datadir}/appdata/shutter.appdata.xml

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
