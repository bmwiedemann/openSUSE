#
# spec file for package rfcdiff
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


Name:           rfcdiff
Version:        1.47
Release:        0
Summary:        Draft Diff Tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://tools.ietf.org/tools/rfcdiff/index
Source:         https://tools.ietf.org/tools/rfcdiff/%{name}-%{version}.tgz
Source2:        https://tools.ietf.org/tools/rfcdiff/distinfo
BuildRequires:  txt2man
BuildArch:      noarch

%description
The purpose of this program is to compare two versions of an
Internet Draft, and as output produce a diff in one of several
formats:
- side-by-side HTML diff
- paged wdiff output in a text terminal
- a text file with changebars in the left margin
- a simple unified diff output

%prep
echo "`grep %{name}-%{version}.tgz %{SOURCE2} | grep MD5 | head -n1 | cut -d= -f2`  %{SOURCE0}" | md5sum -c
echo "`grep %{name}-%{version}.tgz %{SOURCE2} | grep SHA256 | head -n1 | cut -d= -f2`  %{SOURCE0}" | sha256sum -c
%setup -q

%build
make %{?_smp_mflags} manpage

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -p -m 0755 %{name} %{buildroot}%{_bindir}/
install -p -m 0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/

%files
%doc changelog copyright
%{_bindir}/*
%{_mandir}/man*/*

%changelog
