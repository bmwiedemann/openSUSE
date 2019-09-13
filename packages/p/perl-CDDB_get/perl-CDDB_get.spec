#
# spec file for package perl-CDDB_get
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


Name:           perl-CDDB_get
Version:        2.28
Release:        0
#Upstream:  This library is released under the same conditions as Perl, that is, either of the following: a) the GNU General Public License Version 2 as published by the Free Software Foundation, b) the Artistic License. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See either the GNU General Public License or the Artistic License for more details. You should have received a copy of the Artistic License with this Kit, in the file named "Artistic". If not, I'll be glad to provide one. You should also have received a copy of the GNU General Public License along with this program, in the file names "Copying"; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA. If you use this library in a commercial enterprise, you are invited, but not required, to pay what you feel is a reasonable fee to the author, who can be contacted at armin@xos.net
%define cpan_name CDDB_get
Summary:        Read the CDDB entry for an audio CD in your drive
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CDDB_get/
Source0:        http://www.cpan.org/authors/id/F/FO/FONKIE/%{cpan_name}-%{version}.tar.gz
Source1:        cddb.pl.1.gz
Source2:        cpanspec.yml
Patch0:         %name-2.23-tmpfile.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module/script gets the CDDB info for an audio cd. You need LINUX,
SUNOS or *BSD, a cdrom drive and an active internet connection in order to
do that.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

# MANUAL BEGIN
install -d -m755  $RPM_BUILD_ROOT/%{_mandir}/man1
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/%{_mandir}/man1
# MANUAL END
%files -f %{name}.files
%defattr(-,root,root,755)
%doc Artistic Changes Copying DATABASE README

%changelog
