#
# spec file for package notify-sharp
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# This package installs in /usr/lib and .pc file goes to /usr/share/pkgconfig
# Define _libexecdir for <= 1110
%if 0%{?suse_version} <= 1110
%define _libexecdir %{_prefix}/lib
%endif

Name:           notify-sharp3
%define _name   notify-sharp
Url:            https://www.meebey.net/projects/notify-sharp/
Version:        3.0.3
Release:        0
License:        MIT
Group:          Development/Libraries/Other
Summary:        A C# client implementation for Desktop Notifications
Source:         https://www.meebey.net/projects/notify-sharp/downloads/%{_name}-%{version}.tar.gz
Patch:          notify-sharp-use_dbussharp_2.pc.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
%if 0%{?suse_version} >= 1130
BuildRequires:  pkgconfig(dbus-sharp-2.0)
BuildRequires:  pkgconfig(dbus-sharp-glib-2.0)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(monodoc)
%else
BuildRequires:  dbus-sharp-devel
BuildRequires:  dbus-sharp-glib-devel
BuildRequires:  gtk-sharp3
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
%setup -q -n %{_name}-%{version}
%patch -p1

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
mkdir -p %{buildroot}%{_datadir}/pkgconfig/
mv %{buildroot}%{_prefix}/lib/pkgconfig/notify-sharp-3.0.pc %{buildroot}%{_datadir}/pkgconfig/notify-sharp-3.0.pc

%files
%defattr(-,root,root)
%{_prefix}/lib/mono/gac/%{_name}/
%{_prefix}/lib/mono/%{_name}-3.0/

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/%{_name}-3.0.pc

%changelog
