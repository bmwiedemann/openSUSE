#
# spec file for package libexif-gtk
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


Name:           libexif-gtk
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libexif-devel
BuildRequires:  libtool
URL:            http://libexif.sourceforge.net/
Summary:        GTK Widgets for Viewing EXIF Information
License:        GPL-2.0-or-later
Group:          System/Libraries
Version:        0.5.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://github.com/libexif/%{name}/archive/v%{version}.tar.gz
Requires:       libexif-gtk5 = %{version}

%description
This library contains GTK widgets for viewing EXIF information within
JPEG images created by some digital cameras.

%package -n libexif-gtk5
Summary:        GTK Widgets for Viewing EXIF Information
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libexif-gtk5
This library contains GTK widgets for viewing EXIF information within
JPEG images created by some digital cameras.

%package devel
Summary:        GTK Widgets for Viewing EXIF Information
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gtk2-devel
Requires:       libexif-devel

%description devel
This library contains GTK widgets for viewing EXIF information within
JPEG images created by some digital cameras.

%prep
%setup -q

%build
bash ./autogen.sh
%configure --with-pic \
	--disable-static
make %{?jobs:-j%jobs}

%install
%makeinstall
%find_lang %{name}-5
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig -n libexif-gtk5

%postun -p /sbin/ldconfig -n libexif-gtk5

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog

%files -n libexif-gtk5 -f %{name}-5.lang
%license COPYING
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%license COPYING
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libexif-gtk

%changelog
