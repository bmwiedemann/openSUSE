#
# spec file for package perl-Gnome2-Canvas
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Sascha Manns <saigkill@opensuse.org>
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


Name:           perl-Gnome2-Canvas
Version:        1.002
Release:        0
Summary:        Gnome2-Canvas Perl module
License:        LGPL-2.0+ and GPL-2.0+
Group:          Development/Languages/Perl
Url:            http://search.cpan.org/dist/Gnome2-Canvas/
Source0:        Gnome2-Canvas-%{version}.tar.gz
BuildRequires:  libgnomecanvas-devel
BuildRequires:  perl
BuildRequires:  perl-ExtUtils-Depends
BuildRequires:  perl-ExtUtils-PkgConfig
BuildRequires:  perl-Glib
BuildRequires:  perl-Gtk2
%if 0%{?suse_version} && 0%{?suse_version} < 1140
BuildRequires:  perl-macros
%endif
Requires:       libgnomecanvas >= %(pkg-config --modversion libgnomecanvas-2.0)     
Requires:       perl-Glib
Requires:       perl-Gtk2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description
The Gnome2::Canvas module allows a perl developer to use the GnomeCanvas
widget with Gtk2-Perl.  Find out more about Gnome+ at http://www.gnome.org.

Like the Gtk2 module on which it depends, Gnome2::Canvas follows the C API
of libgnomecanvas-2.0 as closely as possible while still being perlish.
Thus, the C API reference remains the canonical documentation.

To discuss gtk2-perl, ask questions and flame/praise the authors,
join gtk-perl-list@gnome.org at lists.gnome.org.

Also have a look at the gtk2-perl website and sourceforge project page,
http://gtk2-perl.sourceforge.net

%prep
%setup -q -n Gnome2-Canvas-%{version}

%build
perl Makefile.PL
make

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,-)
%dir %{perl_vendorarch}/Gnome2
%dir %{perl_vendorarch}/Gnome2/Canvas
%dir %{perl_vendorarch}/Gnome2/Canvas/Install
%dir %{perl_vendorarch}/auto/Gnome2
%dir %{perl_vendorarch}/auto/Gnome2/Canvas

%changelog
