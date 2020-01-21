#
# spec file for package guile-parted
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


Name:           guile-parted
Version:        0.0.2
Release:        0
Summary:        Guile bindings to Parted
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://gitlab.com/mothacehe/guile-parted
Source0:        https://gitlab.com/mothacehe/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        guile-parted-rpmlintrc
# Support Guile 3.0. Patch proposed upstream in https://gitlab.com/mothacehe/guile-parted/merge_requests/1
Patch0:         support-guile-3.0.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-bytestructures
BuildRequires:  guile-devel
BuildRequires:  parted-devel
BuildRequires:  pkg-config
Requires:       guile
Requires:       guile-bytestructures
Requires:       parted-devel

%description
This package provides Guile bindings to GNU Parted.

%prep
%setup -q
%patch0 -p1

%build
./bootstrap
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README.org
%license COPYING
%{_datadir}/guile/*
%{_libdir}/guile/*

%changelog
