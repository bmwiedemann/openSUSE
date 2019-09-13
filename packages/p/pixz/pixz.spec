#
# spec file for package pixz
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if ( 0%{?centos_version} && 0%{?centos_version} < 700 ) || ( 0%{?rhel_version} && 0%{?rhel_version} <= 700 )
%define use_static_libarchive 1
%else
%define use_static_libarchive 0
%endif

%if ( 0%{?centos_version} && 0%{?centos_version} < 700 ) || ( 0%{?rhel_version} && 0%{?rhel_version} < 700 )
%define use_static_lzma 1
%else
%define use_static_lzma 0
%endif

Name:           pixz
Version:        1.0.6
Release:        0
Summary:        Parallel, indexing version of XZ
License:        BSD-2-Clause
Group:          Productivity/Archiving/Compression
Url:            https://github.com/vasi/pixz
Source:         https://github.com/vasi/pixz/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{use_static_libarchive}
BuildRequires:  libarchive-static-devel >= 2.8
%else
%if 0%{?suse_version} <= 1110
BuildRequires:  libarchive-devel >= 2.8
%else
BuildRequires:  pkgconfig(libarchive) >= 2.8
%endif
%endif
%if %{use_static_lzma}
BuildRequires:  xz-static-devel >= 4.999.9-beta-212
%else
%if 0%{?suse_version} <= 1110
BuildRequires:  xz-devel >= 4.999.9-beta-212
%else
BuildRequires:  pkgconfig(liblzma) >= 4.999.9-beta-212
%endif
%endif
# compatibility tests run classic xz
BuildRequires:  xz

%description
The existing XZ Utils provide great compression in the .xz file format, but
they produce just one big block of compressed data. Pixz instead produces a
collection of smaller blocks which makes random access to the original data
possible. This is especially useful for large tarballs.

Pixz supports automatic indexing and parallel compression and decompression
using all available CPU cores.

%prep
%setup -q

%build
%if %{use_static_libarchive}
export LIBARCHIVE_LIBS="-Wl,-Bstatic -larchive -Wl,-Bdynamic,-lbz2"
%endif
%if %{use_static_lzma}
export LZMA_LIBS="-Wl,-Bstatic -llzma -Wl,-Bdynamic"
%endif
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%check
make check

%files
%defattr(-,root,root)
%doc NEWS TODO README.md LICENSE
%{_bindir}/pixz
%{_mandir}/man1/pixz.1.gz

%changelog
