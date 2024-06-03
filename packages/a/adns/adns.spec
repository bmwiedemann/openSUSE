#
# spec file for package adns
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lname	libadns1
Name:           adns
Version:        1.6.1
Release:        0
Summary:        Advanced Easy-to-Use Asynchronous-Capable DNS Utilities
License:        GPL-2.0-or-later
Group:          Productivity/Networking/DNS/Utilities
URL:            https://www.chiark.greenend.org.uk/~ian/adns/ftp/
Source0:        http://www.chiark.greenend.org.uk/~ian/adns/ftp/%{name}-%{version}.tar.gz
Source1:        http://www.chiark.greenend.org.uk/~ian/adns/ftp/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        README.SUSE
Source4:        baselibs.conf
Patch1:         adns-1.4-configure.patch
Patch2:         adns-visibility.patch
BuildRequires:  autoconf

%description
adns includes a collection of useful DNS resolver utilities.

%package -n %{lname}
Summary:        Advanced DNS resolver client library
Group:          System/Libraries
Provides:       libadns = %{version}
#openSUSE 10.2
Obsoletes:      libadns <= 1.3

%description -n %{lname}
Libadns is an advanced, easy to use, asynchronous-capable DNS resolver
client library for C (and C++) programs.

%package -n libadns-devel
Summary:        Libraries and header files to develop programs with libadns support
Group:          Development/Languages/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel

%description -n libadns-devel
Libadns-devel includes the header file and static library to develop
programs with libads support.

%prep
%autosetup -p0
cp %{SOURCE3} .

%build
autoreconf -fiv
%configure
%make_build

%install
make install \
    prefix=%{buildroot}%{_prefix} \
    bindir=%{buildroot}%{_bindir} \
    includedir=%{buildroot}%{_includedir} \
    libdir=%{buildroot}%{_libdir} \

# FIXME: --disable-static not available
rm %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets -n %{lname}

%check
## Fails without network
#%%make_build check

%files
%license COPYING
%doc GPL-vs-LGPL README* TODO changelog
%{_bindir}/adns*

%files -n %{lname}
%license COPYING
%{_libdir}/libadns.so.1*

%files -n libadns-devel
%license COPYING
%{_includedir}/adns.h
%{_libdir}/libadns.so

%changelog
