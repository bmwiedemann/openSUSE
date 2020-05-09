#
# spec file for package help2man
#
# Copyright (c) 2020 SUSE LLC
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


Name:           help2man
Version:        1.47.15
Release:        0
Summary:        Script for generating man pages from --help output
License:        GPL-3.0-or-later
Group:          Development/Tools/Doc Generators
URL:            https://www.gnu.org/software/help2man/
Source0:        https://ftp.gnu.org/gnu/help2man/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/help2man/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
BuildRequires:  perl-gettext
Requires:       perl-gettext
Requires(post): info
Requires(preun): info
Recommends:     %{name}-lang

%description
help2man is a script to create simple man pages from the --help and
--version output of programs.

Since most GNU documentation is now in info format, this provides a way
to generate a placeholder man page pointing to that resource while
still providing some useful information.

%lang_package

%prep
%setup -q

%build
%configure \
	--enable-nls
%make_build

%install
%make_install

%find_lang %{name} --with-man

%post
%install_info --info-dir=%{_infodir} %{_infodir}/help2man.info%{ext_info}

%post -n %{name}-lang
%install_info --info-dir=%{_infodir} %{_infodir}/help2man.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/help2man.info%{ext_info}

%preun -n %{name}-lang
%install_info_delete --info-dir=%{_infodir} %{_infodir}/help2man.info%{ext_info}

%files
%license COPYING
%doc NEWS README THANKS debian/changelog
%{_bindir}/help2man
%{_libdir}/help2man/
%{_infodir}/help2man.info%{?ext_info}
%{_mandir}/man1/help2man.1%{?ext_man}

%files lang -f %{name}.lang
%{_infodir}/help2man-*.info%{?ext_info}
%dir %{_mandir}/??
%dir %{_mandir}/??/man1

%changelog
