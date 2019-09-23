#
# spec file for package gnustep-make
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



%define         gs_config        %{_sysconfdir}/GNUstep/GNUstep.conf
%define         gs_layout        fhs-other
%define         gs_makefiles     %{_datadir}/GNUstep/Makefiles
# Disable LTO for all GNUstep packages
%define         _lto_cflags      %{nil}

Name:           gnustep-make
Summary:        GNUstep Makefile package
Version:        2.7.0
Release:        0
License:        LGPL-2.1+ and GPL-3.0+
Group:          System/GUI/Other
Url:            http://www.gnustep.org/
Source:         ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz.sig
Source2:        %{name}-rpmlintrc
BuildRequires:  gcc-objc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# Disable debug package as rpm > 4.13 does not allow for empty debug file list.
%global debug_package %{nil}

%description
This package contains the basic scripts, makefiles and directory
layout needed to run and compile any GNUstep software. This package
was configured for the FHS file system layout, customised for SUSE.

%prep
%setup -q
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
%defattr (-, root, root)
%doc ANNOUNCE ChangeLog COPYING FAQ GNUstep-HOWTO NEWS README RELEASENOTES
%dir %{_sysconfdir}/GNUstep
%dir %{_datadir}/GNUstep
%{_bindir}/debugapp
%{_bindir}/gnustep-config
%{_bindir}/gnustep-tests
%{_bindir}/openapp
%{_bindir}/opentool
%{_mandir}/man1/debugapp.1.gz
%{_mandir}/man1/gnustep-config.1.gz
%{_mandir}/man1/gnustep-tests.1.gz
%{_mandir}/man1/openapp.1.gz
%{_mandir}/man1/opentool.1.gz
%{_mandir}/man7/GNUstep.7.gz
%{_mandir}/man7/library-combo.7.gz
%config(noreplace) %{gs_config}
%{gs_makefiles}
%defattr(0755,root,root)
%{gs_makefiles}/*.template
%{gs_makefiles}/*.*sh

%changelog
