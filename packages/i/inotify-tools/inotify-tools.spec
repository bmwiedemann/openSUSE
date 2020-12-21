#
# spec file for package inotify-tools
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


Name:           inotify-tools
Version:        3.20.11.0
Release:        0
Summary:        Tools for inotify
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/inotify-tools/inotify-tools
Source:         https://github.com/inotify-tools/inotify-tools/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  libtool

%description
inotify is a kernel facility to watch file system changes. This
package provides some tools for it.

%package -n libinotifytools0
Summary:        Library files for inotify-tools
Group:          System/Monitoring

%description -n libinotifytools0
inotify is a kernel facility to watch file system changes. This
package provides some tools for it.

%package devel
Summary:        Development files for inotify-tools
Group:          Development/Tools/Other
Requires:       libinotifytools0 = %{version}

%description devel
This package contains the development files for inotify-tools, which provides
utilities for the kernel facility inotify.

%package doc
Summary:        Documentation for inotify-tools
Group:          Documentation/Other
Requires:       %{name} = %{version}
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description doc
This package contains the documentation for inotify-tools, which provides
utilities for the kernel facility inotify.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static \
    --docdir=%{_docdir}/%{name} \
    --enable-doxygen
%make_build

%install
%make_install
%fdupes %{buildroot}/%{_docdir}
rm %{buildroot}/%{_libdir}/libinotifytools.la

%post -n libinotifytools0 -p /sbin/ldconfig
%postun -n libinotifytools0 -p /sbin/ldconfig

%check
%make_build check

%files
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_mandir}/man1/inotifywait.1%{?ext_man}
%{_mandir}/man1/inotifywatch.1%{?ext_man}

%files -n libinotifytools0
%license COPYING
%{_libdir}/libinotifytools.so.*

%files devel
%{_libdir}/libinotifytools.so
%{_includedir}/inotifytools/

%files doc
%doc %{_docdir}/%{name}

%changelog
