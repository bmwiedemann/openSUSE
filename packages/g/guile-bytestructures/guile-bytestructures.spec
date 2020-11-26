#
# spec file for package guile-bytestructures
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


Name:           guile-bytestructures
Version:        1.0.9
Release:        0
Summary:        Bytestructures for Guile
License:        GPL-3.0-only
Group:          Development/Libraries/Other
URL:            https://github.com/TaylanUB/scheme-bytestructures
Source0:        https://github.com/TaylanUB/scheme-bytestructures/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel >= 2.0
Requires:       guile
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This library offers a system imitating the type system of the C programming
language, to be used on bytevectors within Guile.

%prep
%setup -q -n scheme-bytestructures-%{version}

%build
autoreconf -fi
%configure --prefix=/usr
make %{?_smp_mflags}

%install
%make_install %{_smp_mflags}

%files
%defattr(-,root,root)
%license COPYING
%doc README.md
%dir %{_datadir}/guile/site/*
%{_datadir}/guile/site/*
%dir %{_libdir}/guile/*/site-ccache
%{_libdir}/guile/*/site-ccache/bytestructures*

%changelog
