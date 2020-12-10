#
# spec file for package cpuminer
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cpuminer
Version:        2.5.1
Release:        0
Summary:        A multi-threaded CPU Bitcoin and Litecoin miner
License:        GPL-2.0-only
URL:            https://github.com/pooler/cpuminer
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  libjansson-devel
BuildRequires:  make

%description
An assembly optimized CPU miner for the Bitcoin and Litecoin cryptocurrencies, based on Jeff Garzik's reference cpuminer.

%prep
%setup -q

%build
./autogen.sh
%configure CFLAGS="%{optflags}"
%make_build

%install
%make_install

%files
%license LICENSE
%doc README NEWS
%{_bindir}/minerd
%{_mandir}/man1/minerd.1%{?ext_man}

%changelog
