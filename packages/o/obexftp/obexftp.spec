#
# spec file for package obexftp
#
# Copyright (c) 2020 SUSE LLC
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


Name:           obexftp
BuildRequires:  asciidoc
BuildRequires:  bluez-devel
BuildRequires:  cmake
# support for building obexfs from this source is disabled for now. reenable ASAP
#BuildRequires:  fuse-devel
BuildRequires:  libtool
BuildRequires:  openobex-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  ruby-devel
BuildRequires:  swig
BuildRequires:  xmlto
Version:        0.24
Release:        0
Summary:        ObexFTP Implements the Object Exchange (OBEX) Protocol's File Transfer Feature
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://triq.net/obexftp
Source:         %name-%version.tar.bz2
Patch1:         obexftp-0.24-fix-absurd-install-path.patch
Patch2:         obexftp-0.24-move_to_python3.patch
Patch3:         obexftp-pkgconfig_requires.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ObexFTP works with all protocols supported by openobex (OpenOBEX).
Currently, these are:

- irda (IrDA),
- bluez-utils (BlueTooth)
- setserial (Serial)

%package devel
Summary:        Development package for obexftp
Group:          Development/Libraries/C and C++
Requires:       %name = %version
Requires:       openobex-devel

%description devel
Files needed for software development using obexftp.

%prep
%setup -q -n %{name}-%{version}-Source
%patch1 -p1
%patch2
%patch3

chmod -x AUTHORS Doxyfile ChangeLog NEWS README THANKS TODO examples/README_obexftpbackup

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} ..
make %{?_smp_mflags} all doc # because "all" apparently does not mean "all"

%install
cd build
make "DESTDIR=$RPM_BUILD_ROOT" install

%perl_process_packlist
rm -f %{buildroot}%{_libdir}/lib*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_mandir}/*/*

%files devel
%defattr(-,root,root)
%_libdir/lib*.so
%_includedir/bfb
%_includedir/obexftp
%_includedir/multicobex
%_libdir/pkgconfig/obexftp.pc

%package -n python3-obexftp
Summary:        ObexFTP Implements the Object Exchange (OBEX) - Python3 bindings
Group:          Productivity/Networking/Other
Requires:       %name = %version

%description -n python3-obexftp
ObexFTP works out-of-the-box with all protocols supported by OpenOBEX.
Currently IrDA, BlueTooth, and Serial.

This package contains the python3 bindings.

%files -n python3-obexftp
%defattr(-,root,root)
%{python3_sitearch}/*

%package -n perl-obexftp
Summary:        ObexFTP Implements the Object Exchange (OBEX) - Perl bindings
Group:          Productivity/Networking/Other
Requires:       %name = %version
Requires:       perl-base = %{perl_version}

%description -n perl-obexftp
ObexFTP works out-of-the-box with all protocols supported by OpenOBEX.
Currently IrDA, BlueTooth, and Serial.

This package contains the Perl bindings.

%files -n perl-obexftp
%defattr(-,root,root)
%if %suse_version < 1140
/var/adm/perl-modules/obexftp
%endif
%{perl_vendorarch}/OBEXFTP.pm
%{perl_vendorarch}/auto/OBEXFTP

%package -n ruby-obexftp
Summary:        ObexFTP Implements the Object Exchange (OBEX) - Ruby bindings
Group:          Productivity/Networking/Other
Requires:       %name = %version
Requires:       ruby(abi) = %{rb_ver}

%description -n ruby-obexftp
ObexFTP works out-of-the-box with all protocols supported by OpenOBEX.
Currently IrDA, BlueTooth, and Serial.

This package contains the Ruby bindings.

%files -n ruby-obexftp
%defattr(-,root,root)
%{_libdir}/ruby/vendor_ruby/%{rb_ver}/%{rb_arch}/obexftp.so

%changelog
