#
# spec file for package openlmi-pegasus-compat
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


Name:           openlmi-pegasus-compat
Summary:        Class definitions to make openlmi providers work with sfcb
License:        MIT
Group:          System/Management
Url:            https://www.opensuse.org
Version:        0.1
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        15_PG_ProviderModule20.mof
Source1:        16_PG_ServerProfile20.mof
Source2:        LICENSE
BuildArch:      noarch

Requires:       sblim-sfcb

# for directory ownership
BuildRequires:  sblim-sfcb

%description
The openlmi providers reference Pegasus internal classes for their
root/interop (indications) implementations. This package provides the
respective class definitions for sfcb.

%prep

%build
cp %{S:2} .

%install
mkdir -p $RPM_BUILD_ROOT/var/lib/sfcb/stage/mofs/root/interop
cp %{S:0} $RPM_BUILD_ROOT/var/lib/sfcb/stage/mofs/root/interop
cp %{S:1} $RPM_BUILD_ROOT/var/lib/sfcb/stage/mofs/root/interop

%post
/usr/bin/sfcbrepos -f

%files
%defattr(-, root, root)
%doc LICENSE
/var/lib/sfcb/stage/mofs/root/interop/*

%changelog
