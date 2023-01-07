#
# spec file for package gnustep-make
#
# Copyright (c) 2022 SUSE LLC
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


%define         gs_config        %{_sysconfdir}/GNUstep/GNUstep.conf
%define         gs_layout        fhs-other
%define         gs_makefiles     %{_datadir}/GNUstep/Makefiles
# Disable LTO for all GNUstep packages
%define         _lto_cflags      %{nil}
# Disable debug package as rpm > 4.13 does not allow for empty debug file list.
%global debug_package %{nil}
Name:           gnustep-make
Version:        2.9.1
Release:        0
Summary:        GNUstep Makefile package
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            http://www.gnustep.org/
Source:         ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz.sig
Source2:        %{name}-rpmlintrc
Source3:        gnustep-make.keyring
BuildRequires:  gcc-objc

%description
This package contains the basic scripts, makefiles and directory
layout needed to run and compile any GNUstep software. This package
was configured for the FHS file system layout, customised for SUSE.

%prep
%autosetup
# Set correct library path.
sed -e 's|/lib/|/%{_lib}/|' -e 's|/lib$|/%{_lib}|' \
        FilesystemLayouts/fhs-system > FilesystemLayouts/%{gs_layout}

%build
# '--with-tar=tar' ensures we get the real tar rather than gnutar.
# If star is installed, it sets up a duff gnutar.
%configure --with-layout=%{gs_layout} \
%if 0%{?suse_version} >= 1120
  --enable-native-objc-exceptions \
%endif
  --with-tar=tar
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} \
  GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
  install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc ANNOUNCE ChangeLog FAQ GNUstep-HOWTO NEWS README RELEASENOTES
%dir %{_sysconfdir}/GNUstep
%dir %{_datadir}/GNUstep
%{_bindir}/debugapp
%{_bindir}/gnustep-config
%{_bindir}/gnustep-tests
%{_bindir}/openapp
%{_bindir}/opentool
%{_mandir}/man1/debugapp.1%{?ext_man}
%{_mandir}/man1/gnustep-config.1%{?ext_man}
%{_mandir}/man1/gnustep-tests.1%{?ext_man}
%{_mandir}/man1/openapp.1%{?ext_man}
%{_mandir}/man1/opentool.1%{?ext_man}
%{_mandir}/man7/GNUstep.7%{?ext_man}
%{_mandir}/man7/library-combo.7%{?ext_man}
%config(noreplace) %{gs_config}
%{gs_makefiles}
%{gs_makefiles}/*.template
%{gs_makefiles}/*.*sh

%changelog
