#
# spec file for package xdelta3
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           xdelta3
Version:        3.1.0
Release:        0
Summary:        A diff utility which works with binary files
License:        Apache-2.0 AND GPL-2.0-only
URL:            https://github.com/jmacd/xdelta-gpl
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  pkgconfig(liblzma)
# xdelta is being dropped
Provides:       xdelta = %{version}
Obsoletes:      xdelta < %{version}

%description
Xdelta3 is a set of tools designed to compute changes between
binary files.  These changes (delta files) are similar to the output of the
"diff" program, in that they may be used to store and transmit only the
changes between files.  The "delta files" that Xdelta3 manages are
stored in RFC3284 (VCDIFF) format.

%package devel
Summary:        Header files for %{name}

%description devel
%{summary}.

%prep
%autosetup

%build
%configure
%ifarch ppc64 s390x
%define do_profiling 0
%endif
%if %{do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}" CXXFLAGS="%{optflags} %{cflags_profile_generate}"
  ./xdelta3 test
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}" CXXFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
%endif

%install
%make_install

# Create compat symlinks
ln -sv %{_bindir}/xdelta3 \
  %{buildroot}%{_bindir}/xdelta
ln -sv %{_mandir}/man1/xdelta3.1 \
  %{buildroot}%{_mandir}/man1/xdelta.1

# installing header files
find . -maxdepth 1 -type f -name "*.h" -exec install -t %{buildroot}%{_includedir}/%{name} -Dpm0644 {} +

%check
./xdelta3regtest

%files
%license COPYING
%doc README.md
%{_bindir}/xdelta
%{_bindir}/xdelta3
%{_mandir}/man1/xdelta.1%{?ext_man}
%{_mandir}/man1/xdelta3.1%{?ext_man}

%files devel
%{_includedir}/%{name}

%changelog
