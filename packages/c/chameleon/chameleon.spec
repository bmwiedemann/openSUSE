#
# spec file for package chameleon
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define chameleon_home %{_datadir}/%{name}
Name:           chameleon
Version:        0.2
Release:        0
Summary:        Common schema transformation tool
License:        LGPL-3.0+
Group:          Development/Libraries
Url:            https://fedorahosted.org/chameleon
Source0:        https://fedorahosted.org/releases/c/h/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  python
Requires:       python
Requires:       python-ply
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Chameleon is a common to database specific schema transformation tool.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{chameleon_home}
cp -p chameleon/*.py %{buildroot}/%{chameleon_home}
install -m 0755 chameleon.bin %{buildroot}/%{_bindir}/chameleon

%files
%defattr(-,root,root,-)
%doc LICENSE README
%dir %{chameleon_home}
%{chameleon_home}/*
%{_bindir}/chameleon

%changelog
