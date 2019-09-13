#
# spec file for package mate-applet-dock
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   mate-dock-applet
Name:           mate-applet-dock
Version:        0.88
Release:        0
Summary:        Dock applet for the MATE panel
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/robint99/mate-dock-applet
Source:         https://github.com/robint99/%{_name}/archive/V%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bamf-daemon
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  python3-devel
Requires:       bamf-daemon
Requires:       python3-Pillow
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-xdg
Recommends:     libunity
%glib2_gsettings_schema_requires
%if 0%{?suse_version} >= 1500
Requires:       python3-python-xlib
%else
Requires:       python3-xlib
%endif

%description
An application dock applet for the MATE panel.

The applet allows you to:
 * Place a dock on any MATE panel, of any size, on any side of the
   desktop you desire.
 * Pin and unpin applications to the dock.
 * Rearrange application icons on the dock.
 * Launch applications by clicking on their icons in the dock.
 * Minimise/restore the running application windows by clicking the
   applications dock icon.
 * Detect changes in the current icon theme and update the dock
   accordingly.
 * Use an indicator by each application to show when it is running.
 * Optionally, use multiple indicators for each window an
   application has opened.
 * Use either a light or dark indicator that it can always be seen
   no matter what colour the panel is.

%prep
%setup -q -n %{_name}-%{version}

%build
autoreconf -fi
%configure \
  --with-gtk3
make %{?_smp_mflags} V=1

%install
%make_install
%fdupes %{buildroot}%{_libdir}/

pushd %{buildroot}%{_libdir}/mate-applets/mate-dock-applet/
# Do not use env for python scripts.
sed -i '/^#!/s|env python3$|python3|' *.py
# Create Python bytecode.
rm -rf *.pyc *.pyo __pycache__/
touch -c *.py
%py3_compile .
popd

%if 0%{?suse_version} < 1500
%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%dir %{_libdir}/mate-applets/
%{_libdir}/mate-applets/mate-dock-applet/
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/services/org.mate.panel.applet.*.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.panel.*.mate-panel-applet

%changelog
