#
# spec file for package guile-newt
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


Name:           guile-newt
Version:        0.0.1
Release:        0
Summary:        Guile bindings to Newt
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://gitlab.com/mothacehe/guile-newt
Source0:        https://gitlab.com/mothacehe/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        guile-newt-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel
BuildRequires:  newt-devel
BuildRequires:  pkg-config
Requires:       guile
Requires:       newt-devel

%description
This package provides Guile bindings to Newt, a library for text based user
interfaces.

%prep
%setup -q

%build
./bootstrap
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%files
%{_datadir}/guile/*
%{_libdir}/guile/*

%changelog
