#
# spec file for package efont-unicode-bitmap-fonts
#
# Copyright (c) 2019 SUSE LLC
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


Name:           efont-unicode-bitmap-fonts
Version:        0.4.2
Release:        0
%define	_miscfontsdir     /usr/share/fonts/misc
Summary:        Unicode Font by /efont/
License:        SUSE-Public-Domain AND BSD-3-Clause
Group:          System/X11/Fonts
URL:            http://openlab.ring.gr.jp/efont/
Source0:        http://openlab.ring.gr.jp/efont/dist/unicode-bdf/efont-unicode-bdf-0.4.2-src.tar.bz2
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         baseline-offset.diff
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         bugzilla-199997-some-glyphs-for-yast.patch
# PATCH-FIX-UPSTREAM -- ToDo
Patch2:         reproducible.patch
# PATCH-FIX-OPENSUSE
Patch3:         remove_deprecated_one_based_array_index.diff
BuildRequires:  bdfresize
BuildRequires:  bdftopcf
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Requires(post):      mkfontdir
Requires(postun):    mkfontdir
Requires(posttrans): mkfontdir
Provides:       efont-unicode = %{version}
Obsoletes:      efont-unicode <= 0.4.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Unicode fonts developed by /efont/ openlab. This font package includes
12,14, 16, and 24 pixel ISO-10646 fonts.

%prep
%setup -q -n efont-unicode-bdf-0.4.2-src
%patch -P 0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
iconv -f ISO-8859-1 -t UTF-8 < README.etl-unicode > README.etl-unicode.tmp
mv README.etl-unicode.tmp README.etl-unicode
for i in README.shinonome README.naga10
do
    iconv -f EUC-JP -t UTF-8 < $i > $i.tmp
    mv $i.tmp $i
done
./configure --with-_miscfontsdir=%{_miscfontsdir}

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_miscfontsdir}
install -m 444 *.pcf.gz %{buildroot}%{_miscfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%license COPYRIGHT
%doc README* ChangeLog
%dir %{_miscfontsdir}/
%{_miscfontsdir}/*.pcf.gz

%changelog
