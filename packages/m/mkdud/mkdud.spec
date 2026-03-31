#
# spec file for package mkdud
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


Name:           mkdud
Version:        2.6
Release:        0
Summary:        Create driver update disks (DUD).
License:        GPL-3.0-or-later
Group:          Hardware/Other
Source:         %{name}-%{version}.tar.xz
URL:            https://github.com/openSUSE/mkdud
Requires:       binutils
Requires:       coreutils
Requires:       cpio
Requires:       file
Requires:       findutils
Requires:       (gpg2 or gnupg2)
Requires:       grep
Requires:       gzip
Requires:       kmod
Requires:       (mkisofs or xorriso)
Recommends:     osc
Requires:       rpm
Requires:       rpm-build
Requires:       tar
Requires:       util-linux
Requires:       xz
Requires:       zstd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Create driver update disks (DUD).

Authors:
--------
    Steffen Winterfeldt

%prep
%setup

%build

%install
  %make_install
  install -D -m 644 mkdud.1 %{buildroot}%{_mandir}/man1/mkdud.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/mkdud
/usr/share/bash-completion
%doc %{_mandir}/man1/mkdud.*
%doc *.md
%if 0%{?suse_version} >= 1500 || 0%{?suse_version} == 0
%license COPYING
%else
%doc COPYING
%endif

%changelog
