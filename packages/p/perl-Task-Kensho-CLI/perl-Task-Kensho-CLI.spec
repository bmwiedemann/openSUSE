#
# spec file for package perl-Task-Kensho-CLI
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Task-Kensho-CLI
Version:        0.40
Release:        0
%define cpan_name Task-Kensho-CLI
Summary:        Glimpse at an Enlightened Perl: Useful Command-line Tools
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Ack)
BuildRequires:  perl(App::Nopaste)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl(Reply)
Requires:       perl(App::Ack)
Requires:       perl(App::Nopaste)
Requires:       perl(Module::CoreList)
Requires:       perl(Reply)
%{perl_requires}

%description
From http://en.wikipedia.org/wiki/Kensho:

    Kenshō (見性) (C. Wu) is a Japanese term for enlightenment experiences -
    most commonly used within the confines of Zen Buddhism - literally
    meaning "seeing one's nature"[1] or "true self."[2] It generally
    "refers to the realization of nonduality of subject and object."[3]

Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

The plan is for Task::Kensho to be a rough testing ground for ideas that go
into among other things the Enlightened Perl Organisation Extended Core
(EPO-EC).

The modules that are bundled by Task::Kensho are broken down into several
categories and are still being considered. They are all taken from various
top 100 most used perl modules lists and from discussions with various
subject matter experts in the Perl Community. That said, this bundle does
_not_ follow the guidelines established for the EPO-EC for peer review via
industry advisers.

Starting in 2011, Task::Kensho split its sub-groups of modules into
individually-installable tasks. Each Task::Kensho sub-task is listed at the
beginning of its section in this documentation.

When installing Task::Kensho itself, you will be asked to install each
sub-task in turn, or you can install individual tasks separately. These
individual tasks will always install all their modules by default. This
facilitates the ease and simplicity the distribution aims to achieve.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENCE

%changelog
