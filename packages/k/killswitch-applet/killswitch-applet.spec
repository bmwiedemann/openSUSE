#
# spec file for package killswitch-applet
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           killswitch-applet
Version:        0.2.3
Release:        0
Summary:        Manage Killswitches
License:        WTFPL
Group:          Productivity/Other
Source:         killswitch-applet-%{version}.tar.gz
BuildRequires:  dbus-1-python
BuildRequires:  python-devel
BuildRequires:  python-gtk
Requires:       dbus-1-python
Requires:       python-gtk
Requires:       python-killswitch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{py_requires}
%if %{?suse_version: %{suse_version} > 1110} %{!?suse_version:1}
BuildArch:      noarch
%endif

%description
killswitch-applet is a small application sitting in the system tray
providing the possibility to manage all the killswitches found in the
system. In this context, "managing" means enabling or disabling certain
killswitches. This is especially useful if you have multiple killswitches
like bluetooth, WWAN or WLAN.

%prep
%setup -q

%build

%install
./setup.py install --prefix=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/killswitch-applet
%{_datadir}/icons/hicolor/32x32/apps/killswitch-applet.png
%{_datadir}/icons/hicolor/scalable/apps/killswitch-applet.svg
%{_prefix}/lib/python*/site-packages/*.egg-info
%{_datadir}/applications/killswitch-applet.desktop

%changelog
