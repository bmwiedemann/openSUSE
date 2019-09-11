#
# spec file for package perl-FreezeThaw (Version 0.5001)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-FreezeThaw
%define cpan_name %( echo %{name} | %{__sed} -e 's,perl-,,' )
Summary:        Converting Perl structures to strings and back
Version:        0.5001
Release:        4
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/FreezeThaw
Source0:        http://search.cpan.org/CPAN/authors/id/I/IL/ILYAZ/modules/FreezeThaw-0.5001.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Converts data to/from stringified form, appropriate for saving-to/reading-from
permanent storage.

Deals with objects, circular lists, repeated appearence of the same refence.
Does not deal with overloaded stringify operator yet.

  Author:	Ilya Zakharevich
%prep
%setup -q -n %{cpan_name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
# normally you only need to check for doc files
%defattr(0644,root,root,0755)
%doc Changes README

%changelog
