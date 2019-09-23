#
# spec file for package gdata-sharp
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


Name:           gdata-sharp
Version:        1.4.0.2
Release:        0
Summary:        Google Data APIs (GData) for Mono/.NET
License:        Apache-2.0
Group:          Development/Libraries/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  mono-devel
BuildRequires:  nunit-devel
Provides:       google-gdata
BuildArch:      noarch
Url:            https://code.google.com/archive/p/google-gdata/
Source:         https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/google-gdata/libgoogle-data-mono-%{version}.tar.gz
# PATCH-FIX-UPSTREAM http://code.google.com/p/google-gdata/source/detail?spec=svn933&r=890
Patch0:         gdata-sharp-core-pc.patch
# PATCH-FIX-OPENSUSE
Patch1:         gdata-sharp-runtime-4.5.patch
# PATCH-FIX-OPENSUSE gdata-sharp-find-nunit.patch dimstar@opensuse.org -- Use pkgconfig to find the right parameters to link nunit
Patch2:         gdata-sharp-find-nunit.patch
# PATCH-FIX-UPSTREAM https://github.com/google/google-gdata/pull/725
Patch3:         gdata-sharp-reproducible.patch

%description
The GData .NET Client Library provides a library and source code
that make it easy to access data through Google Data APIs.

%package devel
Summary:        .NET library for the Google Data API
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package provides a simple protocol for the Google Data APIs (GData).

%prep
%setup -q -n libgoogle-data-mono-%{version}
%patch0

%if 0%{?suse_version} > 1110
# Mono >= 3.2 isn't available for SLE
%patch1 -p1
%endif
%if 0%{?suse_version} != 1320 && 0%{?suse_version} != 1310
%patch2 -p1
%endif
%patch3 -p1

%build
make PREFIX=%{_prefix}

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
mkdir %{buildroot}%{_datadir}
mv %{buildroot}%{_prefix}/lib/pkgconfig %{buildroot}%{_datadir}/

%files
%defattr(-,root,root)
%doc LICENSE-2.0.txt RELEASE_NOTES.HTML
%{_prefix}/lib/mono/gac/Google.GData.*
%{_prefix}/lib/mono/GData-Sharp

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/gdata-sharp*.pc

%changelog
