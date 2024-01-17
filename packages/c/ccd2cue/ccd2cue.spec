#
# spec file for package ccd2cue
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ccd2cue
Version:        0.5
Release:        0
Summary:        CCD sheet to CUE sheet converter
License:        GPL-3.0+ and GFDL-1.3
Group:          Productivity/Multimedia/Other
Url:            https://www.gnu.org/software/ccd2cue/
# git clone git://git.savannah.gnu.org/ccd2cue.git
Source:         ftp://ftp.gnu.org/pub/gnu/ccd2cue/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.gnu.org/pub/gnu/ccd2cue/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=81839/%{name}.keyring
Recommends:     %{name}-doc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GNU ccd2cue is a CCD sheet to CUE sheet converter.  It supports the full
extent of CUE sheet format expressiveness, including mixed-mode discs
and CD-Text meta-data.

%package doc
Summary:        Documentation for ccd2cue and the CCD and CUE sheet formats
License:        GFDL-1.3
Group:          Documentation/Other
Requires:       %{name} = %{version}
Requires(post): info
Requires(preun): info
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif
# TODO: HTML documentation with doxygen

%description doc
GNU ccd2cue is a CCD sheet to CUE sheet converter.  It supports the full
extent of CUE sheet format expressiveness, including mixed-mode discs
and CD-Text meta-data.

This package contains the documentation, including free documentation on
the CCD and CUE sheet formats.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%check
make %{?_smp_mflags} check

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%defattr(-,root,root)
%doc ANNOUNCEMENT AUTHORS ChangeLog COPYING DONORS NEWS README THANKS TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_mandir}/??.UTF-8
%dir %{_mandir}/??.UTF-8/man1
%{_mandir}/*/man1/%{name}.1*

%files doc
%defattr(-,root,root)
%doc GNU-FREE-DOCUMENTATION-LICENSE LINUX-AND-THE-GNU-SYSTEM THE-GNU-MANIFESTO WHY-FREE-SOFTWARE-NEEDS-FREE-DOCUMENTATION WHY-SOFTWARE-SHOULD-NOT-HAVE-OWNERS
%{_infodir}/%{name}.info.gz

%changelog
