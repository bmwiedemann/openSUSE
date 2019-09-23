#
# spec file for package exif
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           exif
BuildRequires:  libexif-devel
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
Url:            http://sourceforge.net/projects/libexif
Summary:        Small Command Line Utility to Show and Change EXIF Information in JPEG Files
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Version:        0.6.21
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://downloads.sourceforge.net/project/libexif/%{name}/%{version}/%{name}-%{version}.tar.bz2

%description
Exif is a small command line utility to show and change EXIF
information hidden in JPEG files. It demonstrate the power of libexif
library.

%prep 
%setup -q

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIE"
export LDFLAGS="-pie"
%configure
make %{?_smp_mflags}

%check
make check

%install
make DESTDIR=${RPM_BUILD_ROOT}/ install
%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
/usr/bin/exif
%doc %{_mandir}/man1/exif.1.gz

%changelog
