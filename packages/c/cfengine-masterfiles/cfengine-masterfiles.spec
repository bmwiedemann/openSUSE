#
# spec file for package cfengine-masterfiles
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cfengine-masterfiles

# Yes, its not FHS conformant but in sync with cfengine documentation
# reported upstream as https://cfengine.com/dev/issues/1896
%define         basedir   /var/cfengine
%define         workdir   %{basedir}

Summary:        CFEngine promises master files
License:        MIT AND LGPL-3.0-or-later
Group:          Productivity/Networking/System
Version:        3.12.0
Release:        0
%define srcname masterfiles
Url:            http://www.cfengine.org/
Source:         https://github.com/cfengine/masterfiles/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires:       cfengine
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cfengine
BuildRequires:  findutils

# wtf? SLE_11 does not honor rpmlintrc
Source1:        %{name}-rpmlintrc
%if 0%{?suse_version} <= 1130
BuildRequires:  -post-build-checks
%endif
%if 0%{?fedora_version} == 20 || 0%{?rhel_version} >= 700
BuildRequires:  perl-Exporter
%endif

%description
Masterfiles are the pristine version of the CFEngine promises. These
will be available in /var/cfengine/masterfiles and are copied to
/var/cfengine/inputs by CFEngine.

%prep
%setup -q -n %{srcname}-%{version}

%build
# EXPLICIT_VERSION must be set in the environment else creation of
# configure will fail
export EXPLICIT_VERSION="%{version}" 
autoreconf -fiv
%configure --prefix=%{basedir}

%install

%{__install} -d %{buildroot}/%{basedir}/masterfiles
%{__make} "DESTDIR=%{buildroot}" install

%files
%defattr(-,root,root)
%doc README.md CONTRIBUTING.md
%license LICENSE
%dir %{basedir}
%dir %{basedir}/masterfiles
%{basedir}/masterfiles/*
%dir %{basedir}/modules/packages
%{basedir}/modules/packages/*

%changelog
