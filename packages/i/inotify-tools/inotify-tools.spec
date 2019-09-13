#
# spec file for package inotify-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.20.1
Release:        0
Summary:        Tools for inotify
License:        GPL-2.0-only
Group:          System/Monitoring
Url:            https://github.com/rvoicilas/inotify-tools/wiki/
Source:         http://github.com/rvoicilas/inotify-tools/archive/%{version}.tar.gz
# PATCH-FIX-OPENSUSE inotify-return.patch -- add a forgotten return value
Patch0:         inotify-return.patch
# PATCH-FIX-OPENSUSE inotify-tools-no-timestamp-in-doc.patch bmwiedemann -- Normalize timestamps in man page - https://github.com/rvoicilas/inotify-tools/pull/97
Patch1:         inotify-tools-no-timestamp-in-doc.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure --disable-static \
    --docdir=%{_docdir}/%{name} \
    --enable-doxygen
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes %{buildroot}/%{_docdir}
rm %{buildroot}/%{_libdir}/libinotifytools.la

%post -n libinotifytools0 -p /sbin/ldconfig

%postun -n libinotifytools0 -p /sbin/ldconfig

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_bindir}/inotifywait
%{_bindir}/inotifywatch
%{_mandir}/man1/inotifywait.1.gz
%{_mandir}/man1/inotifywatch.1.gz

%files -n libinotifytools0
%defattr(-,root,root)
%license COPYING
%{_libdir}/libinotifytools.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libinotifytools.so
%{_includedir}/inotifytools/

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}

%changelog
