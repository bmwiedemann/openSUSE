#
# spec file for package perl-Tie-RefHash-Weak
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


Name:           perl-Tie-RefHash-Weak
Version:        0.09
Release:        0
%define cpan_name Tie-RefHash-Weak
Summary:        A Tie::RefHash subclass with weakened references in the keys.
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Tie-RefHash-Weak/
Source:         http://www.cpan.org/authors/id/N/NU/NUFFIN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Variable::Magic)
Requires:       perl(Task::Weaken)
Requires:       perl(Variable::Magic)
%{perl_requires}

%description
The the Tie::RefHash manpage module can be used to access hashes by
reference. This is useful when you index by object, for example.

The problem with the Tie::RefHash manpage, and cross indexing, is that
sometimes the index should not contain strong references to the objecs. the
Tie::RefHash manpage's internal structures contain strong references to the
key, and provide no convenient means to make those references weak.

This subclass of the Tie::RefHash manpage has weak keys, instead of strong
ones. The values are left unaltered, and you'll have to make sure there are
no strong references there yourself.

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
%doc Changes TODO

%changelog
