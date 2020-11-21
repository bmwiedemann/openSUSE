#
# spec file for package stdman
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


Name:           stdman
Version:        2018.03.11
Release:        0
Summary:        C++ stdlib man pages
License:        MIT
Group:          Documentation/Man
URL:            https://github.com/jeaye/stdman
Source0:        https://github.com/jeaye/stdman/archive/2018.03.11.tar.gz
BuildArch:      noarch
Requires:       man

%description
stdman is a tool that parses archived HTML files from cppreference and generates groff-formatted manual pages for Unix-based systems. The goal is to provide excellent formatting for easy readability.

This package provides the full cppreference documentation in the man format.

%prep
%setup -q

%build
%configure

%install
# INSTEAD OF RUNNING make install, WHICH WOULD HAVE INSTALLED GZIP
# COMPRESSED MAN FILES TO MAN DIR, COPY UNCOMPRESSED MAN FILES TO
# man DIR AND LET brp-compress TAKE CARE OF GZIP COMPRESSION.
# brp-compress FREAKS OUT WHEN IT FINDS ALREADY COMPRESSED FILES
# WITH SPECIAL CHARACTERS IN THEM: SEE
# https://bugzilla.opensuse.org/show_bug.cgi?id=1087430
mkdir -p %{buildroot}%{_mandir}/man3
cp -pr ./man/*.3 %{buildroot}%{_mandir}/man3/

%files
%doc README.md
%license LICENSE
%{_mandir}/man3/*.3.gz

%changelog
