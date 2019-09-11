#
# spec file for package newlib
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


Name:           newlib
Version:        3.1.0
Release:        0
Summary:        C library intended for use on embedded systems
License:        BSD-3-Clause AND MIT AND LGPL-2.0-or-later AND ISC
Group:          Development/Tools
Url:            https://sourceware.org/newlib/
Source0:        ftp://sourceware.org/pub/newlib/newlib-%{version}.tar.gz

Patch1:         epiphany-fixes.diff

%if %{suse_version} > 1220
BuildRequires:  makeinfo
%else
BuildRequires:  texinfo
%endif

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts, all under free software licenses
that make them easily usable on embedded products.

%prep
%setup -q
%patch1 -p1

%build
mkdir build-dir
cd build-dir
# On %%ix86 hosts newlib is documented to be buildable as shared library via --with-newlib,
# but it fails to build for us and we don't need a host library at the moment.
../configure \
	--prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
%ifarch %ix86
%if 0
	--with-newlib \
%endif
%endif
	CFLAGS="%{optflags}"

make %{?_smp_mflags}

%install
cd build-dir
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING.NEWLIB COPYING.LIBGLOSS COPYING COPYING.LIB COPYING3 COPYING3.LIB
%doc newlib/README newlib/NEWS

%changelog
