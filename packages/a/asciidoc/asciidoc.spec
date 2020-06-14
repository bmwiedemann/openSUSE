#
# spec file for package asciidoc
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


Name:           asciidoc
Version:        9.0.0
Release:        0
Summary:        Text-Based Document Generation
License:        GPL-2.0-or-later
URL:            https://github.com/asciidoc/asciidoc-py3
Source0:        https://github.com/%{name}/%{name}-py3/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         asciidoc.version.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  python3-xml
Requires:       docbook-xsl-stylesheets
Requires:       python3-xml
Recommends:     dblatex
# a2x needs /usr/bin/xsltproc
Recommends:     libxslt
BuildArch:      noarch

%description
AsciiDoc is a text document format for writing short documents,
articles, books, and UNIX man pages. AsciiDoc files can be translated
to HTML and DocBook markups using the asciidoc command.

%package examples
Summary:        Examples and Documents for asciidoc

%description examples
This package contains examples and documents of asciidoc.

%prep
%autosetup -n %{name}-py3-%{version} -p1

# do not use env
find ./ -name \*.py -exec sed -i -e 's:%{_bindir}/env\ :%{_bindir}/:g' {} \;

%build
autoreconf -fiv
%configure

%install
%make_install

# Strip .py extension from binaries
pushd %{buildroot}%{_bindir}
	mv %{name}.py %{name}
	mv a2x.py a2x
popd

%files
%license COPYRIGHT
%doc README.asciidoc BUGS.txt CHANGELOG.txt
%config %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/a2x
%{_mandir}/man1/*

%files examples
%doc doc website

%changelog
