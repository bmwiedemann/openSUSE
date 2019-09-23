#
# spec file for package sc-controller
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           sc-controller
Version:        0.4.7
Release:        0
Summary:        User-mode driver and GTK3-based GUI for the Steam Controller
License:        GPL-2.0-only
Group:          Hardware/Joystick
URL:            https://github.com/kozec/sc-controller
Source:         https://github.com/kozec/sc-controller/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(udev)
#Requires:       libgtk-3-0
Requires:       python-evdev
Requires:       python-gobject-Gdk
Requires:       python-pylibacl
Requires:       python-setuptools

%description
Application allowing to setup, configure and use the Steam Controller
without using the Steam client.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --optimize=1

%fdupes %{buildroot}%{_prefix}

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md ADDITIONAL-LICENSES TODO.md
%{_bindir}/*
%{python_sitearch}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/scc/
%{_datadir}/mime/packages/*
%{_datadir}/icons/hicolor/*
%{_udevrulesdir}/69-sc-controller.rules

%dir %_libdir/python2.7/site-packages/scc/
%dir %{_datadir}/scc/*

%changelog
