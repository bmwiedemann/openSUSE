#
# spec file for package usbprog
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


# RHEL and CentOS have no wxGTK, so we cannot build the GUI here
%if 0%{?rhel_version} || 0%{?centos_version}
%define         build_gui 0
%define         readme_name README.RedHat
%define         group_name uucp
%endif

%if 0%{?fedora_version}
%define         build_gui 1
%define         readme_name README.Fedora
%define         group_name dialout
%endif

%if 0%{?suse_version}
%define         build_gui 1
%define         readme_name README.SUSE

%if 0%{?suse_version} >= 1120
%define         group_name dialout
%else
%define         group_name uucp
%endif

%endif

Name:           usbprog
Version:        0.2.0
Release:        0
Url:            http://www.embedded-projects.net/index.php?page_id=165
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
Source1:        README.distribution
Patch1:         usbprog-wxwidgets-3.0.diff
Summary:        Programmer for the USBprog hardware
License:        GPL-2.0+ and CC-BY-SA-3.0
Group:          Development/Tools/Other

BuildRequires:  gcc-c++
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(udev)
%if %{build_gui}
BuildRequires:  python-wxWidgets-3_0
BuildRequires:  wxWidgets-3_0-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcurl)

%define _udevdir %(pkg-config --variable=udevdir udev)
%define _udevrulesdir %{_udevdir}/rules.d

%description
USBprog is a programmer for the USBprog hardware.

%if %{build_gui}

%package gui
Requires:       %{name} = %{version}
Summary:        GUI program of USBprog
Group:          Development/Tools/Other

%description gui
A wxGTK version of the USBprog programmer.

%endif

%package -n libusbprog0
Requires:       %{name} = %{version}
Summary:        USBprog Library
Group:          Development/Tools/Other

%description -n libusbprog0
Library for USBprog.

%package devel
Requires:       %{name} = %{version}
Summary:        Development files for libusbprog
Group:          Development/Tools/Other

%description devel
Header files for libusbprog.

%prep
%setup -q
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
%makeinstall
%if %{build_gui} == 0
rm -f $RPM_BUILD_ROOT/%{_datadir}/applications/usbprog.desktop
rm -f $RPM_BUILD_ROOT/%{_datadir}/pixmaps/usbprog_icon.xpm
%endif
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.*a
mkdir -p %{buildroot}%{_udevrulesdir}
sed -e 's/@@USBPROG_GROUP@@/'%{group_name}'/g' usbprog.rules.in \
        > %{buildroot}%{_udevrulesdir}/98-usbprog.rules
sed -e 's/@@USBPROG_GROUP@@/'%{group_name}'/g' %{S:1} > %{readme_name}

%post -n libusbprog0 -p /sbin/ldconfig

%postun -n libusbprog0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog NEWS %{readme_name}
%doc %{_datadir}/doc/usbprog/USBprog.pdf
%dir %{_datadir}/doc/usbprog
%{_bindir}/usbprog
%{_mandir}/man1/usbprog.1*
%{_udevrulesdir}/98-usbprog.rules

%files -n libusbprog0
%defattr(-,root,root)
%{_libdir}/*so.*

%if %{build_gui}

%files gui
%defattr(-,root,root)
%{_bindir}/usbprog-gui
%{_datadir}/applications/usbprog.desktop
%{_datadir}/pixmaps/usbprog_icon.xpm
%{_mandir}/man1/usbprog-gui.1*

%endif

%files devel
%defattr(-,root,root)
%{_includedir}/usbprog
%{_libdir}/*so

%changelog
