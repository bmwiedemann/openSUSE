#
# spec file for package perl-File-Find-Rule
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


Name:           perl-File-Find-Rule
Version:        0.34
Release:        0
%define cpan_name File-Find-Rule
Summary:        Alternative interface to File::Find
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Find-Rule/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Number::Compare)
BuildRequires:  perl(Text::Glob) >= 0.07
Requires:       perl(Number::Compare)
Requires:       perl(Text::Glob) >= 0.07
%{perl_requires}

%description
File::Find::Rule is a friendlier interface to File::Find. It allows you to
build rules which specify the desired files and directories.

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
%doc Changes findrule

%changelog
