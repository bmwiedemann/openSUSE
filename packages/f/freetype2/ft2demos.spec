#
# spec file for package ft2demos
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


%define freetype_version 2.10.4
Name:           ft2demos
Version:        2.10.4
Release:        0
Summary:        Freetype2 Utilities and Demo Programs
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/Other
URL:            https://www.freetype.org
Source0:        https://downloads.sourceforge.net/project/freetype/freetype2/%{version}/freetype-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/project/freetype/freetype-demos/%{version}/ft2demos-%{version}.tar.xz
Source10:       https://downloads.sourceforge.net/project/freetype/freetype2/%{version}/freetype-%{version}.tar.xz.sig
Source11:       https://downloads.sourceforge.net/project/freetype/freetype-demos/%{version}/ft2demos-%{version}.tar.xz.sig
Source12:       freetype2.keyring
Source1000:     bnc628213_test.otf
Source1004:     bnc629447_sigsegv31.ttf
Source1013:     bnc633938_badbdf.0
Source1015:     bug-641580_CVE-2010-3311.cff
Source1016:     bug-647375_tt2.ttf
# silence our clamav check
NoSource:       1000
# PATCH-FIX-UPSTREAM overflow.patch -- I: Statement is overflowing a buffer
Patch201:       overflow.patch
# PATCH-FIX-OPENSUSE don-t-mark-libpng-as-required-library.patch -- it is private in .pc
Patch202:       don-t-mark-libpng-as-required-library.patch
Patch308961:    bugzilla-308961-cmex-workaround.patch
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
Requires:       ftbench = %{version}-%{release}
Requires:       ftdiff = %{version}-%{release}
Requires:       ftdump = %{version}-%{release}
Requires:       ftgamma = %{version}-%{release}
Requires:       ftgrid = %{version}-%{release}
Requires:       ftinspect = %{version}-%{release}
Requires:       ftlint = %{version}-%{release}
Requires:       ftmulti = %{version}-%{release}
Requires:       ftstring = %{version}-%{release}
Requires:       ftvalid = %{version}-%{release}
Requires:       ftview = %{version}-%{release}
Conflicts:      dtc < 1.4.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Freetype2 utilities and demo programs.

%package -n ftbench
Summary:        Run FreeType benchmarks
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftbench
Run FreeType benchmarks
This tool is part of the FreeType project

%package -n ftdiff
Summary:        Compare font hinting modes
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftdiff
Compare font hinting modes
This tool is part of the FreeType project

%package -n ftdump
Summary:        Simple font dumper
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftdump
Simple font dumper
This tool is part of the FreeType project

%package -n ftgamma
Summary:        Screen gamma calibration helper
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftgamma
Screen gamma calibration helper
This tool is part of the FreeType project

%package -n ftgrid
Summary:        Simple glyph grid viewer
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftgrid
Simple glyph grid viewer
This tool is part of the FreeType project

%package -n ftinspect
Summary:        Shows how a font gets rendered by FreeType
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftinspect
Shows how a font gets rendered by FreeType, allowing
control over virtually all rendering parameters
This tool is part of the FreeType project

%package -n ftlint
Summary:        Simple font tester
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftlint
Simple font tester
This tool is part of the FreeType project

%package -n ftmulti
Summary:        Multiple masters font viewer
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftmulti
Multiple masters font viewer
This tool is part of the FreeType project

%package -n ftstring
Summary:        String viewer
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftstring
String viewer
This tool is part of the FreeType project

%package -n ftvalid
Summary:        Layout table validator
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftvalid
Layout table validator
This tool is part of the FreeType project

%package -n ftview
Summary:        Simple glyph viewer
Group:          Productivity/Publishing/Other
Conflicts:      %{name} < %{version}-%{release}

%description -n ftview
Simple glyph viewer
This tool is part of the FreeType project

%prep

%setup -q -n freetype-%{freetype_version} -b 1
%patch308961 -p 1
pushd ../ft2demos-%{version}
%patch201 -p1
popd
%patch202 -p1

%build
export CFLAGS="%{optflags} -std=gnu99 -D_GNU_SOURCE $(getconf LFS_CFLAGS)"
%configure \
    --enable-static \
    --without-bzip2

make %{?_smp_mflags}
pushd ..
    ln -s freetype-%{freetype_version} freetype2
    cd ft2demos-%{version}
    make %{?_smp_mflags}

    cd src/ftinspect
    sed -i s/"-isystem "/"-I "/ ftinspect.pro
    qmake-qt5 ftinspect.pro
    make
popd

%install
mkdir -p %{buildroot}%{_bindir}
pushd ../ft2demos-%{version}/bin/.libs
    install -m 755 ft* %{buildroot}%{_bindir}
    install -m 755 ../../src/ftinspect/ftinspect %{buildroot}%{_bindir}
popd

%check
%{buildroot}%{_bindir}/ftbench -c 1 %{SOURCE1000}
%{buildroot}%{_bindir}/ftbench -c 1 %{SOURCE1004} |& grep -v "couldn't load font resource" && echo "should fail"
%{buildroot}%{_bindir}/ftbench -c 1 %{SOURCE1013} |& grep -v "couldn't load font resource" && echo "should fail"
%{buildroot}%{_bindir}/ftbench -c 1 %{SOURCE1015} |& grep -v "couldn't load font resource" && echo "should fail"
%{buildroot}%{_bindir}/ftbench -c 1 %{SOURCE1016}

%files
%defattr(-,root,root)
%doc README

%files -n ftbench
%defattr(-,root,root)
%{_bindir}/ftbench

%files -n ftdiff
%defattr(-,root,root)
%{_bindir}/ftdiff

%files -n ftdump
%defattr(-,root,root)
%{_bindir}/ftdump

%files -n ftgamma
%defattr(-,root,root)
%{_bindir}/ftgamma

%files -n ftgrid
%defattr(-,root,root)
%{_bindir}/ftgrid

%files -n ftinspect
%defattr(-,root,root)
%{_bindir}/ftinspect

%files -n ftlint
%defattr(-,root,root)
%{_bindir}/ftlint

%files -n ftmulti
%defattr(-,root,root)
%{_bindir}/ftmulti

%files -n ftstring
%defattr(-,root,root)
%{_bindir}/ftstring

%files -n ftvalid
%defattr(-,root,root)
%{_bindir}/ftvalid

%files -n ftview
%defattr(-,root,root)
%{_bindir}/ftview

%changelog
