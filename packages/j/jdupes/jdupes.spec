#
# spec file for package jdupes
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019-2020 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           jdupes
Version:        1.21.1
Release:        0
Summary:        A powerful duplicate file finder and an enhanced fork of 'fdupes'
License:        MIT
Group:          Productivity/File utilities
URL:            https://github.com/jbruchon/jdupes
Source0:        https://github.com/jbruchon/jdupes/archive/refs/tags/v%{version}.tar.gz
Source1:        macros.jdupes
Source2:        jdupes_wrapper.cpp
BuildRequires:  gcc-c++

%description
A program for identifying and taking actions upon duplicate files.

A WORD OF WARNING: jdupes IS NOT a drop-in compatible replacement for fdupes!
Do not blindly replace fdupes with jdupes in scripts and expect everything to
work the same way. Option availability and meanings differ between the two
programs.

%prep
%setup -q

%build
make %{?_smp_mflags} \
     ENABLE_DEDUPE=1 \
     STATIC_DEDUPE_H=1
g++ %{optflags} -O2 -Wall %{SOURCE2} -o jdupes_wrapper

%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix} install
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.%{name}
install -D -m755 jdupes_wrapper  %{buildroot}/usr/lib/rpm/jdupes_wrapper

%check
./jdupes -q -r testdir

%files
%license LICENSE
%doc CHANGES README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_rpmmacrodir}/macros.%{name}
/usr/lib/rpm/jdupes_wrapper

%changelog
