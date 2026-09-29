#
# spec file for package run0-wrappers
#
# Copyright (c) 2025 SUSE LLC
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

Name:           rdi-installer
Version:        1.0.0+git20260923.8f88a3f
Release:        0
Summary:        Utility to write disk images to hard disk
License:        MIT
URL:            https://github.com/thkukuk/rdi-installer
Source:         rdi-installer-%{version}.tar.xz
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(ncursesw)
Requires:       gpg2
Requires:       keywait
Requires:       pbzip2
Requires:       pigz
Requires:       pv
Requires:       wget
Requires:       xz
Requires:       zstd

%description
This package contains a raw disk image installer and additonal utilities,
which allow an user to write raw disk images comfortable to a hard disk.

%package utilities
Summary:        Additonal utilities for the rdi-installer image
License:        MIT AND GPL-2.0-or-later

%description utilities
Additional utilities which handle kernel commandline options for the installer.

%package -n rdii-helper
Summary:        Utility to get boot and disk information for RDII
License:        GPL-2.0-or-later

%description -n rdii-helper
Small utility to print firmware informations about booting, provides a list of useable disks and adjust the LoaderEntryDefault on firstboot.

%package -n keywait
Summary:        Waits for a key press or a timeout
License:        GPL-2.0-or-later
Conflicts:	ucommon

%description -n keywait
Small utility which either waits that the user presses a key or a timeout occured.

%package image-arch-deps
Summary:        Requires arch specific RPMs for rdii image
License:        MIT
%ifarch %ix86 x86_64
Requires:       ucode-amd
Requires:       ucode-intel
%endif

%description image-arch-deps
This RPM requires architecture specific packages for building
the rdi-installer image in OBS.


%prep
%autosetup -n rdi-installer-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE.GPL2
%license LICENSE.MIT
%{_bindir}/rdi-installer
%{_mandir}/man7/rdii-config.7%{?ext_man}

%files utilities
%license LICENSE.GPL2
%license LICENSE.MIT
%{_bindir}/rdii-networkd
%{_bindir}/rdii-fetch-config
%{_bindir}/rdii-proxy-setup
%{_bindir}/rdii-ssh-setup
%{_prefix}/lib/systemd/system/rdii-fetch-config-early.service
%{_prefix}/lib/systemd/system/rdii-fetch-config.service
%{_prefix}/lib/systemd/system/rdii-mount-img-part.service
%{_prefix}/lib/systemd/system/rdii-networkd.service
%{_prefix}/lib/systemd/system/rdii-proxy-setup.service
%{_prefix}/lib/systemd/system/rdii-ssh-setup.service
%dir %{_libexecdir}/rdi-installer
%{_libexecdir}/rdi-installer/mount-part-by-label
%{_mandir}/man8/rdii-networkd.8%{?ext_man}
%{_mandir}/man8/rdii-ssh-setup.service.8%{?ext_man}

%files -n rdii-helper
%license LICENSE.GPL2
%{_bindir}/rdii-helper
%{_prefix}/lib/systemd/system/rdii-set-default-loader-entry.service

%files -n keywait
%license LICENSE.GPL2
%{_bindir}/keywait
%{_mandir}/man1/keywait.1%{?ext_man}

%files image-arch-deps
%license LICENSE.MIT

%changelog
