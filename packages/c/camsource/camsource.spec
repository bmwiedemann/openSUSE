#
# spec file for package camsource
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


Name:           camsource
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libv4l-devel >= 0.8.4
BuildRequires:  pkgconfig(libxml-2.0)
Version:        0.7.1
Release:        0
Summary:        Camsource Grabs Images from a Video4Linux Device
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Graphics
URL:            http://camsource.sourceforge.net
Source:         camsource-%{version}.tar.gz
Source1:        camsource-rpmlintrc
Patch0:         camsource-no_implicit_decls.diff
Patch1:         camsource-v4l-conf-video_window-overwrite.patch
Patch2:         camsource-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Camsource grabs images from a video4linux device (webcam or TV card).
It is modular and has several plug-ins for modifying the image before
displaying it via HTTP or FTP upload.

%package devel
Summary:        Camsource Grabs Images from a Video4Linux Device
Group:          Development/Libraries/C and C++
Requires:       camsource = %{version}
Provides:       camsource:/usr/include/camsource/image.h
BuildArch:      noarch

%description devel
Camsource grabs images from a video4linux device (webcam or TV card).
It is modular and has several plug-ins for modifying the image before
displaying it via HTTP or FTP upload.

%prep
%autosetup -p1
chmod ugo+x configure

%build
export CFLAGS="%{optflags} -Wall"
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}%{_sysconfdir}/camsource.conf.example %{buildroot}%{_sysconfdir}/camsource.conf

%files
%defattr(-,root,root)
%license COPYING
%doc INSTALL ChangeLog camsource.conf.example
%{_bindir}/camsource
%{_libdir}/camsource
%config(noreplace) %{_sysconfdir}/camsource.conf

%files devel
%defattr(-,root,root)
%{_includedir}/camsource

%changelog
