#
# spec file for package perl-HTML-Stream
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


Name:           perl-HTML-Stream
Version:        1.60
Release:        0
%define cpan_name HTML-Stream
Summary:        HTML output stream class, and some markup utilities
License:        GPL-1.0+ OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Stream/
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSTAAL/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The *HTML::Stream* module provides you with an object-oriented (and
subclassable) way of outputting HTML. Basically, you open up an "HTML
stream" on an existing filehandle, and then do all of your output to the
HTML stream. You can intermix HTML-stream-output and ordinary-print-output,
if you like.

There's even a small built-in subclass, *HTML::Stream::Latin1*, which can
handle Latin-1 input right out of the box. But all in good time...

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes docs examples README README.system
%license COPYING

%changelog
