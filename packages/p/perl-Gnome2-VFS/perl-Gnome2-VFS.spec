#
# spec file for package perl-Gnome2-VFS
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name Gnome2-VFS
Name:           perl-Gnome2-VFS
Version:        1.083
Release:        0
Summary:        Perl interface to the 2.x series of the GNOME VFS library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/Gnome2-VFS
Source:         https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  pkgconfig
BuildRequires:  perl(ExtUtils::Depends) >= 0.20
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:  perl(Glib) >= 1.120
BuildRequires:  pkgconfig(gnome-vfs-2.0)
Requires:       gnome-vfs2 >= %(pkg-config --modversion gnome-vfs-2.0)
#BuildRequires: perl(Glib::Object::Subclass)
#BuildRequires: perl(Gnome2::VFS)
#BuildRequires: perl(Gtk2)
Requires:       perl(ExtUtils::Depends) >= 0.20
Requires:       perl(ExtUtils::PkgConfig) >= 1.03
Requires:       perl(Glib) >= 1.120
%{perl_requires}

%description
Since this module tries to stick very closely to the C API, the
documentation found at

  L<http://developer.gnome.org/doc/API/2.0/gnome-vfs-2.0/>

is the canonical reference.

In addition to that, there's also the automatically generated API
documentation: the Gnome2::VFS::index manpage.

The mapping described in the Gtk2::api manpage also applies to this module.

To discuss this module, ask questions and flame/praise the authors, join
gtk-perl-list@gnome.org at lists.gnome.org.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%license LICENSE
%doc ChangeLog.pre-git doctypes examples maps-2.0 maps-2.6 maps-2.8 NEWS perl-Gnome2-VFS.doap README vfs.typemap xs_files-2.0 xs_files-2.6 xs_files-2.8

%changelog
