#
# spec file for package imgen (Version 1.0)
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           imgen
Summary:        Mellanox Firmware Generator
Version:        1.0
Release:        2.7
License:        GPL-2.0
Group:          System/Console
Source0:        %{name}-%{version}.tar.bz2
Source1:        mic.1
Source2:        t2a.1
Patch0:         imgen-makefile.patch	
Patch1:         imgen-missing_headers.patch
Patch2:         imgen-use_cpp_headers.patch
Patch3:         imgen-string_const_to_charp.patch
Patch4:         imgen-aliasing.patch
Url:            http://www.openfabrics.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++ zlib-devel
BuildRequires:  automake autoconf libtool
BuildRequires:  libexpat-devel

%description
FW Image Generator from FW release for all Mellanox devices (except
Anafa)

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
rm -fr .git

%build
make CFLAGS="%{optflags}"

%install
install -D t2a %{buildroot}%{_bindir}/t2a
install -D mic %{buildroot}%{_bindir}/mic
install -d %{buildroot}%{_mandir}/man1
install -m 644 %{S:1} %{S:2} %{buildroot}%{_mandir}/man1
gzip -9 %{buildroot}%{_mandir}/man1/*.1

%files
%defattr(-, root, root)
%doc COPYING
%_bindir/*
%doc %{_mandir}/man1/t2a.1.gz
%doc %{_mandir}/man1/mic.1.gz

%changelog
