#
# spec file for package perl-XML-NamespaceFactory
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-XML-NamespaceFactory
Version:        1.02
Release:        0
%define cpan_name XML-NamespaceFactory
Summary:        Simple factory objects for SAX namespaced names.
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-NamespaceFactory/
Source:         http://www.cpan.org/authors/id/P/PE/PERIGRIN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Simply create a new XML::NamespaceFactory object with the namespace you
wish to use as its single parameter. If you wish to use the empty
namespace, simply pass in an empty string (but undef will not do).

Then, when you want to get a JClark name, call a method on that object the
name of which is the local name you wish to have. It'll return the JClark
notation for that local name in your namespace.

Unfortunately, some local names legal in XML are not legal in Perl. To
circumvent this, you can use the hash notation in which you access a key on
the object the name of which is the local name you wish to have. This will
work just as the method call name but will accept more characters. Note
that it does not check that the name you ask for is a valid XML name. This
form is more general but slower.

If this is not clear, hopefully the SYNOPSIS should help :)

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes cpanfile LICENSE README

%changelog
