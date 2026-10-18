#
# spec file for package fuseiso
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


Name:           fuseiso
Version:        20260614
Release:        0
Summary:        FUSE module to mount CD-ROM images with ISO9660 filesystems in them
License:        GPL-2.0-or-later
URL:            https://sr.ht/~whynothugo/fuseiso/
Source0:        https://git.sr.ht/~whynothugo/fuseiso/archive/v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3) >= 3.14
BuildRequires:  pkgconfig(glib-2.0) >= 2.2
BuildRequires:  pkgconfig(zlib)
Requires:       fuse3

%description
Fuseiso is a FUSE filesystem module which allows to mount many ISO9660
filesystem images (for CD-ROMs) as a non-root user using fuse.

It supports plain ISO9660 Level 1 and 2, with Rock Ridge, Joliet and
zisofs extensions and also supports the CD-ROM image types img, bin,
mdf and nrg.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install
# docs are also shipped via %%doc from the sources
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}

%changelog
