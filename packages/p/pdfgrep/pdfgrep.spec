#
# spec file for package pdfgrep
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pdfgrep
Version:        2.1.2
Release:        0
Summary:        Search in pdf files for strings matching a regular expression
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            http://pdfgrep.sourceforge.net/
Source:         https://pdfgrep.org/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel >= 1.0.0
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(poppler-cpp)

%description
Pdfgrep is a tool to search text in PDF files. It works similar to `grep'.

Features:
- search for regular expressions.
- support for some important grep options, including:
+ filename output.
+ page number output.
+ optional case insensitivity.
+ count occurrences.

%prep
%setup -q

%build
%configure \
  --with-bash-completion
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}

%changelog
