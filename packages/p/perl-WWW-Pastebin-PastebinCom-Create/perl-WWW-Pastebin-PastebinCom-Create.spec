#
# spec file for package perl-WWW-Pastebin-PastebinCom-Create
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


Name:           perl-WWW-Pastebin-PastebinCom-Create
Version:        1.003
Release:        0
%define cpan_name WWW-Pastebin-PastebinCom-Create
Summary:        Paste On Www.Pastebin.Com Without Api Keys
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/WWW-Pastebin-PastebinCom-Create/
Source0:        http://www.cpan.org/authors/id/Z/ZO/ZOFFIX/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Moo) >= 1.004001
BuildRequires:  perl(WWW::Mechanize) >= 1.73
Requires:       perl(Moo) >= 1.004001
Requires:       perl(WWW::Mechanize) >= 1.73
%{perl_requires}

%description
This module provides the means to paste on the www.pastebin.com manpage
pastebin, without the need for http://pastebin.com/api. See the WARNING!!!
section above.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
# MANUAL no testing (accesses pastebin)
#./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples LICENSE README

%changelog
