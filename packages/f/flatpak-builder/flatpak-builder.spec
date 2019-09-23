#
# spec file for package flatpak-builder
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


Name:           flatpak-builder
Version:        1.0.8
Release:        0
Summary:        Tool to build flatpaks from source
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            http://flatpak.org/
Source0:        https://github.com/flatpak/flatpak-builder/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  libcap-devel
BuildRequires:  libdwarf-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(flatpak) >= 0.11.8
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(ostree-1) >= 2018.7
BuildRequires:  pkgconfig(yaml-0.1)
Requires:       %{_bindir}/bzip2
Recommends:     %{_bindir}/bzr
Requires:       %{_bindir}/eu-strip
Requires:       %{_bindir}/git
Requires:       %{_bindir}/patch
Requires:       %{_bindir}/strip
Requires:       %{_bindir}/tar
Requires:       %{_bindir}/unzip

%description
Tool to build flatpaks from source.
See https://wiki.gnome.org/Projects/SandboxedApps for more information.

%prep
%autosetup

%build
%configure \
	--enable-docbook-docs \
	--with-dwarf-header=%{_includedir}/libdwarf \
	%{nil}
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/doc/%{name}/
%{_bindir}/flatpak-builder
%{_mandir}/man1/flatpak-builder.1%{ext_man}
%{_mandir}/man5/flatpak-manifest.5%{ext_man}

%changelog
