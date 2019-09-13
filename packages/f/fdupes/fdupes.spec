#
# spec file for package fdupes
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

# Upstream calls this version 1.6.1, but that version number is *lower* than
# previously released ones, like 1.51, so we mangle the number to keep
# continuity: https://github.com/adrianlopezroche/fdupes/issues/74.
%global upstream_version 1.6.1

Name:           fdupes
Version:        1.61
Release:        0
Summary:        Identifying or deleting duplicate files
License:        MIT
Group:          Productivity/Archiving/Compression
Url:            https://github.com/adrianlopezroche/fdupes
Source0:        https://github.com/adrianlopezroche/fdupes/archive/v%{upstream_version}.tar.gz#/%{name}-%{upstream_version}.tar.gz
Source1:        macros.fdupes
#PATCH-FIX-SUSE: fix patch according distro's needs
Patch0:         fdupes-makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%prep
%setup -q -n %{name}-%{upstream_version}
%patch0

%build
make %{?_smp_mflags} COMPILER_OPTIONS="%{optflags}"

%install
install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.%{name}

%check
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir

%files
%defattr(-, root, root)
%doc CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_rpmmacrodir}/macros.%{name}

%changelog
