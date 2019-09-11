#
# spec file for package gnome-keysign
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


Name:           gnome-keysign
Version:        0.9.7.2
Release:        0
Summary:        GNOME OpenGPG key signing helper
License:        GPL-3.0-or-later
Group:          Productivity/Security
Url:            https://github.com/GNOME-Keysign/gnome-keysign
Source:         %{name}-%{version}.tar.xz
Patch0:         gnome-keysign-python3-setup.patch

BuildRequires:  gobject-introspection
BuildRequires:  python3-Babel
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
%ifarch x86_64
Requires:       gstreamer1(element-zbar)()(64bit)
%else
Requires:       gstreamer1(element-zbar)
%endif
Requires:       python3-Twisted
Requires:       python3-avahi
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gpg
Requires:       python3-pybluez
Requires:       python3-qrcode
Requires:       python3-requests
Requires:       python3-setuptools

%description
Its purpose is to ease signing other peoples' keys. It is similar
to caff, PIUS, or monkeysign. In fact, it is influenced a lot by
these tools and either reimplements ideas or reuses code.
Consider either of the aboved mentioned tools when you need a much
more mature codebase.

%prep
%setup -q
%patch0 -p1

%build
python3 setup.py build

%install
python3 setup.py install -O1 --skip-build --root %{buildroot}
%suse_update_desktop_file -r org.gnome.Keysign System Security

%files
%license COPYING
%doc README.rst
%{_bindir}/%{name}
%{_bindir}/gks-qrcode
%{_datadir}/applications/org.gnome.Keysign.desktop
%{_datadir}/metainfo/org.gnome.Keysign.appdata.xml
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Keysign.svg
%{python3_sitelib}/keysign/
%{python3_sitelib}/gnome_keysign-*.egg-info/

%changelog
