#
# spec file for package sgpio
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


Name:           sgpio
Version:        1.2.1
Release:        0
Summary:        SGPIO captive backplane tool
License:        GPL-2.0+
Group:          System/Base
Url:            http://sources.redhat.com/lvm2/wiki/DMRAID_Eventing
Source0:        %{name}-%{version}.tar.bz2
Patch0:         sgpio-cflags.diff
Patch1:         sgpio_0.10.patch
Patch2:         sgpio-make.patch
BuildRequires:  dos2unix
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Serial General Purpose Input Output (SGPIO) is a communication method used
between a main board and a variety of internal and external hard disk drive
bay enclosures. This utility can be used to control LEDs in an enclosure.
For more information about SGPIO, please consult the  SFF-8485
Specification.

%prep
%setup -q -n %{name}
%patch0
%patch1
%patch2

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"
dos2unix README LICENSE_GPL
chmod a-x README LICENSE_GPL

%install
install -D -m 0755 sgpio   %{buildroot}/%{_bindir}/sgpio
install -D -m 0644 sgpio.1 %{buildroot}/%{_mandir}/man1/sgpio.1

%files
%defattr(-,root,root)
%doc README LICENSE_GPL
%{_bindir}/sgpio
%{_mandir}/man1/sgpio.1%{ext_man}

%changelog
