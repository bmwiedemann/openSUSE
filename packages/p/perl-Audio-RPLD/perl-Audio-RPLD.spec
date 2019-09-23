#
# spec file for package perl-Audio-RPLD
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


%define src_name libaudio-rpld-perl
%define src_ver 0.1beta6
Name:           perl-Audio-RPLD
Version:        0.007_0.1beta6
Release:        0
Summary:        Module to control the RoarAudio PlayList Daemon (rpld)
License:        GPL-3.0
Group:          Development/Libraries/Perl
Url:            http://roaraudio.keep-cool.org
Source:         http://roaraudio.keep-cool.org/dl/%{src_name}-%{src_ver}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(inc::Module::Install)
Recommends:     roarpld
BuildArch:      noarch
%{perl_requires}

%description
Audio::RPLD is a Perl module to access the RoarAudio PlayList Daemon from
within any Perl application.
It supports most commands supported by the rpld.
This included commands to control playback, the Main Queue, playlists
and pointer mangement.

%prep
%setup -q -n %{src_name}-%{src_ver}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc AUTHORS ChangeLog COPYING.gplv3 README TODO

%changelog
