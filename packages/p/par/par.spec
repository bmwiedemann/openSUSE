#
# spec file for package par
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           par
Version:        1.1
Release:        0
Summary:        Parity Archive File Generator
License:        GPL-2.0-or-later
URL:            https://parchive.sourceforge.net/
Source:         https://sourceforge.net/projects/parchive/files/par/%{version}/par-v%{version}.tar.gz/download#/par-v%{version}.tar.gz
Patch0:         %{name}.diff
BuildRequires:  gcc
BuildRequires:  make

%description
Parchive creates extra parity data over several volumes. These can be
used to restore the complete archive after some data loss or
corruption.

%prep
%autosetup -p0 -n %{name}-cmdline

%build
%make_build

%install
%make_install

%check
# Upstream has no testsuite; smoke-test the core function end to end:
# create parity volumes, delete a data file, recover it, verify content.
mkdir check-tmp
pushd check-tmp
for i in 1 2 3; do
  head -c 100000 /dev/urandom > data$i.bin
done
md5sum data1.bin data2.bin data3.bin > before.md5
%{buildroot}%{_bindir}/par a -n2 test.par data1.bin data2.bin data3.bin
%{buildroot}%{_bindir}/par c test.par
rm data2.bin
%{buildroot}%{_bindir}/par r test.par
md5sum -c before.md5
popd

%files
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/par

%changelog
