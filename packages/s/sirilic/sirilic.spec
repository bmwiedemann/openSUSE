#
# spec file for package sirilic
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           sirilic
Version:        2.0.10
Release:        0
Summary:        Siril plugin for preparing acquisition files for processing
License:        LGPL-3.0-or-later
URL:            https://gitlab.com/free-astro/sirilic
Source:         https://gitlab.com/free-astro/sirilic/-/archive/V.%{version}/sirilic-V.%{version}.tar.bz2
BuildArch:      noarch
Requires:       python3-tk
Requires:       siril >= 1.4

%description
SiriLic (SiriL Interactive Companion) is a software for preparing
acquisition files (raw, Offset, Flat and Dark) for processing with SiriL software.
It does three things:
* Structuring the SiriL working directory into sub-folders
* Convert Raw, Offset, Dark or Flat files into SiriL sequence
* Automatically generate the SiriL script according to the files present and the options
Sirilic allows also to batch process multiple channel and sessions.

SiriLic is a Siril Python script. It is installed into Siril's system script
directory and appears in Siril under "Python Script > sirilic".

%prep
%setup -q -n %{name}-V.%{version}

%build

%install
install -d %{buildroot}%{_datadir}/siril/scripts/sirilic
cp -a sirilic/. %{buildroot}%{_datadir}/siril/scripts/sirilic/
find %{buildroot}%{_datadir}/siril/scripts/sirilic -name '*.po' -delete
sed -i '1s|^#!.*env python.*|#!/usr/bin/python3|' %{buildroot}%{_datadir}/siril/scripts/sirilic/*.py

%files
%license LICENSE.txt
%doc README.md
%dir %{_datadir}/siril
%dir %{_datadir}/siril/scripts
%{_datadir}/siril/scripts/sirilic

%changelog
