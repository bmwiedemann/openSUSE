#
# spec file for package perl-XML-Filter-BufferText
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-XML-Filter-BufferText
Version:        1.01
Release:        0
%define cpan_name XML-Filter-BufferText
Summary:        Filter to put all characters() in one event
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-Filter-BufferText/
Source:         http://www.cpan.org/authors/id/R/RB/RBERJON/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::SAX) >= 0.04
BuildRequires:  perl(XML::SAX::Base) >= 1.03
Requires:       perl(XML::SAX) >= 0.04
Requires:       perl(XML::SAX::Base) >= 1.03
%{perl_requires}

%description
This is a very simple filter. One common cause of grief (and programmer
error) is that XML parsers aren't required to provide character events in
one chunk. They can, but are not forced to, and most don't. This filter
does the trivial but oft-repeated task of putting all characters into a
single event.

Note that this won't help you cases such as:

  <foo> blah <!-- comment --> phubar </foo>

In the above case, given the interleaving comment, there will be two
'character()' events. This may be worked around in the future if there is
demand for it.

An interesting way to use this filter, instead of telling users to use it,
is to return it from your handler's constructor, already configured and
all. That'll make the buffering totally transparent to them
('XML::SAX::Writer' does that).

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
