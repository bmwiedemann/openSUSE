#
# spec file for package utsushi
#
# Copyright (c) 2021 SUSE LLC
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


Name:           utsushi
Version:        1610777387.ab70633
Release:        0
Summary:        Next Generation Image Acquisition Utilities
License:        GPL-3.0-or-later
URL:            https://gitlab.com/utsushi/utsushi
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Patch0:         0001-drivers-avoid-library-version-for-dynamically-loadab.patch
Patch1:         0002-avoid-version-for-dynamic-libs.patch
Patch2:         0003-fix-uint-deprecation.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libxslt-tools
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  sane-backends
BuildRequires:  tesseract-ocr
BuildRequires:  tesseract-ocr-traineddata-orientation_and_script_detection
BuildRequires:  pkgconfig(Magick++)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sane-backends)
Provides:       imagescan

%description
This software provides applications to easily turn hard-copy documents and
imagery into formats that are more amenable to computer processing.

Included are a native driver for a number of EPSON scanners and a compatibility
driver to interface with software built around the SANE standard.

This is the community maintained fork, based on imagescan upstream.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1
%patch2
./bootstrap

%build
%configure \
    --with-jpeg \
    --with-tiff \
    --with-gtkmm \
    --with-sane \
    --with-magick \
    --with-magick-pp \
    --enable-sane-config \
    --enable-udev-config \
    --disable-static
%make_build

%check
#make check

%install
%make_install
install -m644 lib/devices.conf %{buildroot}/%{_sysconfdir}/%{name}/%{name}.conf
mkdir -p %{buildroot}/%{_udevrulesdir}
install -m644 drivers/esci/utsushi-esci.rules %{buildroot}/%{_udevrulesdir}/56-utsushi-esci.rules
# Fix issue with "undefined symbol: libcnx_usb_LTX_factory" (https://bugs.archlinux.org/task/63491)
patchelf --add-needed libcnx-usb.so %{buildroot}/%{_libdir}/%{name}/sane/libsane-utsushi.so
# Headers are not needed outside this package
rm -r %{buildroot}/%{_includedir}
# Do not install libtool files
find %{buildroot} -type f -name "*.la" -delete -print
# Remove unwanted link to libtool file
rm %{buildroot}/%{_libdir}/sane/libsane-utsushi.la
%find_lang %{name}

%files
%license COPYING
%doc ChangeLog NEWS README
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_libdir}/%{name}
%{_libdir}/sane/libsane-%{name}.*
%{_datadir}/%{name}
%{_udevrulesdir}/56-utsushi-esci.rules
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*.conf
%config %{_sysconfdir}/sane.d/dll.d/%{name}

%files -n %{name}-lang -f %{name}.lang

%changelog
