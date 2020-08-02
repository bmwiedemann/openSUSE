#
# spec file for package perl-CLASS
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



Name:           perl-CLASS
Version:        1.00
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name CLASS
Summary:        Alias for __PACKAGE__
Url:            http://search.cpan.org/dist/CLASS/
Group:          Development/Libraries/Perl
#Source:         http://www.cpan.org/authors/id/M/MS/MSCHWERN/CLASS-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
CLASS and $CLASS are both synonyms for __PACKAGE__. Easier to type.

$CLASS has the additional benefit of working in strings.

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
%defattr(644,root,root,755)
%doc Changes

%changelog
