#
# spec file for package libx86emu
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2008 Steffen Winterfeldt
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


Name:           libx86emu
BuildRequires:  xz
Summary:        An x86 emulation library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Version:        2.4
Release:        0
Source:         %{name}-%{version}.tar.xz
Url:            https://github.com/wfeldt/libx86emu
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An x86 emulation library with focus on usage and
execution logging functions.

%package -n     libx86emu2
Summary:        An x86 emulation library
Group:          System/Libraries

%description -n libx86emu2
An x86 emulation library with focus on usage and
execution logging functions.

%package -n     libx86emu-devel
Summary:        Development files for libx86emu
Group:          Development/Libraries/C and C++
Requires:       libx86emu2 = %version

%description -n libx86emu-devel
An x86 emulation library with focus on usage and
execution logging functions.

This package contains the header files for the library API.

%prep
%setup -n libx86emu-%{version}

%build
make LIBDIR=%{_libdir}

%install
install -d -m 755 %{buildroot}%{_libdir}
%make_install LIBDIR=%{_libdir}

%post -n libx86emu2 -p /sbin/ldconfig

%postun -n libx86emu2 -p /sbin/ldconfig

%files -n libx86emu2
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc README.md
%license LICENSE*

%files -n libx86emu-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/x86emu.h

%changelog
