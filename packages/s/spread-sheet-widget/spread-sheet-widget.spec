#
# spec file for package spread-sheet-widget
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017,2020 <opensuse.lietuviu.kalba@gmail.com>
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


%define         libname libspread-sheet-widget0
Name:           spread-sheet-widget
Version:        0.6
Release:        0
Summary:        GNU Spread Sheet Widget library for Gtk+
License:        GPL-3.0-or-later
Group:          Development/Libraries/X11
URL:            https://www.gnu.org/software/ssw/
Source0:        https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz
# *sig. can be converted into *.asc by:
# gpg --enarmor spread-sheet-widget-*.tar.gz.sig
Source1:        https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
BuildRequires:  gtk3-devel >= 3.18.0

%description
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2-dimensional tabular data in a manner similar to many
popular spread sheet programs.

The design follows the model-view-controller paradigm and is of complexity O(1)
in both time and space. This means that it is efficient and fast even for very
large data.

Features commonly found in graphical user interfaces such as cut and paste,
drag and drop and row/column labelling are also included.

%package -n %{libname}
Summary:        GNU Spread Sheet Widget library for Gtk+
Group:          System/Libraries

%description -n %{libname}
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2-dimensional tabular data in a manner similar to many
popular spread sheet programs.

The design follows the model-view-controller paradigm and is of complexity O(1)
in both time and space. This means that it is efficient and fast even for very
large data.

Features commonly found in graphical user interfaces such as cut and paste,
drag and drop and row/column labelling are also included.

%package devel
Summary:        Header files for GNU Gtk+ Spread Sheet Widget library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}

%description devel
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget
for viewing and manipulating 2-dimensional tabular data in a manner
similar to many popular spread sheet programs.

This subpackage contains the header files for the library.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} 

%install
%make_install
find %{buildroot}%{_libdir} -name "*.la" -delete
[ -f %{buildroot}/usr/share/info/dir ] && rm %{buildroot}/usr/share/info/dir

%post -n %{libname} 
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun -n %{libname}
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/lib%{name}.so.0*
%{_infodir}/%{name}.info*

%files devel
%{_includedir}/ssw-axis-model.h
%{_includedir}/ssw-sheet-axis.h
%{_includedir}/ssw-sheet.h
%{_includedir}/ssw-virtual-model.h
%{_libdir}/lib%{name}.so
%attr(0644,root,root) %{_libdir}/pkgconfig/%{name}.pc

%changelog
