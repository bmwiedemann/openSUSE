#
# spec file for package sirilic
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


Name:           sirilic
Version:        1.15.7
Release:        0
Summary:        Software that uses SiriL for preparing acquisition files for processing
License:        LGPL-3.0-or-later
URL:            https://gitlab.com/free-astro/sirilic
Source:         https://gitlab.com/free-astro/sirilic/-/archive/V%{version}/sirilic-V%{version}.tar.bz2
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(python3) >= 3.6
Requires:       siril >= 1.0.6
BuildArch:      noarch
%if 0%{?fedora_version} >= 30 || 0%{?centos_version} >= 8
BuildRequires:  python-wxpython4 >= 4.0
Requires:       python-wxpython4 >= 4.0
%endif
%if 0%{?suse_version} >= 1530
BuildRequires:  python3-wxPython >= 4.0
Requires:       python3-wxPython >= 4.0
%endif

%description
SiriLic ( SiriL Image Converter) is a software for preparing
acquisition files (raw, Offset, Flat and Dark) for processing with SiriL software.
It does three things:
* Structuring the SiriL working directory into sub-folders
* Convert Raw, Offset, Dark or Flat files into SiriL sequence
* Automatically generate the SiriL script according to the files present and the options
Sirilic allows also to batch process multiple channel and sessions.

%prep
%setup -q -n %{name}-V%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python3/g' %{buildroot}/%{python3_sitelib}/%{name}/*.py
sed -i 's/\/usr\/bin\/env python/\/usr\/bin\/python3/g' %{buildroot}/%{python3_sitelib}/%{name}/*.pyw
rm -f %{buildroot}/%{python3_sitelib}/%{name}/i18n/fr_FR/LC_MESSAGES/sirilic.mo

%files
%{_bindir}/sirilic
%{_datadir}/applications/sirilic.desktop
%{_datadir}/pixmaps/sirilic.png
%{python3_sitelib}/*

%changelog
