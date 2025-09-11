#
# spec file for package obs-git-init
#
# Copyright (c) 2025 SUSE LLC
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


Name:           obs-git-init
Version:        0.2.3
Release:        0
Summary:        A help service to setup git repositories for OBS
License:        GPL-2.0-or-later
URL:            https://src.opensuse.org/adrianSuSE/obs-git-init
Source0:        %{name}-%{version}.tar.xz
Requires:       perl(Config::INI)
Requires:       perl(Config::IniFiles)
BuildArch:      noarch

%description

%prep
%setup -q

%build

%install
make DESTDIR=%{buildroot} install

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_prefix}/lib/obs

%changelog
