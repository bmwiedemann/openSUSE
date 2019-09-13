#
# spec file for package jackEQ
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           jackEQ
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  jack-devel
BuildRequires:  ladspa-devel
BuildRequires:  libxml2-devel
#BuildRequires:  update-desktop-files
Summary:        JACK Equalization Tool for Live Performance
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Mixers
Version:        0.5.9
Release:        0
Url:            http://jackeq.sf.net
Requires:       jack
Requires:       ladspa-swh-plugins >= 0.4.3
Source:         %{name}-%{version}.tar.bz2
Patch1:         jackeq-fix-no-add-needed.patch
Patch2:         jackeq-fix_LADSPA_PATH_for_x86_64.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
jackEQ is a tool for routing and manipulating audio from and to
multiple input/output sources.	It runs in the JACK Audio Connection
Kit and uses LADSPA for its back-end DSP work.	jackEQ is designed
specifically for live performance.

%prep
%setup -q
%patch1
%patch2
chmod -x README* COPYING AUTHORS ChangeLog NEWS TODO

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%{?buildroot:%__rm -rf '%{buildroot}'}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README* TODO
%{_bindir}/jackeq
%{_datadir}/jackeq

%changelog
