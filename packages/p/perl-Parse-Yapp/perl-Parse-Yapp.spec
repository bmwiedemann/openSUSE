#
# spec file for package perl-Parse-Yapp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Parse-Yapp
Version:        1.21
Release:        0
#Upstream:  The Parse::Yapp module and its related modules and shell scripts are You may use and distribute them under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file. If you use the "standalone parser" option so people don't need to install
%define cpan_name Parse-Yapp
Summary:        Perl extension for generating and using LALR parsers
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Parse-Yapp/
Source0:        https://cpan.metacpan.org/authors/id/W/WB/WBRASWELL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Parse::Yapp (Yet Another Perl Parser compiler) is a collection of modules
that let you generate and use yacc like thread safe (reentrant) parsers
with perl object oriented interface.

The script yapp is a front-end to the Parse::Yapp module and let you easily
create a Perl OO parser from an input grammar file.

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
%doc Calc.yp Changes docs README README.md yapp YappParse.yp

%changelog
