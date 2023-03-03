#
# spec file for package paperjam
#
# Copyright (c) 2023 SUSE LLC
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


Name:           paperjam
Version:        1.1.1
Release:        0
Summary:        A tool for transforming PDF documents
License:        GPL-2.0-or-later
URL:            https://mj.ucw.cz/sw/paperjam/
Source:         http://mj.ucw.cz/download/linux/paperjam-%{version}.tar.gz
Patch0:         reproducible.patch
Patch1:         stop_using_obsolete_standards.patch
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  libpaper-devel
BuildRequires:  qpdf-devel

%description
PaperJam is a tool for processing PDF documents: re-ordering pages,
scaling and rotating them, placing multiple pages on one sheet of paper,
adding cropmarks, and many other tricks.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build

%install
%make_install PREFIX="/usr"

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/paperjam
%{_mandir}/man1/paperjam.1%{?ext_man}

%changelog
