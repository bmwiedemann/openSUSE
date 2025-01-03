#
# spec file for package dico
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define         sover 2
%define         lib_name lib%{name}%{sover}
Name:           dico
Version:        2.12
Release:        0
Summary:        Flexible modular implementation of DICT server (RFC 2229)
License:        GPL-3.0-or-later
Group:          Productivity/Office/Dictionary
URL:            https://www.gnu.org/software/dico/
Source0:        https://ftp.gnu.org/gnu/dico/dico-%{version}.tar.xz
# not updated on savannah
# Source1:        https://ftp.gnu.org/gnu/dico/dico-%%{version}.tar.xz.sig
# https://www.gnu.org.ua/software/dico/download.html
# Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=311#/%%{name}.keyring
BuildRequires:  groff
BuildRequires:  guile-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  wordnet-devel
BuildRequires:  pkgconfig(libgsasl)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(zlib)
Requires:       m4
Recommends:     %{name}-modules
%lang_package

%description
GNU Dico is a flexible modular implementation of DICT server (RFC 2229). In
contrast to another implementations, it does not depend on particular
database format. GNU Dico handles database accesses using loadable modules.

%package devel
Summary:        Development files to build modules for %{name}
Group:          Development/Libraries/Other
Requires:       %{lib_name} = %{version}

%description devel
GNU Dico is a flexible modular implementation of DICT server (RFC 2229). In
contrast to another implementations, it does not depend on particular
database format. GNU Dico handles database accesses using loadable modules.

This package contains the development headers for developing modules for
%{name}.

%package -n %{lib_name}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{lib_name}
GNU Dico is a flexible modular implementation of DICT server (RFC 2229). In
contrast to another implementations, it does not depend on particular
database format. GNU Dico handles database accesses using loadable modules.

This package contains shared library for %{name}.

%package modules
Summary:        Modules for %{name}
Group:          Productivity/Office/Dictionary
Requires:       %{name} = %{version}

%description modules
GNU Dico is a flexible modular implementation of DICT server (RFC 2229). In
contrast to another implementations, it does not depend on particular
database format. GNU Dico handles database accesses using loadable modules.

This package contains extensions and modules for %{name}.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fcommon"
%configure \
  PYTHON=%{_bindir}/python3 \
  PYTHON_CONFIG=%{_bindir}/python3-config \
  DEFAULT_DICT_SERVER=dict.org \
  --libexecdir=%{_bindir} \
  --enable-static=no
%make_build

%install
%make_install
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
%find_lang %{name}

%ldconfig_scriptlets -n %{lib_name}

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/dico
%{_bindir}/dicod
%{_bindir}/gcider
%{_bindir}/idxgcide
%dir %{_libdir}/%{name}
%dir %{_datadir}/dico/
%dir %{_datadir}/dico/%{version}
%dir %{_datadir}/dico/%{version}/include
%{_datadir}/dico/%{version}/include/pp-setup
%{_infodir}/dico.info%{?ext_info}
%{_mandir}/man1/dico.1%{?ext_man}
%{_mandir}/man5/dicod.conf.5%{?ext_man}
%{_mandir}/man8/dicod.8%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%files -n %{lib_name}
%license COPYING
%{_libdir}/libdico.so.%{sover}*

%files devel
%license COPYING
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libdico.so

%files modules
%license COPYING
%{_libdir}/%{name}/*.so

%changelog
