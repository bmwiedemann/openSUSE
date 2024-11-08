#
# spec file for package linux-ftools
#
# Copyright (c) 2024 SUSE LLC
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


Name:           linux-ftools
Version:        1.3.1
Release:        0
Summary:        Linux command line tools for fallocate, fincore, fadvise, etc
License:        Apache-2.0
Group:          Development/Debug
URL:            http://code.google.com/p/linux-ftools/
Source:         linux-ftools-%{version}.tar.gz
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
%setup -q -n linux-ftools-%{version}

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D -m 0755 fallocate %{buildroot}%{_bindir}/linux-fallocate
install -D -m 0755 fadvise %{buildroot}%{_bindir}/linux-fadvise
install -D -m 0755 fincore %{buildroot}%{_bindir}/linux-fincore
rm %{buildroot}%{_bindir}/fallocate
rm %{buildroot}%{_bindir}/fadvise
rm %{buildroot}%{_bindir}/fincore

%files
%defattr(-,root,root)
%doc COPYING README.md
%{_bindir}/linux-fallocate
%{_bindir}/linux-fadvise
%{_bindir}/linux-fincore

%changelog
