#
# spec file for package flatpak-builder
#
# Copyright (c) 2024 SUSE LLC
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


%define flatpak_version 1.15.6
%bcond_with system_debugedit
%if 0%{?suse_version} >= 1550
%bcond_without system_debugedit
%endif
Name:           flatpak-builder
Version:        1.4.4
Release:        0
Summary:        Tool to build flatpaks from source
License:        LGPL-2.1-or-later
Group:          Development/Tools/Building
URL:            http://flatpak.org/
Source0:        https://github.com/flatpak/flatpak-builder/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         fusermount3.diff
BuildRequires:  AppStream
BuildRequires:  AppStream-compose
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  libcap-devel
BuildRequires:  meson
BuildRequires:  pkgconfig >= 0.24
BuildRequires:  xmlto
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(flatpak) >= %{flatpak_version}
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdw) >= 0.172
BuildRequires:  pkgconfig(libelf) >= 0.8.12
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4
BuildRequires:  pkgconfig(ostree-1) >= 2017.14
BuildRequires:  pkgconfig(yaml-0.1)
Requires:       %{_bindir}/appstreamcli
Requires:       %{_bindir}/bzip2
Requires:       AppStream-compose
Recommends:     %{_bindir}/bzr
Requires:       %{_bindir}/eu-strip
Requires:       %{_bindir}/git
Requires:       %{_bindir}/patch
Requires:       %{_bindir}/strip
Requires:       %{_bindir}/tar
Requires:       %{_bindir}/unzip
Requires:       flatpak >= %{flatpak_version}
# it is enough to have debugedit insatlled for meson to detect it and use the system version
%if %{with system_debugedit}
BuildRequires:  debugedit
Requires:       debugedit
%endif

%description
Tool to build flatpaks from source.
See https://docs.flatpak.org/ for more information.

%prep
%autosetup -p1

%build
# these are the same flags that are normally set minus -Werror=return-type which causes libglnx to not compile
export CFLAGS='-O2 -Wall -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=3 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -flto=auto -g'
%meson \
	-D fuse=3 \
	-D docs=enabled
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/doc/%{name}/
%{_bindir}/flatpak-builder
%{_mandir}/man1/flatpak-builder.1%{ext_man}
%{_mandir}/man5/flatpak-manifest.5%{ext_man}
%if %{without system_debugedit}
%{_libexecdir}/flatpak-builder-debugedit
%endif

%changelog
