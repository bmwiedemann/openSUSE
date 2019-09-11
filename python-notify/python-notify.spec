#
# spec file for package python-notify
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


%define pypkgname pynotify
Name:           python-notify
Version:        0.1.1
Release:        0
Summary:        Python bindings for libnotify
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            http://www.galago-project.org/specs/notification
Source:         http://www.galago-project.org/files/releases/source/notify-python/notify-python-%{version}.tar.bz2
Patch0:         notify-python-0.1.1-fix-GTK-symbols.patch
# PATCH-FIX-UPSTREAM libnotify-0.7.patch fcrozat@novell.com -- fix build with libnotify >= 0.7 (from Fedora)
Patch1:         libnotify07.patch
BuildRequires:  fdupes
BuildRequires:  libnotify-devel
BuildRequires:  python-devel
BuildRequires:  python-gtk-devel
%if 0%{?suse_version} <= 1130
BuildRequires:  gtk2-devel
%endif

%description
Python bindings for libnotify.

%package devel
Summary:        Python bindings for libnotify
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description devel
Python bindings for libnotify.

%prep
%setup -q -n "notify-python-%{version}"
%patch0 -p1 -b .fix-GTK-symbols
%patch1 -p1 -b .notify07

%build
%define _lto_cflags %{nil}
%if 0%{?suse_version} <= 1130
export CFLAGS="%{optflags} `pkg-config --cflags --libs gtk+-2.0`"
%endif
%configure
# We touch src/pynotify.override in build because upstream did not rebuild
# pynotify.c from the input definitions. This forces pynotify.c to be
# regenerated. This is needed to have Notification.attach_to_status_icon
touch src/pynotify.override
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}/%{py_sitedir}

%files
%license COPYING
%doc AUTHORS NEWS
%{py_sitedir}/gtk-2.0/%{pypkgname}/

%files devel
# we explicitly list the directories here to be sure we don't include something
# that should live in the main package
%dir %{_datadir}/pygtk
%dir %{_datadir}/pygtk/2.0
%{_datadir}/pygtk/2.0/defs/
%{_libdir}/pkgconfig/notify-python.pc

%changelog
