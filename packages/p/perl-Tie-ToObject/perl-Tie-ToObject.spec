#
# spec file for package perl-Tie-ToObject
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Tie-ToObject
Version:        0.03
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Tie-ToObject
Summary:        Tie to an existing object.
Url:            http://search.cpan.org/dist/Tie-ToObject/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/N/NU/NUFFIN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ok)
BuildRequires:  perl(Test::use::ok)
Requires:       perl(Test::use::ok)
%{perl_requires}

%description
While the perldoc/tie manpage allows tying to an arbitrary object, the
class in question must support this in it's implementation of 'TIEHASH',
'TIEARRAY' or whatever.

This class provides a very tie constructor that simply returns the object
it was given as it's first argument.

This way side effects of calling '$object->TIEHASH' are avoided.

This is used in the Data::Visitor manpage in order to tie a variable to an
already existing object. This is also useful for cloning, when you want to
clone the internal state object instead of going through the tie interface
for that variable.

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)

%changelog
