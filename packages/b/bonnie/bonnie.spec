#
# spec file for package bonnie
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bonnie
Version:        1.6
Release:        0
Summary:        File System Benchmark
License:        GPL-2.0-or-later
URL:            https://code.google.com/p/bonnie-64/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         bonnie-fix-o_direct.diff

%description
Bonnie is a popular performance benchmark that targets various aspects
of Unix file systems.

%prep
%setup -q -n %{name}
%patch0

%build
make SYSFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install

%files
%doc bonnie.doc README
%{_bindir}/bonnie
%{_mandir}/man1/bonnie.1%{?ext_man}

%changelog
