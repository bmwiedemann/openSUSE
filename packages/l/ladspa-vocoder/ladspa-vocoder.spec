#
# spec file for package ladspa-vocoder
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ladspa-vocoder
Version:        0.4
Release:        0
Summary:        LADSPA vocoder plugin
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.sirlab.de/linux/download_vocoder_ladspa.html
Source:         https://www.sirlab.de/linux/download/vocoder-ladspa-%{version}.tgz
Patch1:         vocoder-0.1.dif
BuildRequires:  gcc
BuildRequires:  ladspa-devel
Supplements:    ladspa
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides a LADSPA (Linux Audio Developer's Simple Plug-in API)
vocoder plugin.

%prep
%setup -q -n vocoder-%{version}
%patch1

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
%make_build CFLAGS="%{optflags} -fPIC"

%install
%make_install INSTALL_PLUGINS_DIR=%{buildroot}%{_libdir}/ladspa

%files
%license COPYRIGHT
%doc README
%{_libdir}/ladspa

%changelog
