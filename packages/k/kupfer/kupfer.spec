#
# spec file for package kupfer
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        329
Release:        0
Summary:        An interface for access to applications and documents
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://kupferlauncher.github.io/
Source:         https://github.com/kupferlauncher/%{name}/releases/download/v%{version}/kupfer-v%{version}.tar.xz
BuildRequires:  dbus-1-python3
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection
BuildRequires:  intltool
BuildRequires:  python3 >= 3.9
BuildRequires:  python3-docutils
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-pyxdg
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
Requires:       desktop-file-utils
Requires:       gvfs
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-docutils
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-pyxdg
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
BuildArch:      noarch

%description
Kupfer is an interface for access to applications
and their documents.

The most typical use is to find a specific application and launch it.
Kupfer can be extended with plugins so that its quick-access
paradigm can be extended to many more objects than just
applications.

%lang_package

%prep
%autosetup -n %{name}-v%{version}

%build
python3 waf configure --prefix=%{_prefix} --libdir=%{_libdir}
python3 waf build %{?_smp_mflags}

%install
python3 waf install --destdir=%{buildroot}

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
