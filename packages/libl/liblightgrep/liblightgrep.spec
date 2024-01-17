#
# spec file for package liblightgrep
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname 0

Name:           liblightgrep
%define lname %{name}%soname
Version:        1.4
Release:        0
Summary:        Multipattern regular expression searching for digital forensics
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
Url:            https://github.com/jonstewart/liblightgrep
# The original archive contains tests : 155MB. As we don't run them, save space by removing them :
# /pytest, /re_gen and /test
#Source:         https://github.com/LightboxTech/liblightgrep/archive/v%{version}.tar.gz
Source:         %{name}-%{version}.tar.xz
Patch0:         aarch64_and_ppc64le.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
# With v1.2.1, to run the %check section, you may need extra modules:
# - Boost::asio
# - Boost::chrono
# - Boost::program_options
# - Boost::system
# - Boost::thread
# - Scope (a git submodule)

%description
liblightgrep is a regular expression engine designed
for digital forensics.

* it searches for many patterns simultaneously,
* searches binary data as a stream, not as discrete lines of text,
* searches for patterns in many different encodings,
* is a forward-looking only engine

%package -n %{lname}
Summary:        Multipattern regular expression searching for digital forensics
License:        LGPL-3.0-or-later
Group:          System/Libraries

%description -n %lname
liblightgrep is a regular expression engine designed
for digital forensics.

* it searches for many patterns simultaneously,
* searches binary data as a stream, not as discrete lines of text,
* searches for patterns in many different encodings,
* is a forward-looking only engine

%package devel
Summary:        Development files for liblightgrep
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description devel
Development files for liblightgrep, a regex engine designed for digital forensics.

This subpackage contains libraries and header files for developing
applications that want to make use of %{name}.

%prep
%setup -q
%patch0 -p1
#The test file test_kilopattern.CPP breaks ARM builds
find . -name 'test_kilopattern.CPP' -delete

%build
autoreconf -i
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%check
#these take many minutes, so don't run them all the time
#   THIS IS FAILING TO BUILD WITH v1.2.1, so comment out
#make check

%files -n %lname
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_libdir}/liblightgrep.so.*

%files devel
%defattr(-,root,root)
%doc README.md
%license COPYING
%{_includedir}/lightgrep/
%{_libdir}/liblightgrep.so
%{_libdir}/pkgconfig/lightgrep.pc

%changelog
