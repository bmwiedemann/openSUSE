#
# spec file for package kupfer
#
# Copyright (c) 2023 SUSE LLC
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


Name:           kupfer
Version:        322
Release:        0
Summary:        An interface for access to applications and documents
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://kupferlauncher.github.io/
Source:         https://github.com/kupferlauncher/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildRequires:  dbus-1-python3
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  python-base
BuildRequires:  python3 >= 3.4
BuildRequires:  python3-docutils
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-libxml2
BuildRequires:  python3-pyxdg
BuildRequires:  typelib-1_0-Gtk-3_0
BuildRequires:  typelib-1_0-Keybinder-3_0
BuildRequires:  typelib-1_0-Wnck-3_0
BuildRequires:  update-desktop-files
BuildRequires:  xml2po
Requires:       desktop-file-utils
Requires:       gvfs
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-docutils
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-libxml2
Requires:       python3-pyxdg
Requires:       typelib-1_0-Gtk-3_0
Requires:       typelib-1_0-Keybinder-3_0
Requires:       typelib-1_0-Wnck-3_0
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(post): update-desktop-files
Requires(postun):hicolor-icon-theme
Requires(postun):shared-mime-info
Requires(postun):update-desktop-files
BuildArch:      noarch

%description
Kupfer is an interface for access to applications
and their documents.

The most typical use is to find a specific application and launch it.
Kupfer can be extended with plugins so that its quick-access
paradigm can be extended to many more objects than just
applications.

%prep
%autosetup -n %{name}-%{version}

%build
./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
./waf build %{?_smp_mflags}

%install
./waf install --destdir=%{buildroot}
%suse_update_desktop_file %{name} GTK X-SuSE-DesktopUtility
%fdupes %{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.rst Documentation/*
%{_bindir}/%{name}
%{_bindir}/%{name}-exec
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-exec.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/%{name}-mimetypes.xml
%{_datadir}/Thunar
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-exec.1%{?ext_man}

%changelog
