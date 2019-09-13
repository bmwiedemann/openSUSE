#
# spec file for package perl-HTTP-Thin
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-HTTP-Thin
Version:        0.006
Release:        0
%define cpan_name HTTP-Thin
Summary:        A Thin Wrapper around HTTP::Tiny to play nice with HTTP::Message
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTTP-Thin/
Source:         HTTP-Thin-0.006.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Hash::MultiValue)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(parent)
#BuildRequires: perl(HTTP::Request::Common)
#BuildRequires: perl(HTTP::Thin)
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(HTTP::Response)
Requires:       perl(HTTP::Tiny)
Requires:       perl(Hash::MultiValue)
Requires:       perl(Safe::Isa)
Requires:       perl(parent)
%{perl_requires}

%description
WARNING: This module is untested beyond the very basics. The implementation
is simple enough that it shouldn't do evil things but, yeah it's still not
approved for use by small children.

'HTTP::Thin' is a thin wrapper around the HTTP::Tiny manpage adding the
ability to pass in the HTTP::Request manpage objects and get back the
HTTP::Response manpage objects. The maintainers of the HTTP::Tiny manpage,
justifiably, don't want to have to maintain compatibility but many other
projects already consume the the HTTP::Message manpage objects. This is
just glue code doing what it does best.

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
%doc CHANGES LICENSE README weaver.ini

%changelog
