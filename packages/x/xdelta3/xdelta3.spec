#
# spec file for package xdelta3
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


Name:           xdelta3
Version:        3.1.0
Release:        0
Summary:        A diff utility which works with binary files
License:        GPL-2.0-only AND Apache-2.0
Group:          Productivity/Archiving/Compression
Url:            http://xdelta.org/
Source0:        https://github.com/jmacd/xdelta-devel/releases/download/v%{version}/xdelta3-%{version}.tar.gz
BuildRequires:  gcc-c++
%if 0%{?opensuse}
# Dependency of tests
BuildRequires:  ncompress
%endif
BuildRequires:  python
BuildRequires:  xz-devel
# xdelta is being dropped
Provides:       xdelta = %{version}
Obsoletes:      xdelta < %{version}

%description
Xdelta3 is a set of tools designed to compute changes between
binary files.  These changes (delta files) are similar to the output of the
"diff" program, in that they may be used to store and transmit only the
changes between files.  The "delta files" that Xdelta3 manages are
stored in RFC3284 (VCDIFF) format.

%prep
%setup -q

%build
%configure
%if %{do_profiling}
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_generate}" CXXFLAGS="%{optflags} %{cflags_profile_generate}"
  ./xdelta3 test 
  make clean
  make %{?_smp_mflags} CFLAGS="%{optflags} %{cflags_profile_feedback}" CXXFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
%endif

%install
%make_install

# Create compat symlinks
ln -sv %{_bindir}/xdelta3 \
  %{buildroot}%{_bindir}/xdelta
ln -sv %{_mandir}/man1/xdelta3.1 \
  %{buildroot}%{_mandir}/man1/xdelta.1

%check
./xdelta3 test

%files
%defattr(-, root, root)
%doc COPYING README.md
%{_bindir}/xdelta
%{_bindir}/xdelta3
%{_mandir}/man1/xdelta.1%{ext_man}
%{_mandir}/man1/xdelta3.1%{ext_man}

%changelog
