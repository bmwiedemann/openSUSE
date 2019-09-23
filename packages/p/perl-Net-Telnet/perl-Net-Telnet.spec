#
# spec file for package perl-Net-Telnet
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


Name:           perl-Net-Telnet
Version:        3.04
Release:        0
%define cpan_name Net-Telnet
Summary:        interact with TELNET port or other TCP ports
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-Telnet/
Source:         http://www.cpan.org/authors/id/J/JR/JROGERS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Net::Telnet allows you to make client connections to a TCP port and do
network I/O, especially to a port using the TELNET protocol. Simple I/O
methods such as print, get, and getline are provided. More sophisticated
interactive features are provided because connecting to a TELNET port
ultimately means communicating with a program designed for human
interaction. These interactive features include the ability to specify a
time-out and to wait for patterns to appear in the input stream, such as
the prompt from a shell. IPv6 support is available when using perl 5.14 or
later (see 'family()'.

Other reasons to use this module than strictly with a TELNET port are:

* *

  You're not familiar with sockets and you want a simple way to make client
  connections to TCP services.

* *

  You want to be able to specify your own time-out while connecting,
  reading, or writing.

* *

  You're communicating with an interactive program at the other end of some
  socket or pipe and you want to wait for certain patterns to appear.

Here's an example that prints who's logged-on to a remote host. In addition
to a username and password, you must also know the user's shell prompt,
which for this example is '"bash$ "'

    use Net::Telnet ();
    $t = new Net::Telnet (Timeout => 10,
                          Prompt => '/bash\$ $/');
    $t->open($host);
    $t->login($username, $passwd);
    @lines = $t->cmd("who");
    print @lines;

See the *EXAMPLES* section below for more examples.

Usage questions should be directed to the perlmonks.org discussion group.
Bugs can be viewed or reported at cpan.org on the Net::Telnet page.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc ChangeLog README

%changelog
