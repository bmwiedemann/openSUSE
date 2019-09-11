#
# spec file for package perl-File-MMagic
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-File-MMagic
Version:        1.30
Release:        0
%define cpan_name File-MMagic
Summary:        Guess file type
License:        Apache-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-MMagic/
Source:         http://www.cpan.org/authors/id/K/KN/KNOK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(File::MMagic)
#BuildRequires: perl(Module::Build)
%{perl_requires}

%description
checktype_filename(), checktype_filehandle() and checktype_contents returns
string contains file type with MIME mediatype format.

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
%doc ChangeLog COPYING README.en README.ja

%changelog
