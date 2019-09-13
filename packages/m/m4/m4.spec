#
# spec file for package m4
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


Name:           m4
Version:        1.4.18
Release:        0
Summary:        GNU m4
License:        GPL-3.0-or-later
Group:          Development/Languages/Other
Url:            https://www.gnu.org/software/m4/
Source0:        https://ftp.gnu.org/pub/gnu/m4/%{name}-%{version}.tar.xz
Source1:        https://ftp.gnu.org/pub/gnu/m4/%{name}-%{version}.tar.xz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=m4&download=1#/%{name}.keyring
Patch1:         gnulib-libio.patch
BuildRequires:  xz
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Provides:       base:%{_bindir}/m4

%description
GNU m4 is an implementation of the traditional Unix macro processor.

%prep
%setup -q
%patch1 -p1

%build
%configure \
  --without-included-regex \
%if 0%{?mageia}
	--disable-dependency-tracking \
%endif
	gl_cv_func_isnanl_works=yes \
	gl_cv_func_printf_directive_n=yes \
	gl_cv_func_printf_infinite_long_double=yes
make %{?_smp_mflags} V=1

%check
make %{?_smp_mflags} check

%install
%make_install
# info's dir file is not auto ignored on some systems
rm -rf %{buildroot}%{_infodir}/dir

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%defattr(-,root,root)
%doc README NEWS THANKS TODO ChangeLog
%license COPYING
%{_bindir}/m4
%{_infodir}/m4.info-1%{ext_info}
%{_infodir}/m4.info-2%{ext_info}
%{_infodir}/m4.info%{ext_info}
%{_mandir}/man1/m4.1%{ext_man}

%changelog
