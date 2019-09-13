#
# spec file for package bs-update
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bs-update
Version:        0.18
Release:        0
Summary:        Automate maintenance of packages in a Build Service
License:        MIT
Group:          Development/Tools/Version Control
Url:            https://github.com/roman-neuhauser/bs-update
Source0:        https://github.com/roman-neuhauser/bs-update/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        PKGBUILD
BuildRequires:  coreutils
BuildRequires:  filesystem
BuildRequires:  gzip
BuildRequires:  make
BuildRequires:  zsh
Requires:       coreutils
Requires:       gzip
Requires:       osc
Requires:       sed
Requires:       tar
Requires:       wget
Requires:       zsh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
bs-update makes it easier to keep packages in a Build Service
up-to-date with respect to their upstream sources.

%prep
%setup -q

%build
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check PREFIX=%{_prefix}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%files
%defattr(-,root,root)
%{_bindir}/bs-update
%{_mandir}/man1/bs-update.1%{ext_man}

%changelog
