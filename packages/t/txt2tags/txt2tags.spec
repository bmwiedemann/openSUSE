#
# spec file for package txt2tags
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Christoph Junghans <junghans@votca.org>
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


Name:           txt2tags
Version:        2.6
Release:        0
Summary:        Converts text files to HTML, XHTML, sgml, LaTeX, man and others
License:        GPL-2.0
Group:          Productivity/Text/Convertors
Url:            http://txt2tags.sourceforge.net
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM https://github.com/txt2tags/txt2tags/commit/49b0808
Patch0:         reproducible.patch
Requires:       python
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Txt2tags is a generic text converter. From a simple text file with minimal
markup, it generates documents on the following formats: HTML, XHTML, sgml,
LaTeX, Lout, man, Magic Point (mgp), MoinMoin and Adobe PageMaker. Supports
heading, font beautifiers, verbatim, quote, link, lists, table and image.
There are GUI, Web and cmdline interfaces. It's a single Python script and
no external commands or libraries are needed.
 
%prep
%setup -q
%patch0 -p1

%build
# compile the translated messages for all languages
%define LANGS $(cd po; ls *.po | cut -d. -f1)
for lang in %{LANGS}; do
        msgfmt -o po/$lang.mo po/$lang.po
done

%install
#chmod 744 extras/*

# executables
install -d %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

# man pages
install -d %{buildroot}/%{_mandir}/man1
install -m 0644 doc/manpage.man %{buildroot}/%{_mandir}/man1/txt2tags.1
rm doc/manpage.man

cd doc
for lang in $(ls -p1 | grep / | cut -d/ -f1); do
  if [ ! -z $(ls $lang | grep .man) ]; then
    install -d %{buildroot}/%{_mandir}/$lang/man1
    install -m 0644 $lang/$(ls $lang | grep .man) %{buildroot}/%{_mandir}/$lang/man1/txt2tags.1
    rm $lang/$(ls $lang | grep .man)
  fi
done
cd ..

# translations
for lang in %{LANGS}; do
        install -d \
                %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
        install -m 0644 po/$lang.mo \
                %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/txt2tags.mo
done

%files
%defattr(-,root,root,0755)
%doc ChangeLog README COPYING
%doc doc/ extras/ samples/
%{_bindir}/%{name}
%{_mandir}/man1/txt2tags.1*
#%{_mandir}/*/man1/txt2tags.1*
%{_datadir}/locale/*/LC_MESSAGES/txt2tags.mo

%changelog
