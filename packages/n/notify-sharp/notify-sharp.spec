#
# spec file for package notify-sharp (Version 0.4.0)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           notify-sharp
Url:            http://trac.galago-project.org/wiki/DesktopNotifications
Version:        0.4.0.r3032
%define _version 0.4.0
Release:        0
License:        MIT
Group:          Development/Libraries/Other
Summary:        A C# client implementation for Desktop Notifications
Source:         %{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM notify-sharp-use-dbus-sharp nmarques@opensuse.org -- replaces the usage of deprecated NDesk.DBus by dbus-sharp, see https://github.com/hyperair/notify-sharp
Patch0:         %{name}-use-dbus-sharp.patch
# PATCH-FIX-UPSTREAM notify-sharp-fix-app-name-derivation.patch vuntz@opensuse.org -- Fix finding the app name, taken from Debian
Patch1:         notify-sharp-fix-app-name-derivation.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?suse_version} >= 1130
BuildRequires:  pkgconfig(dbus-sharp-1.0)
BuildRequires:  pkgconfig(dbus-sharp-glib-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(monodoc)
%else
BuildRequires:  dbus-sharp-devel
BuildRequires:  dbus-sharp-glib-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk-sharp2
BuildRequires:  mono-devel
BuildRequires:  monodoc
%endif
Recommends:     notification-daemon

%description
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%package devel
Summary:        A C# client implementation for Desktop Notifications
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
notify-sharp is a C# client implementation for Desktop Notifications,
i.e. notification-daemon. It is inspired by the libnotify API.

Desktop Notifications provide a standard way of doing passive pop-up
notifications on the Linux desktop. These are designed to notify the
user of something without interrupting their work with a dialog box
that they must close. Passive popups can automatically disappear after
a short period of time.

%prep
%setup -q -n %{name}-%{_version}
%patch0 -p1
%patch1 -p1

%build
NOCONFIGURE=1 autoreconf -fi
%configure \
   --libdir=%{_prefix}/lib \
   --disable-docs
make %{?jobs:-j%jobs}

%install
# For backward compatability with <= 1110
%makeinstall
# Move .pc file to /usr/share/pkgconfig (for no arch) and remove from libdir
install -Dm 0644 %{name}.pc %{buildroot}%{_datadir}/pkgconfig/%{name}.pc
find %{buildroot}%{_prefix}/lib -name %{name}.pc -type f -print -delete

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/mono/gac/%{name}
%{_prefix}/lib/mono/gac/%{name}/
%dir %{_prefix}/lib/mono/%{name}
%{_prefix}/lib/mono/%{name}/
#/usr/lib/monodoc/sources/*

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/%{name}.pc

%changelog
