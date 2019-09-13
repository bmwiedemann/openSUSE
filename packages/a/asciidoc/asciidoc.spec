#
# spec file for package asciidoc
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


Name:           asciidoc
Version:        8.6.10
Release:        0
Summary:        Text-Based Document Generation
License:        GPL-2.0+
Group:          Development/Tools/Doc Generators
Url:            http://asciidoc.org
Source0:        https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         asciidoc.version.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  python2 >= 2.3
BuildRequires:  python2-xml
Requires:       docbook-xsl-stylesheets
Requires:       python2 >= 2.3
Requires:       python2-xml
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
Group:          Development/Tools/Doc Generators

%description examples
This package contains examples and documents of asciidoc.

%prep
%setup -q
%patch0 -p1

%build
sed -i "s|python|python2|g" Makefile.in
autoreconf -fi
%configure

%install
%make_install

# Strip .py extension from binaries
pushd %{buildroot}%{_bindir}
	mv %{name}.py %{name}
	mv a2x.py a2x
popd

# install vim files
mkdir -p %{buildroot}%{_datadir}/vim/site/{syntax,ftdetect}
install -m 0644 vim/syntax/* %{buildroot}%{_datadir}/vim/site/syntax

%files
%config %{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/a2x
%{_datadir}/vim
%{_mandir}/man1/*
%doc README.asciidoc BUGS.txt CHANGELOG.txt COPYRIGHT

%files examples
%doc doc examples

%changelog
