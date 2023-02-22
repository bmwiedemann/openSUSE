#
# spec file for package autoconf-archive
#
# Copyright (c) 2023 SUSE LLC
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


Name:           autoconf-archive
Version:        2023.02.20
Release:        0
Summary:        A Collection of macros for GNU autoconf
License:        GPL-3.0-or-later WITH Autoconf-exception-3.0
URL:            https://savannah.gnu.org/projects/autoconf-archive
Source0:        https://ftp.gnu.org/pub/gnu/autoconf-archive/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/pub/gnu/autoconf-archive/%{name}-%{version}.tar.xz.sig
# http://wwwkeys.pgp.net:11371/pks/lookup?op=get&search=0x99089D72
Source2:        %{name}.keyring
BuildArch:      noarch

%description
The GNU Autoconf Archive is a collection of more than 450 macros for `GNU
Autoconf <http://www.gnu.org/software/autoconf>`_ that have been contributed as
free software by friendly supporters of the cause from all over the Internet.
Every single one of those macros can be re-used without imposing any
restrictions whatsoever on the licensing of the generated `configure` script. In
particular, it is possible to use all those macros in `configure` scripts that
are meant for non-free software. This policy is unusual for a Free Software
Foundation project. The FSF firmly believes that software ought to be free, and
software licenses like the GPL are specifically designed to ensure that
derivative work based on free software must be free as well. In case of
Autoconf, however, an exception has been made, because Autoconf is at such a
pivotal position in the software development tool chain that the benefits from
having this tool available as widely as possible outweigh the disadvantage that
some authors may choose to use it, too, for proprietary software.

%prep
%setup -q

%build
%configure \
	--docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/%{name}/
# install via macro later
rm -v %{buildroot}%{_docdir}/%{name}/COPYING*

%files
%license COPYING*
%doc AUTHORS README
%{_infodir}/%{name}.info*%{ext_info}
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/*.m4

%changelog
