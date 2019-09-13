#
# spec file for package gtk2-engine-aurora (Version 1.5.1)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           gtk2-engine-aurora
Version:        1.5.1
Release:        1
Summary:        Another GTK2 engine theme
Group:          System/GUI/LXDE
License:        GPL-2.0
Url:            http://gnome-look.org/content/show.php/Aurora+GTK+Engine?content=56438
BuildRequires:  gcc gtk2-devel make pkg-config
Source0:        aurora-%version.tar.bz2
Patch0:         %name-no-return-in-non-void.patch
Patch1:         %name-arrow_size.patch
# PATCH-FIX-UPSTREAM gtk2-engine-aurora-fix-glib-includes.patch gber@opensuse.org -- Do not include glib/gtimer.h directly
Patch2:         gtk2-engine-aurora-fix-glib-includes.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Aurora Gtk Engine themes all common Gtk widgets
to provide an attractive, complete and consistent
look for Gtk applications.

%prep
%setup -q -n aurora-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure --enable-animation
make %{?jobs:-j%jobs}

%install
%makeinstall
mkdir -p %buildroot/%_datadir/themes
cp -R Aurora %buildroot/%_datadir/themes/
rm %buildroot/%_libdir/gtk-2.0/2.10.0/engines/libaurora.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING
%_datadir/themes/Aurora
%_libdir/gtk-2.0/2.10.0/engines/libaurora.so

%changelog
