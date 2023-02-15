#
# spec file for package cfengine-masterfiles
#
# Copyright (c) 2023 SUSE LLC
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


# Yes, its not FHS conformant but in sync with cfengine documentation
%define basedir   %{_localstatedir}/cfengine
%define workdir   %{basedir}

%define srcname masterfiles
Name:           cfengine-masterfiles
Version:        3.21.0
Release:        0
Summary:        CFEngine promises master files
License:        LGPL-3.0-or-later AND MIT
Group:          Productivity/Networking/System
URL:            https://cfengine.com/
Source:         https://github.com/cfengine/masterfiles/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cfengine
BuildRequires:  findutils
Requires:       cfengine
BuildArch:      noarch
%if 0%{?fedora_version} == 20 || 0%{?rhel_version} >= 700
BuildRequires:  perl-Exporter
%endif

%description
Masterfiles are the pristine version of the CFEngine promises. These
will be available in %{basedir}/masterfiles and are copied to
%{basedir}/inputs by CFEngine.

%prep
%setup -q -n %{srcname}-%{version}

%build
# EXPLICIT_VERSION must be set in the environment else creation of
# configure will fail
export EXPLICIT_VERSION="%{version}"
autoreconf -fiv
%configure --prefix=%{basedir}

%install
%make_install

%files
%license LICENSE
%doc README.md CONTRIBUTING.md
%{basedir}/masterfiles

%changelog
