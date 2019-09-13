#
# spec file for package linux-ftools
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define hg_version 2a7918d4b81b
Name:           linux-ftools
Version:        1.3
Release:        0
Summary:        Linux command line tools for fallocate, fincore, fadvise, etc
License:        Apache-2.0
Group:          Development/Debug
Url:            http://code.google.com/p/linux-ftools/
Source:         linux-ftools-%{hg_version}.tar.gz
Source1:        COPYING
Patch0:         gcc46.diff
Patch1:         linux-ftools_use_asm_unistd_h.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make

%description
These are tools designed for working with modern linux system calls including,
mincore, fadvise, etc.

We designed these primarily to work in high performance environments to
determine information about the running kernel, improve system performance, and
debug performance problems.

%prep
%setup -q -n linux-ftools-%{hg_version}
%patch0
%patch1 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}
cp %{S:1} .

%install
make install DESTDIR=%{buildroot}
# already shipped by util-linux
rm -f %{buildroot}%{_bindir}/linux-fallocate

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/linux-fadvise
%{_bindir}/linux-fincore

%changelog
