#
# spec file for package python-discid
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2013 Johannes Dewender <novell@JonnyJD.net>
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


%{?sle15allpythons}
Name:           python-discid
Version:        1.2.0
Release:        0
Summary:        Python binding of Libdiscid
License:        LGPL-3.0-or-later
URL:            https://github.com/JonnyJD/python-discid
Source:         https://files.pythonhosted.org/packages/source/d/discid/discid-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libdiscid) >= 0.2.2
# no automatic requires since libdiscid is not linked
# Can't use %_libdir due to noarch
Requires:       %(rpm -qf $(readlink -qne /usr/lib*/libdiscid.so) --qf '%%{NAME} >= %%{VERSION}')
BuildArch:      noarch
%python_subpackages

%description
Python-discid implements Python bindings for MusicBrainz Libdiscid.

Libdiscid's main purpose is the calculation of an identifier of audio
discs (disc id) to use for the MusicBrainz database.

That identifier is calculated from the TOC of the disc, similar to the
freeDB CDDB identifier. Libdiscid can calculate MusicBrainz Disc IDs and
freeDB Disc IDs.
Additionally the MCN of the disc and ISRCs from the tracks can be extracted.

This module is a close binding that offloads all relevant data
storage and calculation to Libdiscid. On the other hand it gives a
pythonic API and uses objects and exceptions.

%prep
%setup -q -n discid-%{version}
sed -i "s|^#!%{_bindir}/env python$|#!%{_bindir}/python3|" examples.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip tests that require /dev/sr0
%pytest -k "not (test_read_simple or test_read_put or test_read_features)"

%files %{python_files}
%license COPYING COPYING.LESSER
%doc CHANGES.rst README.rst
%{python_sitelib}/discid
%{python_sitelib}/discid-%{version}.dist-info

%changelog
