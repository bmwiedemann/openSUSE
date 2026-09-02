#
# spec file for package pool-git-init
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


Name:           pool-git-init
Version:        0.3.1
Release:        0
Summary:        Helper services to setup git repositories for packaging
License:        GPL-2.0-or-later
URL:            https://src.opensuse.org/openSUSE/pool-git-init
Source0:        %{name}-%{version}.tar.xz
Requires:       perl(Config::INI)
Requires:       perl(Config::IniFiles)
Recommends:     obs-service-format_spec_file
Provides:       obs-git-init = %version
Obsoletes:      obs-git-init < 0.3.0
BuildArch:      noarch

%description

%prep
%setup -q

%build

%install
make DESTDIR=%{buildroot} install

%posttrans
# because rpm itself can not replace directory with a symlink
# 1st we still may have a remaining empty directory, clean it
[ -d %{_prefix}/lib/obs/helper ] && rmdir %{_prefix}/lib/obs/helper
# create the compat symlink
[ -e %{_prefix}/lib/obs/helper ] || ln -sf ../pool/helper %{_prefix}/lib/obs/

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%dir %{_prefix}/lib/obs
%ghost %{_prefix}/lib/obs/helper
%{_prefix}/lib/pool

%changelog
