#
# spec file for package perl-FindBin-Real
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



Name:           perl-FindBin-Real
Version:        1.05
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name FindBin-Real
Summary:        Locate directory of original perl script
Url:            http://search.cpan.org/dist/FindBin-Real/
Group:          Development/Libraries/Perl
#Source:         http://www.cpan.org/authors/id/S/ST/STRO/FindBin-Real-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
Locates the full path to the script bin directory to allow the use of paths
relative to the bin directory.

This allows a user to setup a directory tree for some software with
directories <root>/bin and <root>/lib and then the above example will allow
the use of modules in the lib directory without knowing where the software
tree is installed.

If perl is invoked using the *-e* option or the perl script is read from
'STDIN' then FindBin sets both 'Bin()' and 'RealBin()' return values to the
current directory.

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
%doc CHANGES README

%changelog
