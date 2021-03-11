#
# spec file for package units
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_without	units_cur
Name:           units
Version:        2.21
Release:        0
Summary:        Conversion Utility
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://www.gnu.org/software/units/
Source0:        http://ftp.gnu.org/gnu/units/units-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/units/units-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=units&download=1#/units.keyring
BuildRequires:  bison
BuildRequires:  readline-devel
%if 0%{?suse_version} <= 1500
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
%endif
%if %{with units_cur}
BuildRequires:  python3-base
%endif

%description
The 'units' program converts quantities expressed in various scales to
their equivalents in other scales.

Units can also convert temperature values (Fahrenheit to Celsius, for
example) but this needs a slightly different input syntax. See the man
page for details.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure PYTHON=/usr/bin/python3
%make_build

%install
%make_install

%check
%make_build check

%if 0%{?suse_version} <= 1500
%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}
%endif

%files
%license COPYING
%{_bindir}/units
%{_datadir}/units
%dir %{_localstatedir}/lib/units
%{_localstatedir}/lib/units/currency.units
%doc ChangeLog NEWS README
%{_infodir}/units.info%{?ext_info}
%{_mandir}/man1/units.1%{?ext_man}
%if %{with units_cur}
%{_bindir}/units_cur
%endif

%changelog
