#
# spec file for package perl-File-Rsync
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-File-Rsync
Version:        0.49
Release:        0
%define cpan_name File-Rsync
Summary:        Perl Module Interface to Rsync(1) F<Http://Rsync.Samba.Org/Rsync/>
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Rsync/
Source0:        http://www.cpan.org/authors/id/L/LE/LEAKIN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Run3)
Requires:       perl(IPC::Run3)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  rsync
Requires:       rsync
# MANUAL END

%description
Perl Convenience wrapper for the rsync(1) program. Written for
_rsync-2.3.2_ and updated for _rsync-3.1.1_ but should perform properly
with most recent versions.

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
%doc Changelog README TODO

%changelog
