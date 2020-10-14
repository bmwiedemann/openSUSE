#
# spec file for package fabtests
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


%define git_ver .0.6c51de3d7817

Name:           fabtests
Version:        1.11.1
Release:        0
Summary:        Test suite for libfabric API
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Development/Tools/Other
URL:            http://www.github.com/ofiwg/libfabric
Source:         libfabric-%{version}%{git_ver}.tar.bz2
Source1:        fabtests-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libfabric-devel = %{version}
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Fabtests provides a set of examples that uses libfabric, a fabric software library.

%prep
%setup -q -n  libfabric-%{version}%{git_ver}

%build
cd fabtests
./autogen.sh
%configure %{?_with_libfabric}
make %{?_smp_mflags}

%install
%make_install -C fabtests

%files
%defattr(-,root,root)
%dir %{_datadir}/fabtests/

%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_datadir}/fabtests/*

%doc AUTHORS README NEWS.md
%license COPYING

%changelog
