#
# spec file for package libquvi-scripts
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libquvi-scripts
Version:        0.9.20131130
Release:        0
Summary:        Lua scripts used by libquvi
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Other
Url:            http://quvi.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/quvi/0.9/libquvi-scripts/libquvi-scripts-%{version}.tar.xz
# For pkgconfig() Provides
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1320
# Package was renamed and provided for multiple lua versions after Leap 42.3
# Require the lua-version that libquvi links
Requires:       lua53-luasocket
%else
Requires:       luasocket
%endif

%description
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%package devel
Summary:        Lua scripts used by libquvi -- Development Files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
libquvi-scripts contains the embedded lua scripts that libquvi uses for
parsing the media details. Some additional utility scripts are also
included.

%package nsfw
Summary:        Not Safe For Work Lua scripts used by libquvi
Group:          Productivity/Multimedia/Other
Requires:       %{name} = %{version}

%description nsfw
Website fetching scripts used by %{name} that are marked as "NSFW"
(Not Safe For Work).

%prep
%setup -q

%build
%configure \
    --with-nsfw

make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

EXCL="$PWD/exclude.lst"
NSFW="$PWD/nsfw.lst"
echo -n >"$EXCL"
echo -n >"$NSFW"
perl -n -e 'print $1,"\n" if /^if WITH_NSFW/ .. /endif/ and m,\b(lua/website/.+\.lua),' share/Makefile.am | while read f; do
    echo "%exclude %{_datadir}/libquvi-scripts/$f" >>"$EXCL"
    echo "%{_datadir}/libquvi-scripts/$f" >>"$NSFW"
done

%files -f exclude.lst
%doc AUTHORS ChangeLog COPYING NEWS README
%{_datadir}/libquvi-scripts/
%{_mandir}/man7/libquvi-scripts.7%{?ext_man}
%{_mandir}/man7/quvi-modules-3rdparty.7%{?ext_man}
%{_mandir}/man7/quvi-modules.7%{?ext_man}

%files nsfw -f nsfw.lst
%dir %{_datadir}/libquvi-scripts/

%files devel
%{_libdir}/pkgconfig/libquvi-scripts-0.9.pc

%changelog
