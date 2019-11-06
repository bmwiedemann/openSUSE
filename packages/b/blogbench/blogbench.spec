#
# spec file for package blogbench
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


Name:           blogbench
Version:        1.1
Release:        0
Summary:        Filesystem Benchmark
License:        ISC
URL:            https://www.pureftpd.org/project/blogbench
Source0:        https://download.pureftpd.org/pub/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://download.pureftpd.org/pub/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
Patch1:         fix-rewriters-argcount.patch

%description
Blogbench is a portable filesystem benchmark that tries to reproduce the load
of a real-world busy file server. It stresses the filesystem with multiple
threads performing random reads, writes, and rewrites in order to get a
realistic idea of the scalability and the concurrency a system can handle.

%prep
%setup -q
%patch1 -p1

%build
%configure --enable-dependency-tracking --with-largefile
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/blogbench
%{_mandir}/man8/blogbench.8%{?ext_man}

%changelog
