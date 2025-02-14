#
# spec file for package xmoontool
#
# Copyright (c) 2025 SUSE LLC
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


Name:           xmoontool
Version:        22.9.94
Release:        0
Summary:        The Moon in focus
License:        SUSE-Public-Domain
Group:          Productivity/Scientific/Astronomy
URL:            http://www.fourmilab.ch/earthview/vplanet.html
Source:         xmoontool-22sep94.tar.gz
Source1:        xmoontool.desktop
Patch0:         xmoontool-22sep94.patch
Patch1:         xmoontool-22sep94-y2kfix.patch
Patch2:         xmoontool-22.9.24-filepermissions.patch
Patch3:         xmoontool-22sep94-xorg7.patch
Patch4:         xmoontool-gcc15.patch
BuildRequires:  openmotif-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)
Provides:       moontool
Obsoletes:      moontool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
One of the most important programs existing :-) Using this program, you
can display all important information about the moon constantly. At
last...

Hint: The option -c makes it also work with color ;-)

%prep
%autosetup -p0 -n xmoontool-22sep94

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -I%{_prefix}/include" XLIBDIR=%{_libdir}

%install
make "DESTDIR=%{buildroot}" install
%suse_update_desktop_file -i %{name} Edutainment Astronomy

%files
%defattr(-,root,root)
%{_bindir}/xmoontool
%{_datadir}/applications/*.desktop
%doc %{_mandir}/man1/xmoontool.1.gz

%changelog
