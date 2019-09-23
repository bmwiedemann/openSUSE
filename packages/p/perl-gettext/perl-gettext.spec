#
# spec file for package perl-gettext
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


Name:           perl-gettext
Version:        1.07
Release:        0
%define cpan_name gettext
Summary:        Message Handling Functions
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/gettext/
Source0:        http://www.cpan.org/authors/id/P/PV/PVANDRY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The gettext module permits access from perl to the gettext() family of
functions for retrieving message strings from databases constructed to
internationalize software.

* $d = Locale::gettext->domain(DOMAIN)

* $d = Locale::gettext->domain_raw(DOMAIN)

  Creates a new object for retrieving strings in the domain *DOMAIN* and
  returns it. 'domain' requests that strings be returned as Perl strings
  (possibly with wide characters) if possible while 'domain_raw' requests
  that octet strings directly from functions like 'dgettext()'.

* $d->get(MSGID)

  Calls 'dgettext()' to return the translated string for the given *MSGID*.

* $d->cget(MSGID, CATEGORY)

  Calls 'dcgettext()' to return the translated string for the given *MSGID*
  in the given *CATEGORY*.

* $d->nget(MSGID, MSGID_PLURAL, N)

  Calls 'dngettext()' to return the translated string for the given *MSGID*
  or *MSGID_PLURAL* depending on *N*.

* $d->ncget(MSGID, MSGID_PLURAL, N, CATEGORY)

  Calls 'dngettext()' to return the translated string for the given *MSGID*
  or *MSGID_PLURAL* depending on *N* in the given *CATEGORY*.

* $d->dir([NEWDIR])

  If *NEWDIR* is given, calls 'bindtextdomain' to set the name of the
  directory where messages for the domain represented by '$d' are found.
  Returns the (possibly changed) current directory name.

* $d->codeset([NEWCODE])

  For instances created with 'Locale::gettext->domain_raw', manuiplates the
  character set of the returned strings. If *NEWCODE* is given, calls
  'bind_textdomain_codeset' to set the character encoding in which messages
  for the domain represented by '$d' are returned. Returns the (possibly
  changed) current encoding name.

gettext(), dgettext(), and dcgettext() attempt to retrieve a string
matching their 'msgid' parameter within the context of the current locale.
dcgettext() takes the message's category and the text domain as parameters
while dgettext() defaults to the LC_MESSAGES category and gettext()
defaults to LC_MESSAGES and uses the current text domain. If the string is
not found in the database, then 'msgid' is returned.

ngettext(), dngettext(), and dcngettext() function similarily but implement
differentiation of messages between singular and plural. See the
documentation for the corresponding C functions for details.

textdomain() sets the current text domain and returns the previously active
domain.

_bindtextdomain(domain, dirname)_ instructs the retrieval functions to look
for the databases belonging to domain 'domain' in the directory 'dirname'

_bind_textdomain_codeset(domain, codeset)_ instructs the retrieval
functions to translate the returned messages to the character encoding
given by *codeset* if the encoding of the message catalog is known.

%prep
%setup -q -n Locale-%{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc README

%changelog
