#
# spec file for package libexif-gtk
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


Name:           libexif-gtk
BuildRequires:  gtk2-devel
BuildRequires:  libexif-devel
Url:            http://libexif.sourceforge.net/
Summary:        GTK Widgets for Viewing EXIF Information
License:        GPL-2.0+
Group:          System/Libraries
Version:        0.4.0
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://downloads.sourceforge.net/project/libexif/%{name}/%{version}/%{name}-%{version}.tar.bz2
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
%configure --with-pic \
	--disable-static
make %{?jobs:-j%jobs}

%install
%makeinstall
%find_lang %{name}-5
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig -n libexif-gtk5

%postun -p /sbin/ldconfig -n libexif-gtk5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog COPYING

%files -n libexif-gtk5 -f %{name}-5.lang
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/libexif-gtk

%changelog
