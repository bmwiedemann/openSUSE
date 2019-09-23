#
# spec file for package pdfgrep
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pdfgrep
Version:        2.0.1
Release:        0
Summary:        Search in pdf files for strings matching a regular expression
License:        GPL-2.0+
Group:          Productivity/Text/Utilities
Url:            http://pdfgrep.sourceforge.net/
Source:         https://pdfgrep.org/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  libpoppler-devel
BuildRequires:  pcre-devel

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
%configure CXXFLAGS="%{optflags}" --with-bash-completion
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS.md README.md
%if 0%{?leap_version} >= 420200 || 0%{?suse_version} > 1320
%license COPYING
%else
%doc COPYING
%endif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}

%changelog
